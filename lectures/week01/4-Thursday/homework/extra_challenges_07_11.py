# # Extra Challenge

#! #### 1. Tic-Tac-Toe



# Continue the Tic-Tac-Toe example from the nested for-loop example

#! #### 2. Matrix Multiplication

# Given two two-dimensional lists of numbers of the size 2x2 - calculate the result of multiplying the two matrices. Print the resulting matrix. 

from copy import copy


def matrix_mult(nums1= [[ ], [ ]], nums2 = [[ ], [ ]]):
    
    nums3 = [[0, 0], [0, 0]]

    for i in range(len(nums1)):
        for j in range(len(nums1[0])): 
            nums3[i][j] = nums1[i][j] * nums2[i][j] 
    return nums3

matrix = matrix_mult([[1, 2],[3, 4]], [[5, 6],[7, 8]])

print(matrix)
# How do you multiple two matricies?

# For more information, go to [this video on khanacademy](https://www.khanacademy.org/math/precalculus/precalc-matrices/multiplying-matrices-by-matrices/v/matrix-multiplication-intro
# )

# Extra Challenge


#! ### 1. Tic-tac-toe 
board = [[[0],[0],[0]],[[0],[0],[0]],[[0],[0],[0]]]
print(f"{board[0]} << Row 0")
print(f"{board[1]} << Row 1")
print(f"{board[2]} << Row 2")
player1 = 'X'
player2 = 'Y'
playing = True

# def question():
#     row = int(input('What row do you want to move to? '))
#     location = int(input('What location on that row? '))
#     player = input('Player X or Y? ')

def move(row, location, player):
    board[row][location]=player
    copy(board)
    for i in range(len(board)):
        print(f"{board[i]} << Row {i}")    
    
while playing:
    row = int(input('What row do you want to move to? '))
    # row -= 1
    if row > 2:
        print("Sorry that is not a valid board row")
        row = int(input('What row do you want to move to? '))
        # location -= 1
    location = int(input('What location on that row? '))
    # location -= 1
    if location > 2:
        print("Sorry that is not a valid board location")
        location = int(input('What location on that row? '))
        # location -= 1
    player = input('Player X or Y? ')
    move(row, location, player)
   

# Write a function `move` that accepts three arguments:

# - `board` a 2-dimensional array that represents a 3x3 tic-tac-toe board
# - `location` a 2-item tuple that specifies an cell on the `board`
# - `player` a String, either `"X"` or `"Y"`



# Return a copy of the `board` with the `player` String placed at the `location`.

# Throw an error if:

# - The `board` is the wrong size
# - The `location` is already occupied by a player
# - The `location` is invalid
# - The `player` String is something other than `"X"` or `"Y"`

#! #### 2. Change maker

# You will write a function that calculates how many bills and coins someone would receive as change.

# Write a function `make_change` that accepts two arguments:

# - `total_charge` - the amount of money owed
# - `payment` - the amount of money payed

# Return a 2-dimensional tuple whose values represent the bills and coins.

# For example, consider the following tuple:

# ```py
# (
#   (3, 0, 1, 1, 0, 1), 
#   (4, 1, 0, 2)
# )
# ```

# The first item represents the bills:

# - 3 singles
# - 0 fives
# - 1 ten
# - 1 twenty
# - 0 fifties
# - 1 hundred

# The second item represents the coins

# - 4 pennies
# - 1 nickel
# - 0 dimes
# - 2 quarters


# Hint: consider writing a small function to help produce the "bills" tuple and another function to help produce the "coins" tuple.

#! #### 3. Calculate the change value

# Write a `value_of_change` function that accepts a 2-dimensional tuple like the one returned by the `make_change` function.

# This function should calculate the monetary value specified by the tuple.

# For example, if the following tuple were passed to `value_of_change`

# ```py
# (
#   (3, 0, 1, 1, 0, 1), 
#   (4, 1, 0, 2)
# )
# ```

# It would return `133.59`

# As before, consider writing helper functions to deal with the bills and the coins separately.
