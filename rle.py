# This challenge also comes from LinkedinLearning. 
# The idea was to make a Run Length Encoding function, but where each variable is stored as tuples in a list. 
# THEN you had to build a second function that decodes that list of tuples and returns the original before it was encoded. 

# This was my successful attempt! Please don't ask me how long this took oh my God. 

def encodeString(stringVal):
    prev_char = stringVal[0]
    counter = 1
    encodedList = []
    final_tuple = None
    for char in stringVal[1:]:
        if prev_char == char:
            counter += 1
        else:
            encodedList.append((prev_char, counter))
            prev_char = char
            counter = 1
    else:
        encodedList.append((prev_char, counter))
        print(encodedList)

    return encodedList

def decodeString(encodedList):
    decodedString = ''
    for i, j in encodedList:
        var = i * j
        decodedString += var
        print(var)

    return decodedString
   
