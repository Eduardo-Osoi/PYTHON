import math
import nump as np
import pandas as pd

#  Función de distribución acumulativa
def cdf(z):
    return round(0.5  * (1 + math.erf(z / math.sqrt(2))), 4)

# Crear un DataFrame vacío para la tabla
z_scores = []
probabilities = []

done = True

while done:
    try:
        # Pedir el valor de la media
        mu = float(input('Media: '))
        # Pedir el valor de la desviación estándar
        sigma = float(input('Desviación estándar: '))
        # Pedir el valor de x
        x = float(input('Valor de x: '))
        # Calcular el valor z
        z = (x - mu) / sigma
        # Calcular la probabilidad
        p = cdf(z)
        # Mostrar el resultado
        print(f'Z-Score: {z}')
        print(f'Probabilidad: {p}')
        # Preguntar si se desea continuar
        done = input('¿Desea continuar? (s/n): ') == 's'
    except ValueError:
        print('Error: Ingrese un valor válido.')    
# Calcular los valores z y las probabilidades correspondientes
for z in np.arange(0.0, 3.7, 0.1):
    z_scores.append(z)
    probabilities.append(cdf(z))

# Crear el DataFrame con los valores obtenidos
data = {'Z-Score': z_scores, 'Probability': probabilities}
df = pd.DataFrame(data)

# Mostrar la tabla
#print(df)
print(cdf(0.01))
