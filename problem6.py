#Encontrar la diferencia entre la suma de los cuadrados de los primeros 100 numeros naturales y el cuadrado de la suma de los primeros 100 numeros naturales. Potencia es ** (cuadrado es **2)
#cuadrado de la suma (1,2,3 ...100)**2
#suma de cuadrados 1**2 + 2**2 + 3**2

cuadrado_suma = 0
suma = 0
suma_cuadrados = 0
resultado = 0

for numero in range (1,101):
 suma = suma + numero
 suma_cuadrados = suma_cuadrados + numero ** 2

cuadrado_suma = suma ** 2

resultado =  cuadrado_suma - suma_cuadrados
print(resultado)

