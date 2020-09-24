print("Hola mucho gusto soy un programa que realiza sumas, restas, multiplicaciones, divisiones,")
print("entregó el residuo de una división y elevo un número a la potencia")

nombre = input(" ¿desea utilizarme ?: ")
print("¿",nombre, "?,", "muy bien")

print("acontinuación digite los números a utilizar")

numero1 = float(input("Digite un número: "))
numero2 = float(input("Digite un segundo número: "))

e = input("¿Qué operación desea realizar? "
          "a)suma, "
          "b)resta, "
          "c)multiplicacion, "
          "d)división, "
          "e)residuo de división, "
          "f)elevar a la potencia: -> ")

if e == "a":
    r = numero1 + numero2
    print("La respuesta es:", r)
elif e == "b":
    r = numero1 - numero2
    print("La respuesta es:", r)
if e == "c":
    r = numero1 * numero2
    print("La respuesta es:", r)
elif e == "d":
    r = numero1 / numero2
    print("La respuesta es:", r)
if e == "e":
    r = numero1 % numero2
    print("La respuesta es:", r)
elif e == "f":
    r = numero1 ** numero2
    print("La respuesta es:", r)

print("Gracias por utilizarme hasta luego uwu.")

########################################################################################################################



