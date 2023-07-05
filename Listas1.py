a=[90,"Python",3.52]

# Imprimir el último elemento de la lista.
print(a[-1])

#--------------------------
# ??
print(a[-2])

#------------------------------
#El método append(), permite agregar elementos al final de la lista.

a.append("Java")
print(a[-1])

# -----------------------
# Imprimir la lista con todos sus elementos
print(a)

#-------------------
#El Método Insert permite ingresar un elemento en la Posición deseada

a.insert(0,"Primero")
print(a)

#----------------------------
#El método remove(), permite recibir como argumento un objeto y lo borra de la lista.
a.remove(3.52)
print(a)

#-------------------------------------------------------
# El método pop(), elimina el último elemento de la lista
a.pop()
print(a)

#-------------------------------------------------------
# El método pop(posicion), elimina el elemento de la posicion ingresada
a.pop(1)
print(a)





