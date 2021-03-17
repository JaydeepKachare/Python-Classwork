import os 
import multiprocessing

def process1(no) :
    print("Process1 is created ")
    print("PID of process1 : ",os.getpid())
    print("PID of parent process1 : ",os.getppid())
    for i in range(no) : 
        print("process1 : ",i )


def process2(no) :
    print("Process2 is created ")
    print("PID of process2 : ",os.getpid())
    print("PID of parent process2 : ",os.getppid())
    for i in range(no) : 
        print("process1 : ",i )


def main() : 
    print("Inside main process ")
    print("PID of current process : ",os.getpid())
    print("PID of parent process : ",os.getppid())

    value = 20

    p1 = multiprocessing.Process(target=process1, args=(value,))
    p2 = multiprocessing.Process(target=process2, args=(value,))

    p1.start()  
    p2.start() 

    p1.join() 
    p2.join() 

    print("main end")


if __name__ == "__main__" :
    main()  

