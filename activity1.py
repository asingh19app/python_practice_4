# arb_args - Takes in any number of arguments and prints them one at a time.
# inner_func - Takes in two integers. Two nested functions should perform separate, distinct math operations using the integers. The result of both nested functions should then be added together and printed.
# lunch_lady - Takes in two strings: a student's name and their lunch preference. The function should print both strings. If a lunch preference is not given, "Mystery Meat" should be printed instead.
# sum_n_product - Accepts two integers and returns both the sum and the product.
# arb_mean - Accepts any number of integers and prints their average.
# arb_longest_string - Accepts any number of strings and returns the longest one.

def arb_args(*args):
    for i in args:
        print(i)

arb_args('pie', 'juice', 'apple')

def inner_func(num1, num2):
    def add_nums(inner_num1):
        return inner_num1 + 5
    
    def sub_nums(inner_num2):
        return inner_num2 - 2
    
    return add_nums(num1) + sub_nums(num2)

print(inner_func(10,10))

def lunch_lady(stu_name, food = 'Mystery Meat'):
    print(stu_name, food)

lunch_lady('Adesh', 'Beef')


def sum_n_product(num1, num2):
    print(num1+num2)
    print(num1*num2)

sum_n_product(5,5)

def arb_mean(*nums):
    count = 0
    sum = 0
    for i in nums:
        sum+=i
        count+=1
        return sum/count
    
print(arb_mean(3,4,5))

def arb_longest_string(*words):
    longest_word = ' '
    for i in words:
        if len(i) > len(longest_word):
            longest_word = i
    print(longest_word)

arb_longest_string('pie', 'shoe', 'Adeshvir')
