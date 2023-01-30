#  cs20b1129
#  Vishnu Abhay Parvatikar

import pandas as pd

df = pd.read_csv("diabetes.csv")


df = df.drop(columns="Type")


while True:
    print("1.Probability of Diabetes given age")
    print("2.Probability of Diabetes given Glucose+Blood Pressure+Skin Thickness + Insulin + BMI Levels")
    print("3.Exit")
    opt = int(input("Enter your choice : "))
    if opt == 1:
        print("Probability of Diabetes in the complete dataset : ")
        total_count = 0
        count = 0
        for index, row in df.iterrows():
            if row["Outcome"] == 1:
                count += 1
                total_count += 1
            elif row["Outcome"] == 0:
                total_count += 1
        probability = count/total_count
        print(f"Probability of Diabetes in entire dataset = {probability}\n")
        print("a.Age Above 50")
        print("b.Age between 40 and 50")
        print("c.Age between 30 and 40")
        print("d.Age less than 30")
        print("e.Exit")
        while True:
            choice = (input("Enter your choice : "))
            if choice == 'a':
                count = 0
                total_count = 0
                for index, row in df.iterrows():
                    if row["Age"] > 50:
                        total_count += 1
                        if row["Outcome"] == 1:
                            count += 1

                probability = count/total_count
                print(
                    f"Probability of Diabetes in Age above 50 = {probability}\n")

            elif choice == 'b':
                count = 0
                total_count = 0
                for index, row in df.iterrows():
                    if row["Age"] <= 50 and row["Age"] > 40:
                        total_count += 1
                        if row["Outcome"] == 1:
                            count += 1

                probability = count/total_count
                print(
                    f"Probability of Diabetes in Age between 40 and 50 = {probability}\n")

            elif choice == 'c':
                count = 0
                total_count = 0
                for index, row in df.iterrows():
                    if row["Age"] <= 40 and row["Age"] > 30:
                        total_count += 1
                        if row["Outcome"] == 1:
                            count += 1

                probability = count/total_count
                print(
                    f"Probability of Diabetes in Age between 30 and 40 = {probability}\n")
            elif choice == 'd':
                count = 0
                total_count = 0
                for index, row in df.iterrows():
                    if row["Age"] < 30:
                        total_count += 1
                        if row["Outcome"] == 1:
                            count += 1

                probability = count/total_count
                print(
                    f"Probability of Diabetes in Age less than 30 = {probability}\n")
            elif choice == 'e':
                print("\n\n")
                break
        else:
            print("Invalid Choice,Try Again\n")
    elif opt == 2:

        total_count = 0
        count = 0

        for index, row in df.iterrows():
            if row["Glucose"] > 120 and row["BloodPressure"] > 90 and row["SkinThickness"] > 30 and row["Insulin"] > 150 and row["BMI"] > 25:
                total_count += 1
                if row["Outcome"] == 1:
                    count += 1
        print("Probability of diabetes using given condition LEVELS : ")
        probability = count/total_count
        print(probability)
        print("\n\n")
    elif opt == 3:
        exit()
    else:
        print("Invalid Choice,Try Again\n")
