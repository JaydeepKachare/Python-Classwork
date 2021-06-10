# demo program for file handling 



def main() : 
    name = input("Enter file name to open : ")
    fobj = open(name,"r")                 # open file to read data 

    print(fobj.read() )
    

if __name__ == "__main__" : 
    main() 
