# This challenge came from freecodecamp.org's daily challenges

# Bingo Range
## Given a bingo letter, return the number range associated with that letter.
## Return an array with all numbers in the range from smallest to largest.

# My Code: 

def get_bingo_range(letter):
    bingo_dict = {
    "B": [1, 15],
    "I": [16, 30],
    "N": [31, 45],
    "G": [46, 60],
    "O": [61, 75]
    }
    letter = bingo_dict[letter]
    high_range_int = letter[1] + 1
    low_range_int = letter[0] 
    letter = list(range(low_range_int, high_range_int))
    print(letter)
    return letter

# Test
get_bingo_range("B") 