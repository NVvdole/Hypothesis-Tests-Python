# File Name: OneStdDevChiSquareTest.py
# Author: Verginia Mae Dole
# Date Created: 4/1/2022

from scipy.stats import chi2

print("One Standard Deviation Chi-Square Test")
print("")
print("\u03C3x0 = hypothesized population std dev")
print("sx = sample std dev")
print("nx = sample size")
print("")

sig = float(input("Enter \u03C3x0: "))
while sig <= 0.0:
    sig = float(input("Enter \u03C3x0: "))
    
std_dev = float(input("Enter sx: "))
while std_dev <= 0.0:
    std_dev = float(input("Enter sx: "))
    
n = int(input("Enter nx: "))
while n <= 0:
    n = int(input("Enter nx: "))
print("")

df = n - 1
X2 = ((n - 1) * pow(std_dev, 2)) / pow(sig, 2)

if X2 <= chi2.median(df):
    pval1 = 2.0 * chi2.cdf(X2, df)
else:
    pval1 = 2.0 * (1.0 - chi2.cdf(X2, df))
pval2 = chi2.cdf(X2, df)    
pval3 = 1.0 - chi2.cdf(X2, df)
    
print("Test Statistic and Degrees of Freedom")
print("X^2 = " + str(X2))
print("df = " + str(df))
print("")

print("Two-Sided Test")
print("H0: \u03C3x == " + str(sig))
print("HA: \u03C3x =/= " + str(sig))
print("p = " + str(pval1))
print("")

print("Left-Sided Test")
print("H0: \u03C3x >= " + str(sig))
print("HA: \u03C3x < " + str(sig))
print("p = " + str(pval2))
print("")

print("Right-Sided Test")
print("H0: \u03C3x <= " + str(sig))
print("HA: \u03C3x > " + str(sig))
print("p = " + str(pval3))
