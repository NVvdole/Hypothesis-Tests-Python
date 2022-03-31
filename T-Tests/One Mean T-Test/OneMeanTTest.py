# File Name: OneMeanTTest.py
# Author: Verginia Mae Dole
# Date Created: 4/1/2022

from scipy.stats import t
import math

print("One Mean T-Test")
print("")
print("\u03BCx0 = hypothesized population mean")
print("x- = sample mean")
print("sx = sample std dev")
print("nx = sample size")
print("")

mu = float(input("Enter \u03BCx0: "))

mean = float(input("Enter x-: "))

std_dev = float(input("Enter sx: "))
while std_dev <= 0.0:
    std_dev = float(input("Enter sx: "))
    
n = int(input("Enter nx: "))
while n <= 0:
    n = int(input("Enter nx: "))
print("")

std_err = std_dev / math.sqrt(n)
df = n - 1
T = (mean - mu) / std_err

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
print("H0: \u03BCx == " + str(mu))
print("HA: \u03BCx =/= " + str(mu))
print("p = " + str(pval1))
print("")

print("Left-Sided Test")
print("H0: \u03BCx >= " + str(mu))
print("HA: \u03BCx < " + str(mu))
print("p = " + str(pval2))
print("")

print("Right-Sided Test")
print("H0: \u03BCx <= " + str(mu))
print("HA: \u03BCx > " + str(mu))
print("p = " + str(pval3))
