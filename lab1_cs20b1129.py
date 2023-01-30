# CS20B1129 Vishnu Abhay Parvatikar

i = 1
while(1):
    print("Enter '1' for INsertion sort , '2' for Binary search , 'Any Key' for exit .")
    i = int(input())
    if (i == 1):
        no = int(input("Enter number of elements for Insertion Sort: "))
        list2 = []

        for i in range(no):
            print("Enter ", (i+1), "th element : ")
            ele = int(input())
            list2.append(ele)
        print(list2)
        for i in range(1, no):

            ele = list2[i]
            j = i-1
            while (j >= 0 and ele < list2[j]):
                list2[j+1] = list2[j]
                j = j-1
            list2[j+1] = ele

        list3 = list2
        print("after Insertion Sorting : ", list3)
    elif (i == 2):
        # Binary Search
        no = int(input("Enter number of elements for Binary Search : "))
        list2 = []

        for i in range(no):
            print("Enter ", (i+1), "th element : ")
            ele = int(input())
            list2.append(ele)
        print(list2)
        for i in range(1, no):

            ele = list2[i]
            j = i-1
            while (j >= 0 and ele < list2[j]):
                list2[j+1] = list2[j]
                j = j-1
            list2[j+1] = ele

        list3 = list2
        print("after Sorting : ", list3)
        sele = int(input("Enter the search element : "))

        low = 0
        high = no-1
        found = False

        while(low <= high):
            mid = int((high + low)/2)

            if(sele < list3[mid]):
                high = mid-1
                print("mid and high are now ", mid, high)
            elif(sele > list3[mid]):
                low = mid+1
                print("mid and high are now ", mid, high)

            elif(sele == list3[mid]):
                found = True
                break

        if found:
            print("The element ", sele, " found at ", mid, " index")
        else:
            print(" Elemnt ", sele, " not found!!")
    else:
        print("Exited!!")
        break









































clas    
