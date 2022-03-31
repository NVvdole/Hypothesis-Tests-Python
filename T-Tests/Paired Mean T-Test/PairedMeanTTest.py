# File Name: PairedMeanTTest.py
# Author: Verginia Mae Dole
# Date Created: 4/1/2022

from scipy.stats import t
import math
import statistics

print("Paired Mean T-Test")
print("")
print("n = sample size")
print("x = first sample")
print("y = second sample")
print("")

n = int(input("Enter n: "))
while n <= 0:
    n = int(input("Enter n: "))
    
x = []
for i in range(n):
    temp = float(input("Enter x" + str(i + 1) + ": "))
    while temp <= 0.0:
        temp = float(input("Enter x" + str(i + 1) + ": "))
    x.append(temp)
    
y = []
for i in range(n):
    temp = float(input("Enter y" + str(i + 1) + ": "))
    while temp <= 0.0:
        temp = float(input("Enter y" + str(i + 1) + ": "))
    y.append(temp)
print("")

d = []
for i in range(n):
    temp = x[i] - y[i]
    d.append(temp)
meand = statistics.mean(d)
std_devd = math.sqrt(statistics.variance(d))

std_err = std_devd / math.sqrt(n)
df = n - 1
T = meand / std_err

if T <= 0.0:
    pval1 = 2.0 * t.cdf(T, df)
else:
    pval1 = 2.0 * t.cdf(-T, df)
pval2 = t.cdf(T, df)
pval3 = 1.0 - t.cdf(T, df)

print("d = x - y")
print("d = " + str(d))
print("d- = " + str(meand))
print("sd = " + str(std_devd))
print("")

print("Test Statistic and Degrees of Freedom")
print("t = " + str(T))
print("df = " + str(df))
print("")

print("Two-Sided Test")
print("H0: \u03BCd == 0")
print("HA: \u03BCd =/= 0")
print("p = " + str(pval1))
print("")

print("Left-Sided Test")
print("H0: \u03BCd >= 0")
print("HA: \u03BCd < 0")
print("p = " + str(pval2))
print("")

print("Right-Sided Test")
print("H0: \u03BCd <= 0")
print("HA: \u03BCd > 0")
print("p = " + str(pval3))
