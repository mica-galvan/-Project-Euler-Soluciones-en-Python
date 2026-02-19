max_palindromo = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        producto = i * j
        

        if str(producto) == str(producto)[::-1]:
            if producto > max_palindromo:
                max_palindromo = producto

print(max_palindromo)
