print("--------------Student Details------------")
dict={}
while(1):
    choice = int(input("Enter 1- Insert , 2-Delete , 3-Search , 4-exit : "))
    if(choice==1):
        stud = {}
        rno = input("Enter your Roll number : ")
        name = input("Enter your Name : ")
        cgpa = input("Enter your CGPA : ")
        mobno = input("Enter your Mobile number : ")
        stud["Name"]=name
        stud["cgpa"]=cgpa
        stud["Mobile_no"]=mobno
        dict[rno]=stud


    elif (choice == 2):
        rno = input("Enter Roll number to delete : ")
        if rno in dict:
            dict.pop(rno)
            print("The current dictionary after deleting roll number ,",rno," is : ")
            print(dict)
        else:
            print("Invalid Roll number.")
    elif (choice == 3):
        rno = input("Enter Roll number to Search : ")
        if rno in dict:
            intdict=dict[rno]
            print("The Details of Student with roll number ,", rno, " :  ")
            print("Name : ",intdict["Name"]," || CGPA : ",intdict["cgpa"]," || Mobile Number : ",intdict["Mobile_no"])
        else:
            print("Invalid Roll number.")

    elif (choice == 4):
        break

    else:
        print("Invalid choice!!")


print(dict)
