# File Name: GOFChiSquareTest.py
# Author: Verginia Mae Dole
# Date Created: 4/1/2022

from scipy.stats import chi2

print("Goodness-of-Fit Chi-Square Test")
print("")
print("n = number of cells")
print("O = observed values")
print("p = probabilities")
print("df = degrees of freedom")
print("")

n = int(input("Enter n: "))
while n <= 0:
    n = int(input("Enter n: "))

obs = []
for i in range(n):
    temp = float(input("Enter O" + str(i + 1) + ": "))
    while temp <= 0.0:
        temp = float(input("Enter O" + str(i + 1) + ": "))
    obs.append(temp)
    
prop = []
for i in range(n):
    temp = float(input("Enter p" + str(i + 1) + ": "))
    while temp <= 0.0 or temp >= 1.0 - sum(prop):
        temp = float(input("Enter p" + str(i + 1) + ": "))
    prop.append(temp)

df = int(input("Enter df: "))
while df <= 0 or df >= n:
    df = int(input("Enter df: "))
print("")

exp = []
for i in range(n):
    temp = sum(obs) * prop[i]
    exp.append(temp)

X2 = 0.0
for i in range(n):
    X2 += pow(obs[i] - exp[i], 2) / exp[i]
pval = 1.0 - chi2.cdf(X2, df)

print("Expected")
print("E = " + str(exp))
print("")

print("Hypotheses")
print("H0: O == E")
print("HA: O =/= E")
print("")

print("Test Statistic and Degrees of Freedom")
print("X^2 = " + str(X2))
print("df = " + str(df))
print("")

print("P-Value")
print("p = " + str(pval))
