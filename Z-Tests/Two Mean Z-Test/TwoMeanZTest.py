# File Name: TwoMeanZTest.py
# Author: Verginia Mae Dole
# Date Created: 4/1/2022

from scipy.stats import norm
import math

print("Two Mean Z-Test")
print("")
print("\u03C3x = first population std dev")
print("\u03C3y = second population std dev")
print("x- = first sample mean")
print("nx = first sample size")
print("y- = second sample mean")
print("ny = second sample size")
print("")
    
sig1 = float(input("Enter \u03C3x: "))
while sig1 <= 0.0:
    sig1 = float(input("Enter \u03C3x: "))
    
sig2 = float(input("Enter \u03C3y: "))
while sig2 <= 0.0:
    sig2 = float(input("Enter \u03C3y: "))
    
mean1 = float(input("Enter x-: "))
    
n1 = int(input("Enter nx: "))
while n1 <= 0:
    n1 = int(input("Enter nx: "))
    
mean2 = float(input("Enter y-: "))
    
n2 = int(input("Enter ny: "))
while n2 <= 0:
    n2 = int(input("Enter ny: "))
print("")

std_err = math.sqrt((pow(sig1, 2) / n1) + (pow(sig2, 2) / n2))
Z = (mean1 - mean2) / std_err

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
