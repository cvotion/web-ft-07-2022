
#! 1. Write a function called power which accepts a base and an exponent.
# The function should return the power of the base to the exponent.

from ast import expr_context


def power(base, exponent):
    if exponent == 0:
        return 1
    
    return base * power(base, exponent - 1)  
    
print(power(4, 3))      

#! 2. Write a function called factorial which accepts a number and returns
#! the factorial of that number.  A factorial is the product of an
#! interger and all the integers below it; eg. , factorial four( 4!) is
#! equal to 24, because 4 * 3 * 2 * 1 equals 24.  factorial zero (0!) is always 1.

def factorial(number):
    if number == 0:
        return 1
    return number * factorial(number - 1)
    # else:
    #     while hold > 0:
    #         sum *= hold
    #         hold -= 1
    # return sum
print(factorial(4))

#! 3. Write a function called recursiveRange which accepts a number and adds up all
#! the numbers from 0 to the number passed to the function

def recursiveRange(number):
    if number == 0:
        return 0
    return number + recursiveRange(number - 1)
    # sum = 0
    # for i in range(0, number+1):
    #     sum += i
    # return sum
print(recursiveRange(3))

#todo### 4. Write a recursive function called reverse which accepts
#todo### a string and returns a new string in reverse
# i = -1
# def reverse(string):
#     newStr = ''
#     string = list(string)
#     i += 1
#     if len(newStr) == len(string):
#         return
#     return newStr + reverse(string[i])

def reverse(s):
    
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]

print(reverse('taco'))

#! 5. Write a recursive function called isPalindrome which returns
#! true if the string passed to it is a palindrome (reads the same forward and backward).
#! Otherwise returns false.


#* isPalindrome('awesome') // false
#* isPalindrome('foobar') // false
#* isPalindrome('tacocat') // true
#* isPalindrome('amanaplanacanalpanama') // true
#* isPalindrome('amanaplanacanalpandemonium') // false


#! 6. Write  function called product ofArray which takes in
#! an array of numbers and returns the product of them all


#! 7. Write a recursive function called fib which accepts a number and
#! returns the ninth number in the Fibonacci Sequence. Recall that the
#! Fibonacci Sequence is the Sequence of whole numbers 1, 1, 2, 3, 5, 8, ... which
#! starts with 1 and 1, and where every number
#! thereafter is equal to the sum of the previous two numbers.