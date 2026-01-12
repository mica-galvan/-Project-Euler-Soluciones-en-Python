a = 1
b = 2
suma = 0

while b <= 4000000:
    if b % 2 == 0:
        suma = suma + b

    siguiente = a + b
    a = b
    b = siguiente

print(suma)
