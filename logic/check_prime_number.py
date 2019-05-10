
from math import sqrt,floor

# Returns true if  number is prime
def check_if_number_is_prime(x):
    # one is not prime
    if x == 1 :
        return False

    # 2 is prime
    if x == 2:
        return True

    # if greater than two and even then not prime
    if x > 2 and x % 2 == 0:
        return False
    

    # 
    # get max divisor and plus 1
    max_divisor =  (floor(sqrt(x))) + 1

    # check range of odd numbers if they divide x without a remainder
    for number in range(3, max_divisor, 2):
        if x % number == 0:
            return False

    # if it fails range check, then it is a prime
    return True