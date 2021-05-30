# Calvin Todd
# CS 325
# 5.29.21
# Portfolio Project: Pattern Match

def patternmatch(string, p):
    """
    This method takes a pattern where '*' cna equal any string of characters (or none), and '?' matches any single
    character.  It returns True if the pattern matches the provided string.
    """
    n = len(string)
    m = len(p)
    dp_array = [[0 for i in range(m+1)] for j in range(n+1)]

    for j in range(n+1):
        for i in range(m+1):
            if i == 0 or j == 0:
                if i == 0 and j == 0:
                    dp_array[j][i] = True
                elif j == 0 and p[i-1] == '*':
                    dp_array[j][i] = dp_array[j][i-1]
                else:
                    dp_array[j][i] = False
            elif p[i-1] == string[j-1] or p[i-1] == '?':
                dp_array[j][i] = dp_array[j-1][i-1]
            elif p[i-1] == '*':
                if dp_array[j-1][i] == True or dp_array[j][i-1] == True:
                    dp_array[j][i] = True
                else:
                    dp_array[j][i] = False
            else:
                dp_array[j][i] = False

    return dp_array[n][m]

