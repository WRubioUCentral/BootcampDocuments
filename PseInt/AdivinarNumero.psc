Algoritmo AdivinarNumero
	Definir n Como Entero
	Definir numero Como Entero
	numero = 2
	Escribir "Voy a adivinar tu número."
	Escribir "Ingresa tu número: "
	Leer n
	
	Mientras (n <> numero) Hacer
		Escribir n, " no es mi número, intentalo de nuevo."
		Leer n
	Fin Mientras
	
	Escribir n, " si es mi número. Chao"
FinAlgoritmo