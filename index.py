"""
    Smallest Palindrome and Prime Number Pseudo Code 

    --------------------------
    get input n
    check if n is an int

    call function  find_smallest_palindrome_prime_number(n)


    function  find_smallest_palindrome_prime_number(n)
        set value_tracker <=  n
        set value_found  <= false
        while not value_found 
        if check_if_number_is_palindrome(value_tracker) and  check_if_number_is_prime(value_tracker)
            value_found = true
        return value_tracker;
    

    
    function check_if_number_is_palindrome(x)
        stringx <= string(x)
        stringxReversed  <= reverse(stringx)
               
        if int (stringx) =  int(stringxReversed)
           return true
        else 
           return false

    function check_if_number_is_prime(x)
       if x =  1
          return false
       if  x = 2
        return true

       if x > 2 and x mod 2 = 0
         return false

        
        max_divisor =  floor(squareroot(n))  + 1

        for d in range(3, max_divisor, 2)
            if x mod d == 0
               return false
        return true

"""

from sys import argv, exit

# Custom functions 
from logic.check_prime_number import check_if_number_is_prime
from logic.check_palindrome_number import check_if_number_is_palindrome


def find_smallest_palindrome_prime_number(N):
    value_found = False

    # if already a palindrome and prime target the next one 
    value_tracker =  N + 1

    # find the number 
    while not value_found:
        if check_if_number_is_palindrome(value_tracker) and check_if_number_is_prime(value_tracker):
            value_found = True
        else:
            value_tracker += 1

    return value_tracker



# this is the main module. Do this when executed directly
if __name__ == "__main__":   
    # get first argument
    consoleArgument =  argv[1]

    try:
        N = int(consoleArgument)        
    except:

        print( consoleArgument + " is not a valid Integer!\n" )

        inputValue  = input("Please enter a valid integer...")

        try:
            N =  int(inputValue)
        except:
            print("Oops. Still not an integer. Please rerun the program")  
            # exit due to user error
            exit(-1);      
        
    print("Smallest palindrome and prime number greater than  " + str(N) + " is  " +  str(find_smallest_palindrome_prime_number(N)))