# Homework
## Functions

####! 1. Find the smallest number

#Write a function `smallest` that accepts a List of numbers as an argument.

from re import L


def smallest(nums = [ ]):
    
    for i in nums:
        if i < nums[0]:
            small_num = i
    return small_num       

small_num = smallest([100, 50, 69, 420 ,45, 2])

print(small_num)

#it should return the smallest number in the List.

####! 2. Find the largest number

#Write a function `largest` that accepts a List of numbers as an argument.

#It should return the largest number in the List.

def largest(nums = [ ]):
    
    for i in nums:
        if i > nums[0]:
            large_num = i
    return large_num

large_num = largest([100, 50, 69, 420 ,45, 2])

print(large_num)

####! 3. Find the shortest String

#Write a function `shortest` that accepts a List of Strings as an argument.

def shortest(words = []):
    for i in words:
        if len(i) < len(words[0]):
            short_word = i
    return short_word

shortest_word = shortest(['both', 'two', 'it', 'bigger'])  
print(shortest_word)      

#It should return the shortest String in the List.

####! 4. Find the longest String

#Write a function `longest` that accepts a List of Strings as an argument.

def longest(words = []):
    for i in words:
        if len(i) > len(words[0]):
            long_word = i
    return long_word

longest_word = longest(['both', 'two', 'it', 'bigger'])  
print(longest_word) 

#It should return the longest String in the List.



