#Questions de cours semaine 5 J. Fasoli

from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def f(X, t, k):
  x, v = X
  dxdt = v
  dvdt = -v - k / (x**2 + 1)
  return [dxdt, dvdt]

def solution(x0, v0, T, k):
  t = np.linspace(0, T, 1000)  
  X0 = [x0, v0] 
  X = odeint(f, X0, t, args=(k,))
  return t, X[:, 0]  

# Test 1 : x0 = 1, v0 = 0, T = 10, k = 1
t, x = solution(1, 0, 10, 1)
plt.plot(t, x)
plt.title('Test 1 : x0 = 1, v0 = 0, T = 10, k = 1')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.show()

# Test 2 : x0 = 0, v0 = 1, T = 5, k = 0.5
t, x = solution(0, 1, 5, 0.5)
plt.plot(t, x)
plt.title('Test 2 : x0 = 0, v0 = 1, T = 5, k = 0.5')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.show()
