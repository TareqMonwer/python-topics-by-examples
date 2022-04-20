def is_palindrome(string):
    if len(string) == 0 or len(string) == 1:
        return True
    

    if string[0] == string[len(string)-1]:
        return is_palindrome(string[1:len(string)-1])

    return False



if __name__ == "__main__":
    print(is_palindrome('aka'))


# Call-Stack
# is_palindrome('aka')      str: aka
# -> string[0] = 'a' == string[2] == 'a'
    # is_palindrome('k')   str: k