#Definimos las funciones que necesitamos para resolver el problema de la mochila

def is_complete_backpack_problem(partial_solution, capacity, available_items):
    #  La condición de parada es alcanzar o superar la capacidad de la mochila o no tener más opciones disponibles
    peso_total = sum(item[1] for item in partial_solution)
    print("Peso total:" , peso_total)
    return peso_total >= capacity or len(available_items) == 0


def select_best_option_backpack_problem(partial_solution, available_items):
    #  Seleccionar la mejor opción local basada en la relación valor/peso
    valid_options = [item for item in available_items if item not in partial_solution]
    mejor_opcion = max(valid_options, key=lambda x: x[0] / x[1])
    return mejor_opcion



#  Definimos la función que resuelve el problema de la mochila

def greedy_backpack_problem(is_complete, select_best_option, options, capacity):
    #  Paso 1: Inicialización
    partial_solution = []
    #  Paso 5: Mientras no se cumpla la condición de parada
    while not is_complete(partial_solution, capacity, options):
        #  Paso 2: Selección de la mejor opción local
        best_option = select_best_option(partial_solution, options)
        
        #  Si la mejor opción supera la capacidad de la mochila se elimina de las opciones disponibles
        umbral_factor = 1
        if (sum(item[1] for item in partial_solution) + best_option[1]) * umbral_factor > capacity:
            options.remove(best_option)
            break

        #  Paso 3: Agregar la mejor opción local a la solución parcial
        partial_solution.append(best_option)
        #  Paso 4: Actualizar las opciones disponibles
        options.remove(best_option)
    #  Paso 6: Devolver la solución parcial
    return print(partial_solution)

#  Ejemplo 1
items = [(60, 10), (100, 20), (120, 30)]  #  (valor, peso)
capacity = 50
greedy_backpack_problem(is_complete_backpack_problem, select_best_option_backpack_problem, items, capacity)

#  Ejemplo 2
items = [(9, 150), (1000, 10000), (8, 100), (7, 200), (6, 50), (15, 300)]  #  (valor, peso)
capacity = 750
#greedy_backpack_problem(is_complete_backpack_problem, select_best_option_backpack_problem, items, capacitiy)

#--------------------------------------------
#  Entradas por consola
def ask_for_entrys():
    items = []
    print("Ingrese los elementos de la mochila en el formato: valor, peso")
    print("Cuando termine de ingresar los elementos escriba 'listo'")
    while True:
        entrada = input()
        if entrada == "listo":
            break
        else:
            items.append(tuple(map(int, entrada.split(","))))
    print("Ingrese la capacidad de la mochila")
    capacity = int(input())
    greedy_backpack_problem(is_complete_backpack_problem, select_best_option_backpack_problem, items, capacity)


ask_for_entrys()
