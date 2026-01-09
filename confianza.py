import math


#  Función de distribución acumulativa
def cdf(z):
    return round(0.5  * (1 + math.erf(z / math.sqrt(2))), 4)

#  Función de percentil (inverso de la función de distribución acumulativa)(método de la bisección)
def mi_ppf(probability, tol=1e-6):
    # Establecer límites iniciales
    lower_bound = -10.0  
    upper_bound = 10.0
    mid = 0.0
    while upper_bound - lower_bound > tol:
        mid = (upper_bound + lower_bound) / 2.0
        if cdf(mid) > probability:
            upper_bound = mid
        else:
            lower_bound = mid
    return round(mid, 2)

def intervalo_de_confianza():
    # Pedir el valor de la media
    mu = float(input('Media: '))
    # Pedir el valor de la desviación estándar
    sigma = float(input('Desviación estándar: '))
    # Pedir el nivel de confianza
    confianza = float(input('Nivel de confianza: '))
    if confianza > 1:
        confianza /= 100
    # Calcular la probabilidad
    p = confianza + (1 - confianza) / 2
    # Calcular el valor z
    z = mi_ppf(p)
    # Mostrar el resultado
    print(f'Z-Score: {z}')
    print(f'Probabilidad: {p}')
    print(f'Intervalo de confianza: ({mu - z * sigma}, {mu + z * sigma})')
    return z, p

intervalo_de_confianza()
