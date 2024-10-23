#DFT OF GIVEN SEQUENCE EXP-1 
import numpy as np 
import matplotlib.pyplot as plt 
x = np.array([2, -2+2j, 3+1j, 1]) 
N = len(x) 
X = np.zeros(N, dtype=complex) 
for k in range(N): 
for n in range(N): 
X[k] += x[n] * np.exp(-2j * np.pi * k * n / N) 
print("Input sequence is:") 
print(x) 
print("DFT of x(n) is :") 
print(X)
