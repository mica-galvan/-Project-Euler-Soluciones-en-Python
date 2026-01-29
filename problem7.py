num = 2
lista_primos=[]

while True:
    primo = True

    for divisor in range(2, num):
        if num % divisor == 0:
            primo = False
            break

    if primo:
        lista_primos.append(num)
    
    if len(lista_primos) ==10001:
        break

    num = num +1

print(lista_primos[10000])