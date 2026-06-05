# Calculadora Basica

Aplicacion de consola para practicar logica de programacion con las 4 operaciones aritmeticas basicas.

## Como ejecutar

```bash
python calculadora.py
```

## Funciones

| Funcion | Que hace |
|---|---|
| `sumar(a, b)` | Retorna la suma de dos numeros |
| `restar(a, b)` | Retorna la resta de dos numeros |
| `multiplicar(a, b)` | Retorna la multiplicacion de dos numeros |
| `dividir(a, b)` | Retorna la division; si `b == 0` retorna mensaje de error |
| `obtener_numero(mensaje)` | Pide un numero al usuario y valida que sea numerico |
| `mostrar_menu()` | Imprime el menu de opciones en consola |
| `main()` | Controla el flujo principal del programa en un bucle |

## Diagrama de flujo

```
Inicio
  │
  ▼
mostrar_menu()
  │
  ▼
¿Opcion ingresada?
  ├─ "5" ──────────────────────> Salir
  │
  ├─ "1","2","3","4"
  │       │
  │       V
  │   obtener_numero(a) para primer numero
  │       │
  │       V
  │   obtener_numero(b) para segundo numero
  │       │
  │       V
  │   ejecutar operacion (sumar / restar / multiplicar / dividir)
  │       │
  │       V
  │   mostrar resultado
  │       │
  │       └──────────────────── volver a mostrar_menu()
  │
  └─ otra ──────────────────────> "Opcion no valida" → volver al menú
```

