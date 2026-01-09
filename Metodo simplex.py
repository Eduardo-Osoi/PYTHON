

import numpy as np
from scipy.optimize import linprog

#Definir la función objetivo y las restricciones en forma de matrices
Z = np.array([110, 150])

restricciones = np.array([[4, 6], [20, 10]])

r = np.array([480, 1500])

# Resolver el problema utilizando el método simplex a través de la función linprog
resultado = linprog(-Z, A_ub=restricciones, b_ub=r, method='simplex')

# Imprimir el resultado

print("Status:", resultado.message)

print("solución óptima:")

print("x =", round(resultado.x[0], 2))

print("y =", round(resultado.x[1], 2))

print("Valor óptimo de la función objetivo: Z =", round(-resultado.fun, 2))

