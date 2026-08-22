hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None

def hexToDec(hexNum):
    # Step 1: base case 
    for char in hexNum:
        if char not in hexNumbers:
            print(f'{hexNum} is not a valid hexadecimal')
            return None
    if len(hexNum) == 3:
        piece = hexNum[0]
        of = hexNum[1]
        shit = hexNum[2]
        hexNum = hexNumbers[piece] * 256 + hexNumbers[of] * 16 + hexNumbers[shit]
    elif len(hexNum) == 2:
        fucking = hexNum[0]
        shit = hexNum[1]
        hexNum = hexNumbers[fucking] * 16 + hexNumbers[shit]
    else: 
        shit = hexNum[0]
        hexNum = hexNumbers[shit]   

    return hexNum

    # I did have to use the hints for tis exercise, (for the first for loop)
    # I couldn't figure out how to iterate through each number
    # And I am sure there is a much more efficient version than this code... 
    # BUT YOU KNOW WHAT THE VARIABLES MADE ME LAUGH!!!
