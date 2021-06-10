# demo program for file handling 



def main() : 
    name = input("Enter file name to open : ")
    fobj = open(name,"r")                 # open file to read data 

    size = int(input("Enter no of bytes to read : "))
    print(fobj.read(size) )
    

if __name__ == "__main__" : 
    main() 
