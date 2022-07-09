# # Homework
# ## Iterative Programming


#? #### 1. Multiply Vectors

# Given two lists of numbers of the same length, create a new list by multiplying the pairs of numbers in corresponding positions in the two lists. Example:

# ```
# [2, 4, 5] x [2, 3, 6] = [4, 12, 30]
# ```
from dataclasses import replace
from ntpath import join
from re import X
from weakref import WeakValueDictionary


list1 = [2, 4, 5]
list2 = [2, 3, 6]
new_list = []

for i in range(0, len(list1)):
    new_list.append(list1[i] * list2[i])
    
print(new_list)

#? #### 2. Matrix Addition

# Given two two-dimensional lists of numbers of the size 2x2 two dimensional list is represented as an list of lists:

# ```
# [ [2, -2],
#    [5, 3] ]
# ```

# Calculate the result of adding the two matrices. The number in each position in the resulting matrix should be the sum of the numbers in the corresponding addend matrices. Example: to add

# 1 3
# 2 4

# 5 2
# 1 0

# 6 5
# 3 4


x = [[1, 3], [2, 4]]
y = [[5, 2], [1, 0]]

result = [[0, 0], [0, 0]]

for i in range(len(x)):
    for j in range(len(x[0])): 
        result[i][j] = x[i][j] + y[i][j] 
for r in result:
    print(r)        

# ```
# 1 3
# 2 4
# ```
# and

# ```
# 5 2
# 1 0
# ```

# results in

# ```
# 6 5
# 3 4
# ```

#? #### 3. Matrix Addition II

# Use your solution in Matrix Addition, and extend it to work for a pair of matrices of any size, as long as they have the same size.
first = [[1, 3], [2, 4], [5, 7]]
second = [[7, 5], [4, 2],[20, 9]]
if len(first) == len(second):
    results = [[first[i][j] + second[i][j] for j in range(len(first[0]))] for i in range(len(first))]
    for r in results:
        print(r)
else:
    print("Lists aren't the same size.")
    
    
#? #### 4. De-dup

# Given a list of numbers or strings, create a new list containing the same elements as the first list, except with any duplicate values removed. Print the list.

list1 = [1, 2, 3, 4, 4, 5]
list2 = []

for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)   

     
        

#? #### 5. Leetspeak

# Given a paragraph of text as a String, print the paragraph in [leetspeak](https://en.wikipedia.org/wiki/Leet). 

# To translate a String to leetspeak, you need to replace make the following character replacements (treat all input characters as uppercase):

# | Letter | Translates To |
# |:------:|:-------------:|
# | A      | 4             |
# | E      | 3             |
# | G      | 6             |
# | I      | 1             |
# | O      | 0             |
# | S      | 5             |
# | T      | 7             |



reg_string = "I am a leet programmer"

string = reg_string.upper()

string_lst = list(string)

cypher = { "A" : "4",
            "E" : "3",
            "G" : "6",
            "I" : "1",
            "O" : "0",
            "S" : "5",
            "T" : "7",
          }
leet = ''
for i in string_lst:
    if i in cypher.keys():
        leet += cypher[i]
    else:
        leet += i    
print(leet)
# for x in string:
#     if x == "a":
#         new_string = string.replace('a', '4')
#         string = new_string
#     elif x == "e":
#         new_string = string.replace('e', '3')
#         string = new_string
#     elif x == "g":
#         new_string = string.replace('g', '6')  
#         string = new_string      
#     elif x == "i":
#         new_string = string.replace('i', '1') 
#         string = new_string
#     elif x == "o":
#         new_string = string.replace('o', '0')
#         string = new_string
#     elif x == "s":
#         new_string = string.replace('s', '5')
#         string = new_string
#     elif x == "t":
#         new_string = string.replace('t', '7')
#         string = new_string
#     else:
#         continue         

# print(new_string)
# Example: If your program is given the String `"I am a leet programmer"`, it should print `"1 4m 4 l337 pr0gr4mm3r"` as the leetspeak translation

#? #### 6. Long-long Vowels

# Given a word as a string, print the result of extending any long vowels to the length of 5. 

# Examples:

# ```
# Good => Goooood 
# Cheese => Cheeeeese 
# Man => Man 
# Spoon => Spooooon 
# ```

word = input("type a word >> ")
word = word.upper()

word_list = list(word)
double_letter = []
vowel = ['A', 'E', 'I', 'O', 'U']
double = 0

for i in word_list:
    if(i not in double_letter):
        double_letter.append(i)
    elif(i in double_letter and i in vowel and double < 1):
        double_letter.append(i*4)
        double += 1    
    elif(i in double_letter and i in vowel and double > 0):
        double_letter.append(i)

double_letter = ''.join(double_letter)
print(double_letter)
#? #### 7. Caesar Cipher

# Given a string, print the Caesar Cipher (or ROT13) of that string. What is Caesar Cipher? [Learn about it here](http://practicalcryptography.com/ciphers/caesar-cipher/).

# Use your solution to decipher the following text: "lbh zhfg hayrnea jung lbh unir yrnearq"

caesar = { 'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5', 'F': '6', 'G': '7', 'H': '8', 'I': '9', 'J': '10', 'K': '11', 'L': '12', 'M': '13', 'N': '14', 'O': '15', 'P': '16', 'Q': '17', 'R': '18', 'S': '19', 'T': '20', 'U': '21', 'V': '22', 'W': '23', 'X': '24', 'Y': '25', 'Z': '26',}

# ## Large 

#? ### Matrix Multiplication
# Given two two-dimensional lists of numbers of the size 2x2 - calculate the result of multiplying the two matrices. Print the resulting matrix.

# How do you multiple two matrices?

