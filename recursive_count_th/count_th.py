'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # Base case (if it's less than 2)
    if len(word) < 2: 
        return 0
    # If first two words == "th"
    elif word[:2] == "th":
    # Return 1 and recursively call count_th at index 2 since we found one at the first two to find more "th"
        return 1 + count_th(word[2:])
    # Else recursively call count_th to look at 1st letter 
    return count_th(word[1:])
    
print(count_th('asdththnbnbthvmvmvmvth'))