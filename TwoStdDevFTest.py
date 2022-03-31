# File Name: TwoStdDevFTest.py
# Author: Verginia Mae Dole
# Date Created: 4/1/2022

from scipy.stats import f

print("Two Standard Deviation F-Test")
print("")
print("sx = first sample std dev")
print("nx = first sample size")
print("sy = second sample std dev")
print("ny = second sample size")
print("")

std_dev1 = float(input("Enter Sx: "))
while std_dev1 <= 0.0:
    std_dev1 = float(input("Enter Sx: "))
    
n1 = int(input("Enter nx: "))
while n1 <= 0:
    n1 = int(input("Enter nx: "))
    
std_dev2 = float(input("Enter Sy: "))
while std_dev2 <= 0.0:
    std_dev2 = float(input("Enter Sy: "))
    
n2 = int(input("Enter ny: "))
while n2 <= 0:
    n2 = int(input("Enter ny: "))
print("")

df1 = n1 - 1
df2 = n2 - 1
F = pow(std_dev1, 2) / pow(std_dev2, 2)

if F <= f.median(df1, df2):
    pval1 = 2.0 * f.cdf(F, df1, df2)
else:
    pval1 = 2.0 * (1.0 - f.cdf(F, df1, df2))
pval2 = f.cdf(F, df1, df2)
pval3 = 1.0 - f.cdf(F, df1, df2)

print("Test Statistic and Degrees of Freedom")
print("F = " + str(F))
print("df1 = " + str(df1))
print("df2 = " + str(df2))
print("")
    
print("Two-Sided Test")
print("H0: \u03C3x == \u03C3y")
print("HA: \u03C3x =/= \u03C3y")
print("p = " + str(pval1))
print("")

print("Left-Sided Test")
print("H0: \u03C3x >= \u03C3y")
print("HA: \u03C3x < \u03C3y")
print("p = " + str(pval2))
print("")

print("Right-Sided Test")
print("H0: \u03C3x <= \u03C3y")
print("HA: \u03C3x > \u03C3y")
print("p = " + str(pval3))
