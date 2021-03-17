# Python multithreading 

import threading

Amount = 1000

def ATM(func,lock) : 
    func(lock) 


def deposit(lock) : 
    lock.acquire()
    amt = int(input("Enter amout to deposit : "))
    global Amount
    Amount += amt 
    print("Deposit Successfull --> Balance : ",Amount)
    lock.release()


def withdraw(lock) :
    lock.acquire()
    amt = int(input("Enter amout to withdraw : "))
    global Amount 
    if amt > Amount : 
        print("There  is no sufficient Balance")
    else :
        Amount -= amt 
        print("Withdraw Successfull --> Balance : ",Amount)
    lock.release() 


def main() :
    print("Inside main")

    lock = threading.Lock() 
    t1 = threading.Thread(target=ATM,args=(deposit,lock,))
    t2 = threading.Thread(target=ATM,args=(withdraw,lock,))

    lock.acquire()
    lock.release()
    t1.start() 

    t2.start() 

    t1.join() 
    t2.join()     


if __name__ == "__main__" : 
    main() 