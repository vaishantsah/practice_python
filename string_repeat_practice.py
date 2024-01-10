import re
user_input="baghjklrtyu"
flag=0
print("Began")
#password=input("Enter password : ")
#Loop to keep length of the password in check
def password_check(password):
    global flag
    pattern_list=[]
    while(len(password)>8 and len(password)<=20 and flag==0): #checking if the password is greater than 8 and less than 20
        if " " in password or "\n" in password: #checking if it contains a space or a new line
            print("\nPlease do not include space or a new line in the password!\n")
            return
        else:
            # for loop to check for repeating letters
            for i in range(len(password)-2):
                if(password[i]==password[i+1] and password[i]==password[i+2]):
                    print("Please enter a password with no repeating characters\n")
                    # block to look for patterns of user input letters
                    while i<len(password)//2:
                        new_string=str(password[i]) 
                        pattern_list=list(re.findall(new_string,password))
                        new_string=new_string+password[i]
                    return
            if(len(pattern_list)>0):
#                first_element=pattern_list[0]
                print(f"A pattern {pattern_list[0]} was found in your password. Please enter a password without a pattern")
                flag=1
                return
    if(flag==0):
        print("Password is valid")
                    
if __name__=='__main__':
    password_check(user_input)