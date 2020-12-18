import sys
from Satelite import Satelite
from Problema import Problema

def main():
    print("Número de parámetros: ", len(sys.argv))
    print("Lista de argumentos: ", sys.argv)

    if len(sys.argv) != 3:
        print("El problema no tiene el numero corecto de parametros")
        return -1

    # abrimos el fichero de problemas
    if sys.argv[1].split('.')[1] != "prob":
        print("El problema no tiene la extension .prob")
        return -1

    archivo_problema = open(sys.argv[1], 'r')
    string_problema = archivo_problema.read()
    print(string_problema)

    matriz_problema = string_problema.splitlines()
    print(matriz_problema)

    observaciones = matriz_problema[0][5:].split(';')
    tuplas_observaciones = []
    for i in observaciones:
        tuplas_observaciones.append(eval(i[1:4]))

    print("Observaciones: " + str(tuplas_observaciones))
    print(observaciones)
    satelites = []

    for i in range(1, len(matriz_problema)):
        satelites.append(matriz_problema[i])

    print("Satelites: " + str(satelites))

    # Satelite 1
    observation_cost1 = satelites[0].split(': ')[1].split(';')[0]
    transmission_cost1 = satelites[0].split(': ')[1].split(';')[1]
    rotation_cost1 = satelites[0].split(': ')[1].split(';')[2]
    charge_power1 = satelites[0].split(': ')[1].split(';')[3]
    battery1 = satelites[0].split(': ')[1].split(';')[4]
    sat1 = Satelite(1, observation_cost1, transmission_cost1, rotation_cost1, charge_power1, battery1, 1)

    # Satelite 2
    observation_cost2 = satelites[1].split(': ')[1].split(';')[0]
    transmission_cost2 = satelites[1].split(': ')[1].split(';')[1]
    rotation_cost2 = satelites[1].split(': ')[1].split(';')[2]
    charge_power2 = satelites[1].split(': ')[1].split(';')[3]
    battery2 = satelites[1].split(': ')[1].split(';')[4]
    sat2 = Satelite(2, observation_cost2, transmission_cost2, rotation_cost2, charge_power2, battery2, 2)

    problema = Problema(sat1, sat2, observaciones)

    problema.a_star_solver()

main()