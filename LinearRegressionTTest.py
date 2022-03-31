# File Name: LinearRegressionTTest.py
# Author: Verginia Mae Dole
# Date Created: 4/1/2022

from scipy.stats import t
import math
import statistics

print("Linear Regression & Correlation T-Test")
print("")
print("n = sample size")
print("x = predictor data")
print("y = response data")
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

meanx = statistics.mean(x)
std_devx = math.sqrt(statistics.variance(x))
meany = statistics.mean(y)
std_devy = math.sqrt(statistics.variance(y))

cov = 0
for i in range(n):
    cov += (x[i] - meanx) * (y[i] - meany)
cov /= (n - 1)
r = cov / (std_devx * std_devy)

b1 = r * (std_devy / std_devx)
b0 = meany - (b1 * meanx)

df = n - 2
T = (r * math.sqrt(n - 2)) / math.sqrt(1.0 - pow(r, 2))

if T <= 0.0:
    pval1 = 2.0 * t.cdf(T, df)
else:
    pval1 = 2.0 * t.cdf(-T, df)
pval2 = t.cdf(T, df)
pval3 = 1.0 - t.cdf(T, df)

print("Linear Regression")
print("y = b0 + b1x")
print("b0 = " + str(b0))
print("b1 = " + str(b1))
print("r = " + str(r))
print("r^2 = " + str(pow(r, 2)))
print("")

print("Test Statistic and Degrees of Freedom")
print("t = " + str(T))
print("df = " + str(df))
print("")

print("Two-Sided Test")
print("H0: \u03B21 == 0 and \u03C1 == 0")
print("HA: \u03B21 =/= 0 and \u03C1 =/= 0")
print("p = " + str(pval1))
print("")

print("Left-Sided Test")
print("H0: \u03B21 >= 0 and \u03C1 >= 0")
print("HA: \u03B21 < 0 and \u03C1 < 0")
print("p = " + str(pval2))
print("")

print("Right-Sided Test")
print("H0: \u03B21 <= 0 and \u03C1 <= 0")
print("HA: \u03B21 > 0 and \u03C1 > 0")
print("p = " + str(pval3))
