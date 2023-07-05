# Implementar un programa que permita leer la cantidad de notas de un alumno,
# luego, almacenar cada nota ingresada por teclado a una Lista.
# Finalmente, imprimir :
# La nota más alta y más baja
# El promedio del curso
# Número de notas superiores al promedio
# Cantidad de alumnos aprobados y reprobados

Cant_notas=int(input("Ingrese la cantidad de notas del alumno ==> "))
lista=[] #Creación de una lista.
suma_notas=0

for i in range(1,Cant_notas+1):
    nota=float(input("Ingrese la nota : "))
    suma_notas=suma_notas + nota
    lista.append(nota)

promedio=suma_notas/Cant_notas

sup_promedio=0
for j in lista:
    if j>promedio:
        sup_promedio+=1

aprobados=0
for h in lista:
    if h>=4:
        aprobados+=1

reprobados=0
for k in lista:
    if k<4:
        reprobados+=1
        
print("La nota más alta es :", max(lista))
print("La nota más baja es :", min(lista))
print("El promedio de las notas es :", promedio)
print("Cantidad alumnos superiores al promedio es :", sup_promedio)
print("La cantidad de Aprobados es :", aprobados)
print("La cantidad de Reprobados es :", reprobados)






      
    
