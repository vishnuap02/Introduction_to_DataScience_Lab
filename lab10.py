# Write a python program (with pandas) to read the given data and display the following:

# 1. Mean, median, mode, minimum, maximum, and standard deviation for all the attributes excluding the attribute ‘Outcome’. Find the value of the correlation coefficient for ‘Age’ with all other attributes (excluding ‘Outcome’), and ‘BMI’ with all other attributes (excluding ‘Outcome’). Then, obtain the scatter plot between

#             a. ‘Age’ and each of the other attributes, excluding ‘Outcome’

#             b. ‘BMI’ and each of the other attributes, excluding ‘Outcome’ (You can use matplotlib library).

# 2. Plot the histogram for the attributes ‘Pregnancies’ and ‘SkinThickness’ (You may use “hist” function from pandas). Plot the histogram of attribute ‘Pregnancies’ and for each of the 2 Outcomes individually (Use “groupby” function to group the tuples according to their “Outcome”). Obtain the boxplot for all the attributes excluding ‘Outcome’ (Use “boxplot” function).


import pandas as pd
import numpy as np
import scipy as sp
import matplotlib as plt
# from sklearn.model_selection import train_test_split

diabetes = pd.read_csv('E:\Downloads\diabetes.csv')

# X_train, X_test, y_train, y_test = train_test_split(
#     diabetes.loc[:, diabetes.columns != 'Outcome'], diabetes['Outcome'], stratify=diabetes['Outcome'], random_state=66)

diab_attr = diabetes.columns.to_list()
for attr in diab_attr:
    attribute = np.array(diabetes[attr].to_list())
    attr_mean = np.mean(attribute)
    attr_mode = sp.stats.mode(attribute)
    attr_median = np.median(attribute)
    attr_std = np.std(attribute)
    attr_max = np.max(attribute)
    attr_min = np.min(attribute)
    print(attribute, " Mean is : ", attr_mean)
    print(attribute, " Mode is : ", attr_mode)
    print(attribute, " Median is : ", attr_median)
    print(attribute, " STD is : ", attr_std)
    print(attribute, " maximum is : ", attr_max)
    print(attribute, " minimum is : ", attr_min)


pearcoeff = np.corrcoef(agelist, preglist)
print("\nThe correlation coefficient of Age with Pregnancies", pearcoeff[0][1])
pearcoeff = np.corrcoef(agelist, gluclist)
print("\nThe correlation coefficient of Age with Glucose", pearcoeff[0][1])
pearcoeff = np.corrcoef(agelist, bplist)
print("\nThe correlation coefficient of Age with Blood Pressure",
      pearcoeff[0][1])
pearcoeff = np.corrcoef(agelist, stlist)
print("\nThe correlation coefficient of Age with Skin Thickness",
      pearcoeff[0][1])
pearcoeff = np.corrcoef(agelist, inslist)
print("\nThe correlation coefficient of Age with Insulin", pearcoeff[0][1])
pearcoeff = np.corrcoef(agelist, BMIlist)
print("\nThe correlation coefficient of Age with BMI", pearcoeff[0][1])
pearcoeff = np.corrcoef(agelist, DPFlist)
print("\nThe correlation coefficient of Age with DiabetesPedigreeFunction",
      pearcoeff[0][1])


pearcoeff = np.corrcoef(BMIlist, preglist)
print("\nThe correlation coefficient BMI with Pregnancies", pearcoeff[0][1])
pearcoeff = np.corrcoef(BMIlist, gluclist)
print("\nThe correlation coefficient BMI with Glucose", pearcoeff[0][1])
pearcoeff = np.corrcoef(BMIlist, bplist)
print("\nThe correlation coefficient BMI with Blood Pressure", pearcoeff[0][1])
pearcoeff = np.corrcoef(BMIlist, stlist)
print("\nThe correlation coefficient BMI with Skin Thickness", pearcoeff[0][1])
pearcoeff = np.corrcoef(BMIlist, inslist)
print("\nThe correlation coefficient BMI with Insulin", pearcoeff[0][1])
pearcoeff = np.corrcoef(BMIlist, DPFlist)
print("\nThe correlation coefficient BMI with DiabetesPedigreeFunction",
      pearcoeff[0][1])
pearcoeff = np.corrcoef(BMIlist, agelist)
print("\nThe correlation coefficient BMI with Age", pearcoeff[0][1])


plt.scatter(agelist, preglist)
plt.show()
plt.scatter(agelist, gluclist)
plt.show()
plt.scatter(agelist, bplist)
plt.show()
plt.scatter(agelist, stlist)
plt.show()
plt.scatter(agelist, inslist)
plt.show()
plt.scatter(agelist, BMIlist)
plt.show()
plt.scatter(agelist, DPFlist)
plt.show()

plt.scatter(BMIlist, preglist)
plt.show()
plt.scatter(BMIlist, gluclist)
plt.show()
plt.scatter(BMIlist, bplist)
plt.show()
plt.scatter(BMIlist, stlist)
plt.show()
plt.scatter(BMIlist, inslist)
plt.show()
plt.scatter(BMIlist, DPFlist)
plt.show()
plt.scatter(BMIlist, agelist)
plt.show()


df.hist(column='Pregnancies')
plt.show()
df.hist(column='SkinThickness')
plt.show()
df.groupby('Outcome').hist(column='Pregnancies')
plt.show()
df.boxplot(column='Pregnancies')
plt.show()
df.boxplot(column='Glucose')
plt.show()
df.boxplot(column='BloodPressure')
plt.show()
df.boxplot(column='SkinThickness')
plt.show()
df.boxplot(column='Insulin')
plt.show()
df.boxplot(column='BMI')
plt.show()
df.boxplot(column='DiabetesPedigreeFunction')
plt.show()
df.boxplot(column='Age')
plt.show()
