import pickle
# fil = open("file.dat", "wb")
# fil.close()


while(1):
    print("MENU: 1:ENTER DATA\t2:READFILE\t3:SEARCH BOOK\t0=EXIT")
    c = int(input())
    if c == 1:
        print("ENTER NUMBER OF BOOKS: \n")
        n = int(input())

        for i in range(n):
            fil = open("file.dat", "ab")
            print("Enter ISSN:")
            issn = int(input())
            print("Enter Title:")
            title = input()
            print("Enter Price:")
            price = input()
            print("Enter Edition:")
            ed = input()
            print("Enter Year:")
            yr = input()
            print("Enter Author Name:")
            athname = input()

            libr = [title, price, ed, yr, athname]
            pickle.dump(libr, fil)
            fil.close()
    elif c == 2:
        fil = open("file.dat", "rb")
        while True:
            try:
                libr = pickle.load(fil)
                print(libr)
            except EOFError:
                break
    elif c == 3:
        print("ENTER TITLE: \n")
        s = input()
        fil = open("file.dat", "rb")
        while True:
            try:
                libr = pickle.load(fil)
                if libr[0] == s:
                    print("THE BOOK IS PRESENT\n")
                    break
            except EOFError:
                print("THE BOOK IS NOT PRESENT")
                break
    elif c == 0:
        print("EXITING !")
        break
    else:
        print("INVALID CHOICE")
