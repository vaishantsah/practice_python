import re

def pat(str:str,to_find:str)->str:
    """
    Returns the number at which we find the certain pattern given by the user
    params:
        str    : The string input in which th pattern is to be checked for
        to_find: Takes the pattern to be looked for in the str above
    """

    patterns=re.compile(to_find)
    text=str
    matches=patterns.finditer(text)
    for match in matches:
        print(match)

if __name__=='__main__':
    sentence=input("Enter the sentence to find the pattern in. \n")
    pattern_to_find=input("Enter the pattern -> ")
    pat(sentence,pattern_to_find)