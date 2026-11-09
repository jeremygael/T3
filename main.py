
import random
import math

# Ingreso de datos
a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
c = int(input("Ingrese el valor de c: "))
d = int(input("Ingrese el valor de d: "))
cantidad = int(input("Ingrese la cantidad de puntos aleatorios: "))

# Validacion
if a <= 0 or b <= 0 or c <= 0 or d <= 0 or cantidad <= 0:
    print("Error: todos los valores deben ser mayores que cero.")
    exit()

# Contadores
puntos_elipse = 0
puntos_interseccion = 0

# Generacion de puntos aleatorios dentro del rectangulo
for _ in range(cantidad):
    x = random.uniform(-a, a)
    y = random.uniform(-b, b)

    # Verificar si pertenece a la elipse
    if (x**2)/(a**2) + (y**2)/(b**2) <= 1:
        puntos_elipse += 1

        # Verificar si ademas pertenece a la hiperbola
        if (x**2)/(c**2) - (y**2)/(d**2) >= 1:
            puntos_interseccion += 1

# Area de la elipse por formula
area_elipse = math.pi * a * b

# Area del rectangulo
area_rectangulo = (2*a) * (2*b)

# Metodo Monte Carlo basado en proporcion
if cantidad > 0:
    area_interseccion = (puntos_interseccion / cantidad) * area_rectangulo
else:
    area_interseccion = 0

# Porcentaje de interseccion respecto a la elipse
if puntos_elipse > 0:
    porcentaje_interseccion = (puntos_interseccion / puntos_elipse) * 100
else:
    porcentaje_interseccion = 0

# Resultados
print("\n========== RESULTADOS ==========")
print(f"Total de puntos generados: {cantidad}")
print(f"Puntos dentro de la elipse: {puntos_elipse}")
print(f"Puntos en la interseccion: {puntos_interseccion}")

print(f"\nArea de la elipse por formula: {area_elipse:.6f}")
print(f"Area de interseccion por Monte Carlo: {area_interseccion:.6f}")

print(f"\nPorcentaje de interseccion: {porcentaje_interseccion:.2f}%")
print("================================")
