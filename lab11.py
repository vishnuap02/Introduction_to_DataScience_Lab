# 1. Write a Python program (with pandas) to do the following on the data file “landslide_data3_miss.csv”.
#    a) Plot a graph of the attribute names (x-axis) with the number of missing values in them (y-axis). (separate python file)
#    b) Target attribute is “stationid”, Drop the tuples (rows) having missing values in the target attribute. Print the total number of tuples deleted. Delete (drop) the tuples (rows) having equal to or more than one third of attributes with missing values. Print the total number of tuples deleted.
#    c) After (b), count and print the number of missing values in each attributes. Also find and print the total number of missing values in the file (after the deletion of tuples).
# 2. Experiments on filling in missing values:
#    a) Replace the missing values by mean of their respective attribute. (Use df.fillna() with suitable arguments.)
#       Compute the mean, median, mode and standard deviation for each attributes and compare the same with that of the original file.
#       Calculate the root mean square error (RMSE) between the original and replaced values for each attribute. (Get original values from original file provided). Compute RMSE given by the equation at the end of the question. Plot these RMSE with respect to the attributes.
#    b) Replace the missing values in each attribute using the linear interpolation technique. Use df.interpolate() with suitable arguments.
#       Compute the mean, median, mode and standard deviation for each attributes and compare with that of the original file.
#       Calculate the root mean square error (RMSE) between the original and replaced values for each attributes. (Get original values from the original file provided). Compute RMSE given by the equation at the end of the question. Plot this RMSE with respect to the attributes.from statistics import mean
#    c) Outlier detection:
#       i) After replacing the missing values by interpolation method, find and list the outliers in the attributes “temperature” and “rain”.
#          Outliers are the values that do not satisfy the condition (Q1 – (1.5 * IQR)) < x < (Q3 + (1.5 * IQR)),
#          where x is the value of the attribute, IQR is the interquartile range, Q1 and Q3 are the first and third quartiles.
#          Obtain the boxplot for these attributes.
#      ii) Replace these outliers with the median of the attribute. Plot the boxplot again and observe the difference with that of the boxplot from the previous box in (i).
#          Do you still get outliers? Why?

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

missdf = pd.read_csv("landslide_data3_miss.csv")
# a) Plot a graph of the attribute names (x-axis) with the number of missing values in them (y-axis). (separate python file)

null_values = missdf.isnull().sum()
null_values.plot(kind='bar')
plt.savefig('missing_values.png')
plt.close()

# b) Target attribute is “stationid”, Drop the tuples (rows) having missing values in the target attribute.
#    Print the total number of tuples deleted. Delete (drop) the tuples (rows) having equal to or more than one third of attributes with missing values.
#    Print the total number of tuples deleted.


# Drop the tuples (rows) having missing values in the target attribute.
print("Before dropping missing values in target attribute: ", df.shape)
df = df.dropna(subset=['stationid'])
print("After dropping missing values in target attribute: ", df.shape, "\n")

# Delete (drop) the tuples (rows) having equal to or more than one third of attributes with missing values.
print("Before dropping tuples having equal to or more than one third of attributes with missing values: ", df.shape)
df = df.dropna(thresh=int(df.shape[1] * 2 / 3))
print("After dropping tuples having equal to or more than one third of attributes with missing values: ", df.shape, "\n")

# c) After (b), count and print the number of missing values in each attributes.
#    Also find and print the total number of missing values in the file (after the deletion of tuples).

missing_values = df.isnull().sum()
print("Missing values in each attributes: ")
print(missing_values)
print("\nTotal number of missing values in the file: ", missing_values.sum())

df_original = pd.read_csv("landslide_data3_original.csv")
df_O = pd.DataFrame()
df_O['mean'] = df_original.mean(numeric_only=True)
df_O['median'] = df_original.median(numeric_only=True)
df_O['mode'] = df_original.mode(numeric_only=True).iloc[0]
df_O['std'] = df_original.std(numeric_only=True)

# a) Replace the missing values by mean of their respective attribute. (Use df.fillna() with suitable arguments.)
df = df.fillna(df.mean(numeric_only=True))
print("\nAfter replacing missing values by mean of their respective attribute: ")

# Compute the mean, median, mode and standard deviation for each attributes and compare the same with that of the original file.
#   Calculate the root mean square error (RMSE) between the original and replaced values for each attribute.
#   (Get original values from original file provided). Compute RMSE given by the equation at the end of the question.

df_R = pd.DataFrame()
df_D = pd.DataFrame()

print("\t\t\tOriginal")
print("-----------------------------------------------------------")
print(df_O)
print("\t\t\tReplaced")
print("-----------------------------------------------------------")
df_R['mean'] = df.mean(numeric_only=True)
df_R['median'] = df.median(numeric_only=True)
df_R['mode'] = df.mode(numeric_only=True).iloc[0]
df_R['std'] = df.std(numeric_only=True)
print(df_R)

print("\t\t\tDifference")
print("-----------------------------------------------------------")
df_D['mean'] = df_O['mean'] - df_R['mean']
df_D['median'] = df_O['median'] - df_R['median']
df_D['mode'] = df_O['mode'] - df_R['mode']
df_D['std'] = df_O['std'] - df_R['std']
print(df_D)

print("\nRMSE: ")
print(((df_original.select_dtypes(include='number') -
        df.select_dtypes(include='number')) ** 2).mean(numeric_only=True) ** 0.5)
#   Plot these RMSE with respect to the attributes.
rmse = ((df_original.select_dtypes(include='number') -
         df.select_dtypes(include='number')) ** 2).mean(numeric_only=True) ** 0.5
rmse.plot(kind='bar')
plt.savefig('rmse_mean.png')
plt.close()

# b) Replace the missing values in each attribute using the linear interpolation technique. Use df.interpolate() with suitable arguments.
df = df.interpolate(numeric_only=True)
print("\nAfter replacing missing values in each attribute using the linear interpolation technique: ")

# Compute the mean, median, mode and standard deviation for each attributes and compare with that of the original file.
#   Calculate the root mean square error (RMSE) between the original and replaced values for each attributes.
#   (Get original values from the original file provided). Compute RMSE given by the equation at the end of the question.
df_R = pd.DataFrame()
df_D = pd.DataFrame()

print("\t\t\tOriginal")
print("-----------------------------------------------------------")
print(df_O)

print("\t\t\tReplaced")
print("-----------------------------------------------------------")
df_R['mean'] = df.mean(numeric_only=True)
df_R['median'] = df.median(numeric_only=True)
df_R['mode'] = df.mode(numeric_only=True).iloc[0]
df_R['std'] = df.std(numeric_only=True)
print(df_R)

print("\t\t\tDifference")
print("-----------------------------------------------------------")
df_D['mean'] = df_O['mean'] - df_R['mean']
df_D['median'] = df_O['median'] - df_R['median']
df_D['mode'] = df_O['mode'] - df_R['mode']
df_D['std'] = df_O['std'] - df_R['std']
print(df_D)

print("\nRMSE: ")
print(((df_original.select_dtypes(include='number') -
        df.select_dtypes(include='number')) ** 2).mean(numeric_only=True) ** 0.5)
