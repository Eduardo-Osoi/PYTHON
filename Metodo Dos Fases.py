import numpy as np
from scipy.optimize import linprog

# Coeficientes de la función objetivo
z = np.array([6, 2])

# Coeficientes de las restricciones (lado izquierdo de las desigualdades)
restriccion = np.array([[1, 2], [3, 2]])

# Lados derechos de las restricciones
r = np.array([4, 8])

# Resolver el problema de programación lineal utilizando el método de las dos fases
res = linprog(z, A_ub=-restriccion, b_ub=-r, method='simplex')

# Verificar si el problema tiene una solución óptima
if res.success:
    print('El problema tiene una solución óptima:')
    print('x =', res.x[0])
    print('y =', res.x[1])
    print('Z =', res.fun)
else:
    print('El problema no tiene una solución óptima.')

