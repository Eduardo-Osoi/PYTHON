from scipy.optimize import linprog

# Coeficientes de la función objetivo
z = [6, 2]

# Coeficientes de las restricciones (lado izquierdo de las desigualdades)
A = [[0.5, 0.2], [-2, -3],[-1, -1]]

# Términos constantes de las restricciones (lado derecho de las desigualdades)
b = [4, -20, -10]

# Límites de las variables (X y Y son no negativas)
x_bounds = (0, None)
y_bounds = (0, None)

# Resolver el problema de optimización
resultado = linprog(z, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

# Imprimir el resultado
print("Estado de la solución:", resultado.message)
print("Valor óptimo de Z:", resultado.fun)
print("Valor óptimo de X:", resultado.x[0])
print("Valor óptimo de Y:", resultado.x[1])
