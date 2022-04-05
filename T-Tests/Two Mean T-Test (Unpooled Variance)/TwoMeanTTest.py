# File Name: TwoMeanTTest.py
# Author: Verginia Mae Dole
# Date Created: 4/1/2022

from scipy.stats import t
import math

print("Two Mean T-Test (Unpooled Variance)")
print("")
print("x- = first sample mean")
print("sx = first sample std dev")
print("nx = first sample size")
print("y- = second sample mean")
print("sy = second sample std dev")
print("ny = second sample size")
print("")

mean1 = float(input("Enter x-: "))

std_dev1 = float(input("Enter sx: "))
while std_dev1 <= 0.0:
    std_dev1 = float(input("Enter sx: "))
    
n1 = int(input("Enter nx: "))
while n1 <= 0:
    n1 = int(input("Enter nx: "))
    
mean2 = float(input("Enter y-: "))

std_dev2 = float(input("Enter sy: "))
while std_dev2 <= 0.0:
    std_dev2 = float(input("Enter sy: "))
    
n2 = int(input("Enter ny: "))
while n2 <= 0:
    n2 = int(input("Enter ny: "))
print("")

df_top = pow((pow(std_dev1, 2) / n1) + (pow(std_dev2, 2) / n2), 2)
df_bottom = (pow(pow(std_dev1, 2)/ n1, 2) / (n1 - 1)) + (pow(pow(std_dev2, 2)/ n2, 2) / (n2 - 1))
df = df_top / df_bottom
std_err = math.sqrt((pow(std_dev1, 2) / n1) + (pow(std_dev2, 2) / n2))
T = (mean1 - mean2) / std_err

if T <= 0.0:
    pval1 = 2.0 * t.cdf(T, df)
else:
    pval1 = 2.0 * t.cdf(-T, df)
pval2 = t.cdf(T, df)
pval3 = 1.0 - t.cdf(T, df)

print("Test Statistic and Degrees of Freedom")
print("t = " + str(T))
print("df = " + str(df))
print("")

print("Two-Sided Test")
print("H0: \u03BCx == \u03BCy")
print("HA: \u03BCx =/= \u03BCy")
print("p = " + str(pval1))
print("")

print("Left-Sided Test")
print("H0: \u03BCx >= \u03BCy")
print("HA: \u03BCx < \u03BCy")
print("p = " + str(pval2))
print("")

print("Right-Sided Test")
print("H0: \u03BCx <= \u03BCy")
print("HA: \u03BCx > \u03BCy")
print("p = " + str(pval3))
