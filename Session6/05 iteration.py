
def loop(message,val=5) :
    counter = 0 
    while counter < val :
        print(message)
        counter = counter + 1 

def main() :
    message = str(input("Enter message to display   :   "))
    val = int(input("how many times to write message    :   "))
    loop(message,val)


if __name__ == "__main__" : 
    main() 