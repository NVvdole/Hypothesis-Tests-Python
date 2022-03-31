# File Name: TwoProportionZTest.py
# Author: Verginia Mae Dole
# Date Created: 4/1/2022

from scipy.stats import norm
import math

print("Two Proportion Z-Test")
print("")
print("x = first sample successes")
print("nx = first sample size")
print("y = second sample successes")
print("ny = second sample size")
print("")

x = int(input("Enter x: "))
while x <= 0:
    x = int(input("Enter x: "))
    
n1 = int(input("Enter nx: "))
while n1 <= x:
    n1 = int(input("Enter nx: "))
    
y = int(input("Enter y: "))
while y <= 0:
    y = int(input("Enter y: "))
    
n2 = int(input("Enter ny: "))
while n2 <= y:
    n2 = int(input("Enter nx: "))
print("")

p1 = float(x) / n1
p2 = float(y) / n2
p = float(x + y) / (n1 + n2)
std_err = math.sqrt(p * (1.0 - p) * ((1.0 / n1) + (1.0 / n2)))
Z = (p1 - p2) / std_err

if Z <= 0.0:
    pval1 = 2.0 * norm.cdf(Z)
else:
    pval1 = 2.0 * norm.cdf(-Z)
pval2 = norm.cdf(Z)
pval3 = 1.0 - norm.cdf(Z)

print("Proportions")
print("px^ = " + str(p1))
print("py^ = " + str(p2))
print("p^ = " + str(p))
print("")

print("Test Statistic")
print("z = " + str(Z))
print("")

print("Two-Sided Test")
print("H0: px == py")
print("HA: px =/= py")
print("p = " + str(pval1))
print("")

print("Left-Sided Test")
print("H0: px >= py")
print("HA: px < py")
print("p = " + str(pval2))
print("")

print("Right-Sided Test")
print("H0: px <= py")
print("HA: px > py")
print("p = " + str(pval3))
