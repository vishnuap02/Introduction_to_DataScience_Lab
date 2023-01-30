import pandas as pd

names = ["Ram", "Sam", "Prabahu"]
ac_nos = ['9893893891', '9893893898', '9893893871']
ac_types = ['SB', 'CA', 'SB']
adhar_no = ['959389389173', '959389389179', '959389389159']
balance = [8989839, 7690990, 989330]
d = {"Name": names, "AccountNo": ac_nos, "AccountType": ac_types,
     "AadharNo": adhar_no, "balance": balance}

df1 = pd.DataFrame(d)
# print(df1)

# converting to csv type
df1.to_csv("SBIAccountHolder.csv")

while 1:
    ch = int(input(
        "Enter choice 1)Append row 2)Delete row 3)Credit 4)Debit 5)Account Details 6)Exit :"))
    if ch == 1:
        print("Enter data to append : ")
        name = input("Name:")
        acno = input("AccountNo:")
        acty = input("AccountType:")
        adno = input("Aadhaar Number:")
        bal = input("Balance:")
        names.append(name)
        ac_nos.append(acno)
        ac_types.append(acty)
        adhar_no.append(adno)
        balance.append(bal)
        d = {"Name": names, "AccountNo": ac_nos, "AccountType": ac_types,
             "AadharNo": adhar_no, "balance": balance}
        df1 = pd.DataFrame(d)
        df1['supporter'][0] = 'Vishnu'
        df1.to_csv("SBIAccountHolder.csv")
        # df1.append(df2)
        print(df1)
    elif ch == 2:
        acno = input("enter account number to delete record:")
        # x = df1.loc[df1['AccountNo'] == acno, 'Name'].iloc[0]
        # df1.drop(int(x), inplace=True)
        print(df1)
        df_index = df1.set_index('AccountNo')

        df_index = df_index.drop(1)
        df1 = df_index
        print(df_index)
        df_index.to_csv("SBIAccountHolder.csv")

    elif ch == 3:
        acno = input("enter account number to credit:")
        amt = int(input("ENter amount to credit :"))
        df1.loc[df1['AccountNo'] == acno,
                'balance'] = df1.loc[df1['AccountNo'] == acno, 'balance'] + amt
        # x = x+amt
        print(df1)
        df1.to_csv("SBIAccountHolder.csv")
    elif ch == 4:
        acno = input("enter account number to Debit:")
        amt = int(input("ENter amount to Debit :"))
        if (df1.loc[df1['AccountNo'] == acno, 'AccountType'].iloc[0] == 'SB'):
            if ((df1.loc[df1['AccountNo'] == acno, 'balance']).tolist())[0] < amt:
                print("Insuffient Balance!")
                continue
        df1.loc[df1['AccountNo'] == acno,
                'balance'] = df1.loc[df1['AccountNo'] == acno, 'balance'] - amt
        # x = x+amt
        print(df1)
        df1.to_csv("SBIAccountHolder.csv")
    elif ch == 5:
        print(df1)

    elif ch == 6:
        print("Exiting!")
        break
    else:
        print("Enter valid choice!")

print("Creating another CSV file!")
contactNo = ["9840787333", "9840787343", "9840787353"]
dob = ['12-2-1990', '12-2-2000', '12-2-2010']
address = ["no 23 Kandigai,Chennai 127",
           "no 73,Melakottaiyur ,Chennai 127", "No 43, Anna Nagar"]
d2 = {"Name": names, "AadharNo": adhar_no,
      "Contact_No": contactNo, "DOB": dob, "Address": address}
df2 = pd.DataFrame(d2)
df2.to_csv("AdhaarDB.csv")
df3 = pd.merge(df1, df2)
df3.to_csv("final.csv")
print(df3)
