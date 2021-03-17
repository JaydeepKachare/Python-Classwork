import threading
import os 


def Thread1() : 
    print(threading.get_ident() )

def Thread2() : 
    print("Thread2 is Created ")
    print("PID of Thread2 is ",os.getpid() )
    print("PID of parent of Thread2 is ",os.getppid() )


def main() : 
    print("Inside main process ")
    print("PID of current process : ",os.getpid())
    print("PID of parent process : ",os.getppid())

    Th1 = threading.Thread(target=Thread1, args=() )
    Th2 = threading.Thread(target=Thread2, args=() ) 

    Th1.start() 
    Th2.start() 

    Th1.join() 
    Th2.join() 

    print("main process End ")

if __name__ == "__main__" : 
    main() 