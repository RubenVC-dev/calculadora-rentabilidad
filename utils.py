import os

def pedir_float(mensaje):
    while True:
        entrada = input(mensaje).strip()
        if entrada == "":
            print("No puedes dejar esto vacío.")
            continue
        try:
            return float(entrada)
        except ValueError:
            print("Error: Por favor, introduce un número válido.")

def pedir_int(mensaje):
    while True:
        entrada = input(mensaje).strip()
        if entrada == "":
            print("No puedes dejar esto vacío.")
            continue
        try:
            return int(entrada)
        except ValueError:
            print("Error: Por favor, introduce un número entero válido.")

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')