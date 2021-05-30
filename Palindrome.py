# Calvin Todd
# CS 325
# 5.28.21
# Portfolio Project: Palindrome

def checkPalindrome_1(string, k):
    """
    Implements a recursive brute force approach to discovering if the given string is a k-palindrome where k is the
    MAXIMUM amount of letters able to br removed from the sting to create a palindrome.  Will return True if true, or
    False if false.
    """
    # reverse the string
    reverse = string[::-1]
    # if k is 0, or as many letters have been removed from the string as possible
    if k == 0:
        if reverse == string:
            return True
        else:
            return False

    # if k is not 0, check to see if palindrome is valid, if not make iterative recursive call:
    else:
        if reverse == string:
            return True
        else:
            for letter in string:
                adjusted_string = string.replace(letter, '')
                truth = checkPalindrome_1(adjusted_string, k - 1)
                if truth:
                    return truth
    return truth

def checkPalindrome_2(string, k):
    """
    This method will check is a string is a k-palindrome using a Dynamic Programming approach
    """
    reversed_string = string[::-1]
    n = len(string)
    dp_array = [[0 for i in range(n+1)] for i in range(n+1)]

    for j in range(n+1):
        for i in range(n+1):
            if i == 0 or j == 0:
                dp_array[j][i] = i + j
            elif string[i - 1] == reversed_string[j - 1]:
                dp_array[j][i] = dp_array[j-1][i-1]
            else:
                dp_array[j][i] = min(dp_array[j-1][i] + 1, dp_array[j][i-1] + 1)

    if dp_array[n][n] <= (2 * k):
        return True
    else:
        return False

