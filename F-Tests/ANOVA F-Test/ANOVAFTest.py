# File Name: ANOVAFTest.py
# Author: Verginia Mae Dole
# Date Created: 4/1/2022

from scipy.stats import f
import statistics

print("One-Way ANOVA F-Test")
print("")
print("nx = number of cells per Category")
print("x1 = Category 1 values")
print("x2 = Category 2 values")
print("x3 = Category 3 values")
print("")

nx = int(input("Enter nx: "))
while nx <= 0:
    nx = int(input("Enter nx: "))
n = nx * 3

x1 = []
for i in range(nx):
    temp = float(input("Enter x" + str(i + 1) + "1: "))
    while temp <= 0.0:
        temp = float(input("Enter x" + str(i + 1) + "1: "))
    x1.append(temp)

x2 = []
for i in range(nx):
    temp = float(input("Enter x" + str(i + 1) + "2: "))
    while temp <= 0.0:
        temp = float(input("Enter x" + str(i + 1) + "2: "))
    x2.append(temp)

x3 = []
for i in range(nx):
    temp = float(input("Enter x" + str(i + 1) + "3: "))
    while temp <= 0.0:
        temp = float(input("Enter x" + str(i + 1) + "3: "))
    x3.append(temp)
print("")

mean1 = statistics.mean(x1)
mean2 = statistics.mean(x2)
mean3 = statistics.mean(x3)
gmean = (mean1 + mean2 + mean3) / 3.0

SSR1 = nx * pow(mean1 - gmean, 2)
SSR2 = nx * pow(mean2 - gmean, 2)
SSR3 = nx * pow(mean3 - gmean, 2)
SSR = SSR1 + SSR2 + SSR3

SSE1 = 0.0
for i in range(nx):
    SSE1 += pow(x1[i] - mean1, 2)
SSE2 = 0.0
for i in range(nx):
    SSE2 += pow(x2[i] - mean2, 2)
SSE3 = 0.0
for i in range(nx):
    SSE3 += pow(x3[i] - mean3, 2)
SSE = SSE1 + SSE2 + SSE3

df1 = 2
df2 = n - 3
MSR = SSR / df1
MSE = SSE / df2
F = MSR / MSE
pval = 1.0 - f.cdf(F, df1, df2)

print("Hypotheses")
print("H0: \u03BC1 == \u03BC2 == \u03BC3")
print("HA: \u03BC1 =/= \u03BC2 =/= \u03BC3")
print("")

print("Test Statistic and P-Value")
print("F = " + str(F))
print("p = " + str(pval))
print("")

print("Factor")
print("df = " + str(df1))
print("SS = " + str(SSR))
print("MS = " + str(MSR))
print("")

print("Error")
print("df = " + str(df2))
print("SS = " + str(SSE))
print("MS = " + str(MSE))
