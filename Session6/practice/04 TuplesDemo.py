# Demo for Tuple in Python

def main() :
    # tuples in python are similar to list in terms of accessing (indexing)
    # main difference is tuples are immutable 
    #                    list are mutable 


    # creating empty tuples 
    empty_tuples = () 
    print("Empty tuples is      :   {}".format(empty_tuples))

    # creating non empty tuples 
    tup = (10,20,30,"jaydeep",10) 
    print("values in tup are    :   {}".format(tup))

    for ele in tup : 
        print("Value in tup is      {}".format(ele))
    print("Print tup element by for loop")
    for i in range(0,len(tup)) : 
        print("Vlaue at tup[ {} ]       :   {}".format(i,tup[i]))

    # count frequesncy of given value in tuples 
    print("Count of objects in tuples is    {} ".format(tup.count(10)))

    # index method return index of given value 
    indx = tup.index(10)
    print("index of 10 in tup is    {}".format(indx))
    print("        tup [ {} ]   :   {}".format(indx,tup[indx]))




if __name__ =="__main__" : 
    main() 