# Returns true for Palindrome
def check_if_number_is_palindrome(x):
    # string x
    string_x =  str(x)

    # reverse string x 
    string_x_reversed =  string_x[::-1]


    if int(string_x) == int(string_x_reversed):
        return True
    else:
        return False
