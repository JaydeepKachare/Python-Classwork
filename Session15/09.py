# copy data from one file to another file 

def main() : 
    src = input("Enter source file : ")
    fsrc = open(src,"r")

    dest = input("Enter destination file : ")
    fdest = open(dest,"w")

    fdest.write(fsrc.read())

    fsrc.close() 
    fdest.close() 

    

if __name__ == "__main__" : 
    main() 