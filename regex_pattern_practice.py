import re
def regex_check(reg:str)->None:
    """
        Accepts a regex name as a string and returns if the file name follows the regex pattern '^\d{1,3}\d{14}[F|X]225\d{1,5}[A-Z0-9&]{11}\.DAT$'
        Param: reg | string, reg | non-string = error
    """
    regex_pattern= r'^\d{1,3}\d{14}[F|X]225\d{1,5}[A-Z0-9&]{11}\.DAT$'
    b = reg
    if re.match(regex_pattern,reg):
        print("Correct Regex Pattern found.")
    else:
        print("Incorrect Regex Pattern found.")

if __name__=="__main__":
    file_name=str(input("Enter the file name: \t"))
    regex_check(file_name)