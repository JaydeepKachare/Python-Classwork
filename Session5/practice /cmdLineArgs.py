# program for accepting command line argument 
import sys 

def main() :
    print("inside main function")
    print("length of command line arguments :   ",len(sys.argv))
    print("First argument : ",sys.argv[0])
    print("Second argument : ",sys.argv[1])
    print("Third argument : ",sys.argv[2])
    print("Fourth argument : ",sys.argv[3])


# starter function 
if __name__ == "__main__" : 
    main() 