# name_args - Accepts any number of named arguments and prints them in the pattern key : value one at a time.

def name_args(**kwargs):
    for i in kwargs.keys():
        print(i, ':', kwargs[i])

name_args(a = 'writing', b = 'python')


#all_true - Returns True if all the elements in an iterable are true. Hint: there is an existing built-in function that could be very helpful here.
#Yes, you are correct. Python provides a built-in function called all() that can be used to check if all the elements in an iterable are true. Here's an example:
#didnt learn this so used chatgpt
def all_true(iterable):
    return all(iterable)

#No, the all() function in Python works with any iterable object, not just lists. In Python, an iterable is any object that can be looped over, such as lists, tuples, sets, strings, dictionaries, and generators.

#The function will return True, because all the elements in the list are considered true values. In Python, any non-zero integer value is considered "truthy", so both 1 and 3 and 2 are considered true. Here's the output you can expect:
print(all_true([True, True, False]))
print(all_true([True, True, True]))
print(all_true([1, 2, 3]))
print(all_true([1, 3, 2]))

#Yes, you are correct. Python provides a built-in function called any() that can be used to check if at least one element in an iterable is true. Here's an example of how you could use it to implement the one_true() function:

#one_true - Returns True if one of the elements in an iterable is true. Hint: there is an existing built-in function that could be very helpful here.

def one_true(iterable):
    return any(iterable)

print('This is ',one_true([False, True, True]))

#recursive_factorial - Uses recursion to find the factorial of an integer.
def recursive_factorial(n):
    if n == 0:
        return 1
    else:
        return n*(recursive_factorial(n-1))
    
print(recursive_factorial(4))


