suma = 0

for numero in range(1000):
    if numero % 3 == 0 or numero % 5 == 0:
        suma = suma + numero

print(suma)
