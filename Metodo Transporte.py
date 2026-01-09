from pulp import LpProblem, LpVariable, LpMinimize, lpSum, LpStatus

# Datos del problema
silos = ['Silo1', 'Silo2', 'Silo3'] 
molinos = ['Molino1', 'Molino2', 'Molino3', 'Molino4'] 

oferta = { 
    'Silo1': 15, 
    'Silo2': 25,
    'Silo3': 10}
demanda = { 
    'Molino1': 5,
    'Molino2': 15,
    'Molino3': 15,
    'Molino4': 15}
costos = {
    ('Silo1', 'Molino1'): 10, ('Silo1', 'Molino2'): 2, ('Silo1', 'Molino3'): 20, ('Silo1', 'Molino4'): 11,
    ('Silo2', 'Molino1'): 7, ('Silo2', 'Molino2'): 9, ('Silo2', 'Molino3'): 24, ('Silo2', 'Molino4'): 12,
    ('Silo3', 'Molino1'): 4, ('Silo3', 'Molino2'): 14, ('Silo3', 'Molino3'): 16, ('Silo3', 'Molino4'): 18}

# Crear el problema de optimización
asunto = LpProblem("Problema de transporte", LpMinimize)

# Variables de decisión
x = LpVariable.dicts("Envios", (silos, molinos), lowBound=0, cat='Integer')

# Función objetivo
asunto += lpSum(costos[(silo, molino)] * x[silo][molino] for silo in silos for molino in molinos)

# Restricciones de oferta
for silo in silos:
    asunto += lpSum(x[silo][molino] for molino in molinos) <= oferta[silo]

# Restricciones de demanda
for molino in molinos:
    asunto += lpSum(x[silo][molino] for silo in silos) >= demanda[molino]

# Resolver el problema
asunto.solve()

# Imprimir el estado de la solución
print("Estado de la solución:", LpStatus[asunto.status])

# Imprimir la cantidad de camiones cargados enviados desde cada silo al molino
for silo in silos:
    for molino in molinos:
        print(f"Enviar {int(x[silo][molino].value())} camiones cargados desde {silo} a {molino}")

# Imprimir el costo total de transporte
print("Costo total de transporte: $", round(asunto.objective.value(), 2))