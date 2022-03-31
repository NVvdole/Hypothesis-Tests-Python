# File Name: IndependenceChiSquareTest.py
# Author: Verginia Mae Dole
# Date Created: 4/1/2022

from scipy.stats import chi2

print("Independence Chi-Square Test")
print("")
print("r = number of rows")
print("c = number of columns")
print("O = observed values")
print("")

rows = int(input("Enter r: "))
while rows <= 0:
    rows = int(input("Enter r: "))

cols = int(input("Enter c: "))
while cols <= 0:
    cols = int(input("Enter c: "))
    
obs = []
for i in range(rows):
    arr = []
    for j in range(cols):
        temp = float(input("Enter O" + str(i + 1) + str(j + 1) + ": "))
        while temp <= 0.0:
            temp = float(input("Enter O" + str(i + 1) + str(j + 1) + ": "))
        arr.append(temp)
    obs.append(arr)
print("")

rowsum = []
for i in range(rows):
    temp = 0.0
    for j in range(cols):
        temp += obs[i][j]
    rowsum.append(temp)

colsum = []
for j in range(cols):
    temp = 0.0
    for i in range(rows):
        temp += obs[i][j]
    colsum.append(temp)
    
total = sum(rowsum)
exp = []
for i in range(rows):
    arr = []
    for j in range(cols):
        temp = (rowsum[i] * colsum[j]) / total
        arr.append(temp)
    exp.append(arr)
    
X2 = 0.0
for i in range(rows):
    for j in range(cols):
        X2 += pow(obs[i][j] - exp[i][j], 2) / exp[i][j]
df = (rows - 1) * (cols - 1)
pval = 1.0 - chi2.cdf(X2, df)

print("Expected")
print("E = " + str(exp))
print("")

print("Hypotheses")
print("H0: Independent")
print("HA: Not Independent")
print("")

print("Test Statistics and Degrees of Freedom")
print("X^2 = " + str(X2))
print("df = " + str(df))
print("")

print("P-Value")
print("p = " + str(pval))
