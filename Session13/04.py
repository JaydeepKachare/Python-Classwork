import os 
import multiprocessing
import threading

def Thread1(no) :
    print("Thread1 is created ")
    print("PID of Thread1 : ",os.getpid())
    print("PID of parent thread1 : ",os.getppid())
    for i in range(no) : 
        print("Thread1 : ",i )


def Thread2(no) :
    print("Thread2 is created ")
    print("PID of Thread2 : ",os.getpid())
    print("PID of parent Thread2 : ",os.getppid())
    for i in range(no) : 
        print("Thread2 : ",i )


def main() : 
    print("Inside main process ")
    print("PID of current process : ",os.getpid())
    print("PID of parent process : ",os.getppid())

    value = 20

    t1 = threading.Thread(target=Thread1, args=(value,))
    t2 = threading.Thread(target=Thread2, args=(value,))

    t1.start() 
    t2.start() 

    t1.join() 
    t2.join()

    print("main end")


if __name__ == "__main__" :
    main()  

