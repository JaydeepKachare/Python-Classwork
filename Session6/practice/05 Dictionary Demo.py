# Demo for dictionary (key-value) Collection in dictionary

def main() :
    # create empty dictonary 
    Dict = {} 
    print("Empty dictionary     :   {}".format(Dict))
    
    # create dictionary with values 
    dict1 = {101:"Jayeep" , 102:"Kishor" , 105:"Rohan"}
    print("dict1 :  {}".format(dict1))

    # creation of dictionary by keyword 
    dict2 = dict({101:"Jayeep" , 102:"Kishor" , 105:"Rohan"})
    print("Dictionary creation using keyword    :   {}".format(dict2))

    # addition of key-value in dictionary
    # if key-value exist ----> get updated
    # if key-value doesnot exist -------> new key-value get created
    dict2[113] = "Nilesh"
    print("Added value in dict2                    ",dict2)

    # Accessing value from dictionary 
    # value = dict [ key ] -------> this will give value 
    print("value at key 102 is  :   ",dict2[102])

    # if value does not exists it will give Error 
    # print("value at key 199 is  :   ",dict2[119])


    # deleting value from dictionary
    print("dict2    :   ",dict2)
    del dict2[113]
    # If key values does not exists it will give Error 
    print("dict2    :   ",dict2)

    # All items in dictionary can be deleted using clear 
    dict2.clear() 

    # delete entire dictionary 
    del dict2

    print("\n")

    d1 = dict() 
    d1[101] =  "Jaydeep"
    d1[102] =  "Kishor"
    d1[103] =  "Rohan"
    d1[104] =  "Pradeep"
    d1[105] =  "Shubham"
    print("d1   :   {}".format(d1))

    print(d1.keys())        # return list of keys 
    print(d1.values())      # return list of values 

    print(d1.__str__())     # return printable version of dictionary

    print(d1.items())

    print("d1 has 101   :   ",101 in d1 )
    print("d1 has 119   :   ",119 in d1 )

    # Iteration over dictionary 
    for i in d1 :
        print("{}   :   {}".format(i,d1[i]))

if __name__ =="__main__" : 
    main() 