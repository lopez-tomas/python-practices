def main():
    edad = int(input("¿Cuántos años tienes? "))
    if edad>18:
        print("Eres mayor de edad.")
    else:
        print("Eres menor de edad.")

#> < == != >=

    if edad >18:
        if edad <45:
            print("Tienes la edad necesaria para el programa de capacitación militar.")

        else:
            print("Eres demasiado viejo para el programa de capacitación militar.")

    else:
        print("Eres demasiado jóven para el programa de capacitación militar.")

main()