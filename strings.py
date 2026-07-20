# En esta seccion se abordan los temas relacionados a strings en python

string = "este es un string"
print(string)

# Se puede manipular como un objeto de tipo lista ya que es iterable
for index in range(len(string)):
    print(string[index])

# Tambien se le pueden hacer varias manipulaciones
string.capitalize # Hace la primera letra mayuscula

new_string = string.upper() # hace todas las letras mayusculas
print(new_string)

new_string = string.lower() # hace todas las letras minusculas
print(new_string)