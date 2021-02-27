# Functions.py

# 1 : function accept nothing  and return nothing 
def fun() :
    print("function fun")

# 2 : function accept parameter and return nothing 
def gun(no) :
    print("function gun with paramter   :   " ,no)

# 3 : function accept paramter and return value 
def sun(no):
    print("function sun with parameter  :   ",no)
    return no+1 
    
# 4 : function accepts multiple values and return  multiple values
def AddSub (num1, num2) : 
    add = num1 + num2 
    sub = num1 + num2 
    return num1,num2

# 5 : nested function definition 
def marvellous() :
    print("inside marvellous")
    def infosystem() :
        print("inside infosystem")
    infosystem() 

def main() :
    fun() 
    gun(11)
    ret = sun(10)
    print("return value of sun is   :   ",ret)
    add,sub = AddSub(30,20) 
    print("Addition : ",add)
    print("Subtraction : ",sub)
    marvellous() 
    

if __name__ == "__main__" : 
    main() 