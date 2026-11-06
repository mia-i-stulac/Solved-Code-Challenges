# So this code challenge was very specific in how it wanted the algorithm to work
# The idea that was wanted was for there to be a list of prime numbers, just starting with 2
#    Then when the factorial is checked to see if its divisible by the nums in the list, if its not divisible by any, its prime and gets added to the list. 
#       So for example, 3 is not divisible by 2, so its prime, *adds to list*, 4 is divisible by 2, skip, 5 is not divisible by 2 or 3 *adds to list* and so on.
# Are there much more efficient ways to do this? abvsolutely. But it wanted this specific framework to check comprehension of nested for loops
#    And guess what my biggest error was in this challenge? *indentation* :)))))) 

def allPrimesUpTo(num):
    prime_nums = [2]
    for number in range (3, num):
        for i in prime_nums:
            if number % i == 0:
                print(f'{number} is divisible by {i}, passing it...') 
                break
        else:
            print(f'{number} is prime I think, adding it...')
            prime_nums.append(number)      
    return prime_nums
