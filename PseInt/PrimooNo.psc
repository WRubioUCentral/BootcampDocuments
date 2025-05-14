Algoritmo PrimooNo
	Definir n Como Entero
	Definir salida Como Logico
	Escribir "Veremos si el número es primo, ingresalo"
	Leer n
	
	Para i<-2 Hasta (n-1) Con Paso 1 Hacer
		Si (n % i) = 0
			salida <- Falso
			Escribir n, " es divisible por ", i
		FinSi
	Fin Para
	
	Si salida = Falso Entonces
		Escribir "No es primo."
	SiNo
		Escribir n, " es primo."
	FinSi
	
FinAlgoritmo