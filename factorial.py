# This was a factorital challenge I did in LinkedinLearning's Python Essential Training

# Desc: Build a factorial function
# Example: n! = n * (n - 1) * (n - 2) ......

def factorial(num):
    #base case (exceptions rules)
    if type(num) != int:
        return None
    elif num == 0:
        return 1
    elif num < 0:
        return None
    #actual factorial function
    count = 1
    while num > 0:
        count = count * num
        num = num - 1
    return count

# This code passed all the tests! Yay! :)
