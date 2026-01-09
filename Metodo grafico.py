import numpy as np
import matplotlib.pyplot as plt

# Función objetivo
def F_O(x, y):
    return 9000 * x + 1200 * y

# Restricciones
def restri1(x):
    return x - 20

def restri2(y):
    return y - 10

def restri3(x, y):
    return 3 * x + 4 * y - 12

# Rango de valores para X y Y
x = np.linspace(0, 25, 50)
y = np.linspace(0, 25, 50)

# Crear malla de coordenadas
X, Y = np.meshgrid(x, y)

# Evaluar restricciones en la malla
restriccion1 = restri1(X)
restriccion2 = restri2(Y)
restriccion3 = restri3(X, Y)

# Verificar la región factible
area_factible = (restriccion1 <= 0) & (restriccion2 <= 0) & (restriccion3 >= 0)

# Crear figura y subgráfico
plt.figure()

# Colorear la región factible
plt.imshow(area_factible, extent=(0, 25, 0, 25), origin='lower', cmap='Purples', alpha=0.3)

# Restricciones
plt.contour(X, Y, restriccion1, [0], colors='red', alpha=0.5, linewidths=2, label='X <= 20')
plt.contour(X, Y, restriccion2, [0], colors='red', alpha=0.5, linewidths=2, label='Y <= 10')
plt.contour(X, Y, restriccion3, [0, 100], colors='red', alpha=0.5, linewidths=2, label='3X + 4Y >= 12')

# Punto de la solución óptima
opt_x = 20
opt_y = 10
opt_z = F_O(opt_x, opt_y)
plt.plot(opt_x, opt_y, 'go', label='Solución Óptima')
plt.text(opt_x + 0.5, opt_y, f'({opt_x}, {opt_y})', verticalalignment='bottom', horizontalalignment='left', color='red')

# Etiquetas de los ejes
plt.xlabel('X')
plt.ylabel('Y')

# Rango de los ejes
plt.xlim(0, 25)
plt.ylim(0, 25)

# Leyenda
plt.legend(title='Solución óptima de Z= 9000x + 1200y')

# Mostrar gráfico
plt.show()
