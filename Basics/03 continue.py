


def main() :
    
    # for i in range(0,5) : 
    #     if i==3 : 
    #         print("I understand meaning of continue")
    #         continue 
    
    #     print("Number = ",i)

    num = 1 
    while num < 5 : 
        if num == 3 : 
            print("I understand meaning of continue") 
            num += 1 
            continue

        print("Number = ",num)
        num += 1 


if __name__ == "__main__" : 
    main() 