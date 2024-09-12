import numpy as np
import matplotlib.pyplot as plt

def F(x):
    return np.sqrt(x**3 + 7*x**2 + 10*x)

critical_points = [-5, -2, 0]

x1 = np.linspace(-10, -5, 200)
x2 = np.linspace(-5, -2, 200)
x3 = np.linspace(-2, 0, 200)
x4 = np.linspace(0, 10, 200)
x = np.concatenate((x1, x2, x3, x4))

y = F(x)

plt.plot(x, y)

plt.fill_between(x, 0, y, where=(x >= -5) & (x <= -2) | (x >= 0), alpha=0.3, color='blue')

plt.plot(critical_points, [F(cp) for cp in critical_points], 'ro')

plt.xlabel('x')
plt.ylabel('F(x)')
plt.title('Intervals where F(x) ≥ 0')

plt.show()