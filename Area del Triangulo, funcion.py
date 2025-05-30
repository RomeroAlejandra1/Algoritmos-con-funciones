def area_triangulo(base, altura):
    return base * altura/2
base = float(input("ingresa la base: "))
altura = float(input("ingresa la altura: "))

resultado = area_triangulo(base, altura)
print ("la area es:", resultado)