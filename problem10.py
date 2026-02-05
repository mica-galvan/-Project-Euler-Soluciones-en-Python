import math
num = 3
lista_primos=[2]
total = 2

while True:
    primo = True

    for divisor in range(2, int(math.sqrt(num)) + 1):
    #for divisor in lista_primos: # funciona porque si no es divisible por uno de mis numero primos ya guardados, entonces es primo.
        if num % divisor == 0:
            primo = False
            break

    if primo:
        lista_primos.append(num)
    
    if num>=2000000:
        break

    num = num +2


total= sum(lista_primos)

print(total)