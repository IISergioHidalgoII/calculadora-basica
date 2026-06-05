def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: no se puede dividir entre cero"
    return a / b

def obtener_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada invalida. Ingresa un numero.")

def mostrar_menu():
    print("\n===== Calculadora Basica =====")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    print("==============================")

def main():
    operaciones = {
        "1": ("Suma", sumar),
        "2": ("Resta", restar),
        "3": ("Multiplicacion", multiplicar),
        "4": ("Division", dividir),
    }

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opcion: ").strip()

        if opcion == "5":
            print("Bye bye!")
            break
        elif opcion in operaciones:
            nombre, funcion = operaciones[opcion]
            a = obtener_numero("Ingresa el primer numero: ")
            b = obtener_numero("Ingresa el segundo numero: ")
            resultado = funcion(a, b)
            print(f"\nResultado ({nombre}): {resultado} de {a} y {b}")
        else:
            print("Opcion no valida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
