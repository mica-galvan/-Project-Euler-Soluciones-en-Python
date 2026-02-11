#print(2**1000)
numero = 2**1000
digitos = [numero]

suma_digitos = sum(int(digito) for digito in str(digitos[0])) #python empieza a contar desde 0 para la suma
print(suma_digitos)

