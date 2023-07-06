class sArray:
    def main():
        arr_1=[]
        n=int(input("Enter the number of array elements"))
        for x in range(0,n):
            y=int(input("enter the arry element"))
            arr_1.append(y)
        
        print("final Array",arr_1," ",type(arr_1))
        print("Length of the arry is ",len(arr_1))