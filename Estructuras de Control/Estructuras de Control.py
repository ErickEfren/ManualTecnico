# Estructura de control if
x = 10
if x > 5:
    print("x es mayor que 5")

# Estructura de control if-else
y = 3
if y > 5:
    print("y es mayor que 5")
else:
    print("y es menor o igual que 5")

# Estructura de control if-elif-else
z = 7
if z < 5:
    print("z es menor que 5")
elif z < 10:
    print("z es mayor o igual que 5 pero menor que 10")
else:
    print("z es mayor o igual que 10")

# Estructura de control while
i = 0
while i < 5:
    print(i)
    i += 1

# Estructura de control for
lista = [1, 2, 3, 4, 5]
for num in lista:
    print(num)

# Estructura de control range
for i in range(5):
    print(i)

# Estructura de control break
for letra in "Python":
    if letra == "h":
        break
    print(letra)

# Estructura de control continue
for letra in "Python":
    if letra == "h":
        continue
    print(letra)

# Estructura de control pass
def mi_funcion():
    pass

# Estructura de control try-except
x = "10"
try:
    x = int(x)
except ValueError:
    print("No se pudo convertir a entero.")
else:
    print(f"x es {x}")

# Estructura de control assert
x = 10
assert x == 10, "x debe ser igual a 10"
