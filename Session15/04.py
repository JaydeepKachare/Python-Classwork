# demo program for file handling 



def main() : 
    name = input("Enter file name to create : ")
    fobj = open(name,"w")                 # create new file for write 

    str = input("Enter data to write in file : ")
    fobj.write(str) 

    

if __name__ == "__main__" : 
    main() 
