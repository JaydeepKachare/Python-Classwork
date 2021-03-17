# get information about your machine 

import os 


def main() :
    print("Inside main")

    print("Number of CPU : ",os.cpu_count())
    print("Ram Size : ",os.uname())



if __name__ == "__main__" : 
    main()