import math
n = 100 
potencia = math.factorial(n) 
digitos = [potencia]

suma_digitos = sum(int(digito) for digito in str(digitos[0])) 

print(suma_digitos)