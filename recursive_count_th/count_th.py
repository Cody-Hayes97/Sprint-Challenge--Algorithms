'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # return zero if the ength of the word is less than 2
    if len(word) < 2:
        return 0
    # if the word begins with th, recurse and search for th given everything in the word after the second index
    elif word[:2] == "th":
        return count_th(word[2:]) + 1
    # otherwise keep recursing through the word, taking off the first index each time until it matches the above case
    else:
        return count_th(word[1:])

