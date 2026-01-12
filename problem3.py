numero = 600851475143
factor = 2

while factor * factor <= numero:
    if numero % factor == 0:
        numero = numero // factor
    else:
        factor += 1

print(numero)

