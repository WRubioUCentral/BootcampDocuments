Algoritmo AdivinarNumero
	Definir n Como Entero
	Definir numero Como Entero
	numero = 2
	Escribir "Voy a adivinar tu n�mero."
	Escribir "Ingresa tu n�mero: "
	Leer n
	
	Mientras (n <> numero) Hacer
		Escribir n, " no es mi n�mero, intentalo de nuevo."
		Leer n
	Fin Mientras
	
	Escribir n, " si es mi n�mero. Chao"
FinAlgoritmo