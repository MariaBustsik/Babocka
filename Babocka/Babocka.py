import numpy as np
import matplotlib
import matplotlib.pyplot as plt

#Формирование данных и построение диаграммы
x1 = np.arange(-9, -1, 0.01)
x2 = np.arange(1, 9, 0.01)
x3 = np.arange(-9, -8, 0.01)
x4 = np.arange(8, 9, 0.01)
x5 = np.arange(-8, -1, 0.01)
x6 = np.arange(1, 8, 0.01)
x7 = np.arange(-8, -1, 0.01)
x8 = np.arange(1, 8, 0.01)
x9 = np.arange(-8, -2, 0.01)
x10 = np.arange(2, 8, 0.01)
x11 = np.arange(-2, -1, 0.01)
x12 = np.arange(1, 2, 0.01)
x13 = np.arange(-1, 1, 0.01)
x14 = np.arange(-1, 1, 0.01)
x15 = np.arange(-2, 0, 0.01)
x16 = np.arange(0, 2, 0.01)

y1 = (-1/8)*((x1 + 9)**2) + 8
y2 = (-1/8)*((x2 - 9)**2) + 8
y3 = 7*((x3 + 8)**2) + 1
y4 = 7*((x4 - 8)**2) + 1
y5 = (1/49)*((x5 + 1)**2)
y6 = (1/49)*((x6 - 1)**2)
y7 = -(4/49)*((x7 + 1)**2)
y8 = -(4/49)*((x8 - 1)**2)
y9 = (1/3)*((x9 + 5)**2) - 7
y10 = (1/3)*((x10 - 5)**2) - 7
y11 = -2*((x11 + 1)**2) - 2
y12 = -2*((x12 - 1)**2) - 2
y13 = -4*(x13**2) + 2
y14 = 4*(x14)**2 - 6
y15 = -1.5*x15 + 2
y16 = 1.5*x16 + 2

plt.subplots()
plt.grid(True)# Отображение сетки на координатной плоскости

plt.plot(x1,y1,'-r',linewidth=1)
plt.plot(x2,y2,'-r',linewidth=1)
plt.plot(x3,y3,'-r',linewidth=1)
plt.plot(x4,y4,'-r',linewidth=1)
plt.plot(x5,y5,'-r',linewidth=1)
plt.plot(x6,y6,'-r',linewidth=1)
plt.plot(x7,y7,'-r',linewidth=1)
plt.plot(x8,y8,'-r',linewidth=1)
plt.plot(x9,y9,'-r',linewidth=1)
plt.plot(x10,y10,'-r',linewidth=1)
plt.plot(x11,y11,'-r',linewidth=1)
plt.plot(x12,y12,'-r',linewidth=1)
plt.plot(x13,y13,'-r',linewidth=1)
plt.plot(x14,y14,'-r',linewidth=1)
plt.plot(x15,y15,'-r',linewidth=1)
plt.plot(x16,y16,'-r',linewidth=1)


plt.show()  # Вывод изображения на экран
