import numpy as np
import matplotlib.pyplot as plt


def f2(x):
    return x**2


def f(x):
    return x**3 - 2* x ** 2 + 1


# compute y=f(x)
x = np.linspace(-10,10,500)
y = f(x)

fig = plt.figure(figsize=(12,5))
ax = fig.add_subplot(131)
ax.plot(x,y)
ax.set_title("y=f(x)")

#compute y=f'(x)
delta_x = 0.0001
y1 = (f(x+delta_x) - f(x))/ delta_x
y2 = 3*x**2 - 4

ax = fig.add_subplot(132)
ax.plot(x,y1, c="r", alpha=0.5, label="rate")
ax = fig.add_subplot(133)
ax.plot(x,y2, c="b", alpha=0.5, label="rule")
ax.set_title("y=f'(x)")
plt.show()

plt.show()

