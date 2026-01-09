#  Definicmos las funciones que necesitamos para resolver el problema de las monedas
def is_complete_coin_problem(partial_solution, target):
    return sum(partial_solution) >= target


def select_best_option_coin_problem(partial_solution, available_coins, target):
    #  Determinar cuanto falta por dar de cambio
    remaining_change = target - sum(partial_solution)
    #  Filtrar las denominaciones que no exceden el cambio restante
    valid_options = [denomination for denomination in available_coins if denomination <= remaining_change]
    #  Elegir la moneda de mayor denominación
    best_option = max(valid_options)
    return best_option

#  Definimos la función que resuelve el problema de las monedas
def greedy_coin_problem(is_complete, select_best_option, options, target):
    #  Paso 1: Inicialización
    partial_solution = []
    #  Paso 5: Mientras no se cumpla la condición de parada
    while not is_complete(partial_solution, target):
        #  Paso 2: Selección de la mejor opción local
        best_option = select_best_option(partial_solution, options, target)
        #  Paso 3: Agregar la mejor opción local a la solución parcial
        partial_solution.append(best_option)
        #  Paso 4: Actualizar las opciones disponibles
        options.remove(best_option)
    #  Paso 6: Devolver la solución parcial
    return print(partial_solution)


greedy_coin_problem(is_complete_coin_problem, select_best_option_coin_problem, [1, 2, 5, 10, 20, 50, 100, 200], 123)

#--------------------------------------------
#  Entradas por consola
def ask_for_entrys():
    options = []
    print("Ingrese las denominaciones de las monedas en el formato: denominacion")
    print("Cuando termine de ingresar las denominaciones escriba 'listo'")
    while True:
        entrada = input()
        if entrada == "listo":
            break
        options.append(int(entrada))
    print("Ingrese el valor de la devuelta")
    target = int(input())
    greedy_coin_problem(is_complete_coin_problem, select_best_option_coin_problem, options, target)


ask_for_entrys()
