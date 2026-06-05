# Calculadora Básica

Aplicación de consola para practicar lógica de programación con las 4 operaciones aritméticas básicas.

## Cómo ejecutar

```bash
python calculadora.py
```

## Funciones

| Función | Qué hace |
|---|---|
| `sumar(a, b)` | Retorna la suma de dos números |
| `restar(a, b)` | Retorna la resta de dos números |
| `multiplicar(a, b)` | Retorna la multiplicación de dos números |
| `dividir(a, b)` | Retorna la división; si `b == 0` retorna mensaje de error |
| `obtener_numero(mensaje)` | Pide un número al usuario y valida que sea numérico |
| `mostrar_menu()` | Imprime el menú de opciones en consola |
| `main()` | Controla el flujo principal del programa en un bucle |

## Diagrama de flujo

```
Inicio
  │
  ▼
mostrar_menu()
  │
  ▼
¿Opción ingresada?
  ├─ "5" ──────────────────────► Salir
  │
  ├─ "1","2","3","4"
  │       │
  │       ▼
  │   obtener_numero() x2
  │       │
  │       ▼
  │   ejecutar operación (sumar / restar / multiplicar / dividir)
  │       │
  │       ▼
  │   mostrar resultado
  │       │
  │       └──────────────────── volver a mostrar_menu()
  │
  └─ otra ──────────────────────► "Opción no válida" → volver al menú
```

## Tecnologías

- Python 3
