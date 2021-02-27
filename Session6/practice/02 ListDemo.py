# Demo for functions in list 



def main() :
    # creation of list 
    List = [] 
    
    # printing list 
    print("print empty list     : ", end=" ")
    print(List)

    # adding element to list 
    List.append(10)
    List.append(20)
    List.append(30)
    List.append("Jaydep")
    print("Print modified list  : ", end=" ")
    print(List)

    # check size of list 
    print("Size of List is      :  {} ".format(len(List)))

    # print element of list by iteratig over list 
    for i in range(0,len(List)) :
        print("List [ {} ]  :   {}".format(i,List[i]))

    print("Just trying another type ofiteration ")
    for ele in List :
        print("List element   :   {}".format(ele))

    # insert value at position
    List.insert(2,25) 
    print("List after inserting value is    {}".format(List))

    # extend : add multiple element at end of list 
    List.extend([50,60,70])
    print("List after extend is             {}".format(List))

    # remove element from list from giving value 
    List.remove(25)
    # List.remove(22)       # if value not present in list ==> Error 
    print("List after removing 25 is        {}".format(List))

    # pop function 
    List.pop() 
    print("List after pop()                   {}".format(List))
    List.pop(2)
    print("List after pop(2)                  {}".format(List))

    # return  index of element 
    print("Index of number 20 is {}".format(List.index(20)))

    # clear list 
    List.clear() 
    print("List         :   {}".format(List))


if __name__ == "__main__" : 
    main() 