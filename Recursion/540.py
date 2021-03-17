# check whether if string is palindrome or not 


def isPalindrome(str) : 
    if len(str)==0 or len(str)==1 : 
        return True 
    
    if str[0] == str[-1] : 
        return isPalindrome(str[1:-1])
    else : 
        return False 


str = input("Enter string : " ) 
if isPalindrome(str) == True  : 
    print("Palindrome")
else : 
    print("Not Palindrome")