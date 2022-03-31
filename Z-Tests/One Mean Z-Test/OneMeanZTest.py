# File Name: OneMeanZTest.py
# Author: Verginia Mae Dole
# Date Created: 4/1/2022

from scipy.stats import norm
import math

print("One Mean Z-Test")
print("")
print("\u03BCx0 = hypothesized population mean")
print("\u03C3x = population std dev")
print("x- = sample mean")
print("nx = sample size")
print("")

mu = float(input("Enter \u03BCx0: "))

sig = float(input("Enter \u03C3x: "))
while sig <= 0.0:
    sig = float(input("Enter \u03C3x: "))
    
mean = float(input("Enter x-: "))
    
n = int(input("Enter nx: "))
while n <= 0:
    n = int(input("Enter nx: "))
print("")

std_err = sig / math.sqrt(n)
Z = (mean - mu) / std_err

if Z <= 0.0:
    pval1 = 2.0 * norm.cdf(Z)
else:
    pval1 = 2.0 * norm.cdf(-Z)
pval2 = norm.cdf(Z)
pval3 = 1.0 - norm.cdf(Z)
    
print("Test Statistic")
print("z = " + str(Z))
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
