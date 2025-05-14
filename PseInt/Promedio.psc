Algoritmo Promedio
	Definir p Como Real
	p = 0
	Dimension notas[5]
	notas[1] <- 2
	notas[2] <- 3
	notas[3] <- 4
	notas[4] <- 1
	notas[5] <- 2.5
	
	Para i<-1 Hasta 5 Hacer
		p = p + notas[i]
	FinPara
	p = p / 5
	
	Escribir "El promedio de sus notas es ", p
FinAlgoritmo