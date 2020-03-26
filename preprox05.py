import matplotlib.pyplot as plt
import numpy as np


def func(x):
    return 1 / (1 + np.exp(-x))


# データ生成
x = np.linspace(-10.0, 10.0, 100)
y = func(x)
plt.plot(x, y)
plt.show()

x = np.linspace(0, 120, 100)
plt.ylim(-1, 5)
y = 0
count = 1
a = 0
k = 0
while k < 20:
    i = 0
    j = 0
    while i < count:
        a += 10
        y += func(5 * (x - a))
        i += 1
    while j < count:
        a += 10
        y -= func(5 * (x - a))
        j += 1
    count += 1
    k += 1
plt.plot(x, y)
plt.show()
