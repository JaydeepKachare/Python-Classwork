
i=1                 # define global variable 
def fun() :
    global i        # declare global variable => can not define again
    print(i)
    i = i+1 
    fun()


def main() :
    fun() 



if __name__ == "__main__" :
    main() 