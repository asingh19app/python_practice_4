# Write a Python function called max_num()to find the maximum of three numbers.
#using built-in max function
def max_num(num1, num2, num3):
   max_number = max(num1, num2, num3)
   print(max_number)   
max_num(4,5,6)

#using if and elifs
def max_number(num1, num2, num3):
   if num1 > num2 and num1 > num3:
      return num1
   elif num2 > num1 and num2 > num3:
      return num2
   elif num3 > num2 and num3 > num1: 
      return num3
print(max_number(4,5,6))
   

# Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(lst):
   count = 1
   for i in lst:
      count*=i
   print(count)

lst = [4,5,6]
mult_list(lst)

#Write a Python function called rev_string() to reverse a string
def rev_string(string):
   return string[::-1]

print(rev_string('Hello World'))

def nums_within(number, beginning, end):
   if number in range(beginning, end+1):
      return(True)
   else:
      return(False)

print(nums_within(3,2,4))
print(nums_within(10,2,5))

# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
# managed to print out total accumlative value
def pascal(number_of_rows):
    a = 1
    b = 1
    num = (a+b)**number_of_rows
    for i in range(1,num):
        print(i)

pascal(5)

