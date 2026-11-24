# This challenge comes from Linkedin Learning once again
# the challenge was to create a custom annotation that handles bad arguments
# then to call that custom error annotation within a wrapper. 
# so the "check" function runs before the actual function so it checks to make sure the numbers are ints
# and if they aren't ints, the custom error triggers, and if not, the sum function proceeds as normal

# I did get a correct working version 30 min in, but the code was super sloppy and I didn't understand how it worked
# and it was redundant... so I took the extra time to modify the code to be cleaner and more efficient... and still be correct
# and this was the final version I stuck with!

def handleNonIntArguments(func):
    def wrapper(*args): 
        for arg in args:
            if type(arg) is not int:
                print('this should only print if its inorrect')
                raise NonIntArgumentException
            else: 
                continue
        return func(*args)
    return wrapper

class NonIntArgumentException(Exception):
    print('Not all the arguments in here are integers...')
    pass

# this code was already given, as it calls the test case and it's just the basic sum function
@Answer.handleNonIntArguments
def sum(a, b, c):
    return a + b + c

try:
    result = sum(1, 2, 'a')
    print('This should not print out')
except Answer.NonIntArgumentException as e:
    print('Hooray!')
