# Demo of set and its method in python 

def main() :
    # creating empty set 
    set1 = set() 
    print("Empty set is     :   ",set1)

    # creating set with help of string 
    # just like construcor
    set1 = set("GeeksForGeeks")
    print("Set created by string is     :   ",set1)

    # creatiion of set with list 
    set1 = set(["Geeks" , "For" , "Geeks"])
    print("Set created with list    :   ",set1)

    # adding element inside set 
    set1 = set() 
    set1.add(10)
    set1.add(20)
    set1.add(30)
    set1.add((30,40))       # set added in set 
    # list cannot be added in set  as List is  not Hashtable 
    print("after adding element is set  :   ",set1)

    # add takes only one argument to add 
    # to add more element at a time use update method 
    set1.update([50,60,70])
    print("set1 after updating element in set   :   ",set1)
    

    # Accessing element of set 
    # for each loop works 
    for ele in set1 :
        print("Set Element is   :   ",ele)

    
    # checking element using in keyword 
    value1 = 20 in set1 
    value2 = 25 in set1

    print("20 exists in set1    :   ",value1)
    print("25 exists in set1    :   ",value2)


    # remove element from set 
    # remove() --------> KeyError if Element does not exist in set
    # discard() -------> No Error if Element does not exist in set
    
    set1.remove(10)
    # set.remove(11)
    set1.discard(20)
    set1.discard(21) 
    print("set1 after remove/discard    :   ",set1)


    # to clear all set use clear method 
    set1.clear() 
    
    set2 = {100,90,80,70,60,40,30} 
    print("set2     :   ",set2)

if __name__ == "__main__" : 
    main() 