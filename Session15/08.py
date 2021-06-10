# demo program for file handling 



def main() : 
    name = input("Enter file name to open : ")
    fobj = open(name,"r")                 # open file to read data 

    print("Data from file is : ")

    for data in fobj : 
        print(data)
            
  
if __name__ == "__main__" : 
    main() 
