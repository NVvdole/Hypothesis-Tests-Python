# File Name: OneProportionZTest.py
# Author: Verginia Mae Dole
# Date Created: 4/1/2022

from scipy.stats import norm
import math

print("One Proportion Z-Test")
print("")
print("px0 = hypothesized population proportion")
print("x = sample successes")
print("nx = sample size")
print("")

p0 = float(input("Enter px0: "))
while p0 <= 0.0 or p0 >= 1.0:
    p0 = float(input("Enter px0: "))
    
x = int(input("Enter x: "))
while x <= 0:
    x = int(input("Enter x: "))
    
n = int(input("Enter nx: "))
while n <= x:
    n = int(input("Enter nx: "))
print("")

p = float(x) / n
std_err = math.sqrt((p0 * (1.0 - p0)) / n)
Z = (p - p0) / std_err

if Z <= 0.0:
    pval1 = 2.0 * norm.cdf(Z)
else:
    pval1 = 2.0 * norm.cdf(-Z)
pval2 = norm.cdf(Z)
pval3 = 1.0 - norm.cdf(Z)

print("Proportion")
print("px^ = " + str(p))
print("")

print("Test Statistic")
print("z = " + str(Z))
print("")

print("Two-Sided Test")
print("H0: px == " + str(p0))
print("HA: px =/= " + str(p0))
print("p = " + str(pval1))
print("")

print("Left-Sided Test")
print("H0: px >= " + str(p0))
print("HA: px < " + str(p0))
print("p = " + str(pval2))
print("")

print("Right-Sided Test")
print("H0: px <= " + str(p0))
print("HA: px > " + str(p0))
print("p = " + str(pval3))
