# Here i declared a empty list which stores sets , and operation between sets is done based on index.
listofSets = []
# index is declared to keep point to latest set being added
index = 0
while(1):
    ch = int(input("Enter Choice 1)Create Empty Set ,2)Insert ,3)Delete ,4)Search ,5)Print ,6)Union ,7)Intersection ,8)Set Difference ,9)Symmetric Difference,10)Exit"))
    if (ch==1):
        a = set()
        listofSets.append(a)
        print("Set is created and added at Index : ",index," of list ")
        index+=1

    elif (ch==2):
        ind = int(input("Enter Index number of Set in which data to be inserted : "))
        if ind<index:
            val = input("Enter Value to be Inserted : ")
            a = listofSets[ind]
            a.add(val)
            listofSets[ind] = a
            print(listofSets[ind])
        else:
            print("List Index Out of range : ")
    elif (ch == 3):
        ind = int(input("Enter Index number of Set in which data to be Deleted : "))
        if ind<index:
            val = input("Enter Value to be Deleted : ")
            a = listofSets[ind]
            a.remove(val)
            listofSets[ind] = a
            print(listofSets[ind])
        else:
            print("List Index Out of range : ")



    elif (ch==4):
        ind = int(input("Enter Index number of Set in which data to be Searched : "))
        if ind<index:
            val = input("Enter Value to be Searched : ")
            a = listofSets[ind]
            if val in a:
                print(val," is found in set ")
            else:
                print("Not Found")
        else:
            print("List Index Out of range : ")
    elif (ch == 5):
        ind = int(input("Enter Index number of Set to be printed : "))
        if ind<index:
            print(listofSets[ind])
        else:
            print("List Index Out of range : ")
    elif (ch==6):
        ind1 = int(input("Enter Index number of Set 1 for Union of Sets : "))
        ind2 = int(input("Enter Index number of Set 2 for Union of Sets : "))

        if ind1 < index and ind2 < index:
            a = listofSets[ind1]
            b = listofSets[ind2]
            c = a.union(b)
            # can be also a|b
            print(c)
        else:
            print("List Index Out of range : ")
    elif (ch == 7):
        ind1 = int(input("Enter Index number of Set 1 for Intersection of Sets : "))
        ind2 = int(input("Enter Index number of Set 2 for Intersection of Sets : "))

        if ind1 < index and ind2 < index:
            a = listofSets[ind1]
            b = listofSets[ind2]
            c = a.intersection(b)
            # can be also a&b
            print(c)
        else:
            print("List Index Out of range : ")
    elif (ch==8):
        ind1 = int(input("Enter Index number of Set 1 for Set Difference : "))
        ind2 = int(input("Enter Index number of Set 2 for Set Difference : "))

        if ind1 < index and ind2 < index:
            a = listofSets[ind1]
            b = listofSets[ind2]
            c = a-b
            print(c)
        else:
            print("List Index Out of range : ")
    elif (ch == 9):
        ind1 = int(input("Enter Index number of Set 1 for Symmetric Difference : "))
        ind2 = int(input("Enter Index number of Set 2 for Symmetric Difference : "))

        if ind1 < index and ind2 < index:
            a = listofSets[ind1]
            b = listofSets[ind2]
            c = a.symmetric_difference(b)
            print(c)
        else:
            print("List Index Out of range : ")

    elif (ch==10):
        print("Exit")
        break
    else:
        print("Invalid Choice")
