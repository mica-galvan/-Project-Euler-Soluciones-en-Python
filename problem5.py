numero = 2

while True:
    divisible = True

    for divisor in range(2, 21):  # del 2 al 20 . Para cada número que salga de range(2, 21), guardalo en una variable llamada divisor y ejecutá el código de abajo #
        if numero % divisor != 0:
            divisible = False
            break

    if divisible:
        print(numero)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
        break

    numero += 1  # pruebo el siguiente número
