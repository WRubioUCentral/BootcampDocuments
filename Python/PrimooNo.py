#print("Veremos si el número es primo, ingresalo")
n = int(input("Veremos si el número es primo, ingresalo: "))

for i in range(2, n):
    if n%i == 0:
        salida = False
        print(n, " es divisible por ",i)

if salida == False:
    print("No es primo")
else:
    print(n, " es primo")