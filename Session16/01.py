# array in Python 
from array import array

def main() : 
    arr = array('i',[11,21,151,51,101,11])

    print(type(arr))
    print("Length of array  : ",len(arr))
    print("Actual array is : ",arr)

    # print("Arr[ 0 ] : ",arr[0])

    for i in range(len(arr)) : 
        print(f"Arr[ {i} ] : {arr[i]}")

    
    for num in arr : 
        print(num)

if __name__ == "__main__" : 
    main()

