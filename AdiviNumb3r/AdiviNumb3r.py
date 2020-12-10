from random import randint as rango
user=0
cpu=0
while True:
    name=input("Ingrese nombre de usuario: ")
    if len(name)<=16 and name.isalnum():
        break
    else:
        print("El nombre de usuario solo debe contener caracteres alfanuméricos (y solo 16 dígitos)")
while True:
    print(f"{name}: {user} - CPU: {cpu}")
    lista=["=",">","<"]
    while True:
        af=input("¿Es un número en el rango del 0 al 100? (S/N)\n")
        af=af.upper()
        if af=="S":
            print("Ok. Comencemos.")
            a=0
            b=100
            break
        elif af=="N":
            while True:
                a=input("Ingrese límite inicial (Recuerde que el límite inicial será esta cantidad añadida en 100):\n")
                if a.isnumeric():
                    a=int(a)
                    if a<(9*10**10):
                        b=a+100
                        break
                    else:
                        print("Ingrese valores menores a 9x10¹⁰")
                else:
                    print("Ingrese solamente valores mayores a cero (0)")
            break
        else:
            print("Ingrese valores correctos")
    num=rango(a,(a+b)/2)
    while True:
        af=input(f"¿El número es mayor a {num}? (S/N)\n")
        af=af.upper()
        if af == "S":
            lii = num + 1
            lif = b
            break
        elif af == "N":
            lii = a
            lif = num
            break
        else:
            print("Ingrese valores correctos")
    num = rango(lii, lif)
    j = 9
    while j >= 0:
        n=input(f"¿Usted pensó en el número {num}? ('>','<','='). Me quedan {j} intentos.\n")
        if n == lista[0]:
            print("¡Excelente!!! He acertado.",end="")
            cpu+=1
            break
        elif n == lista[1] or n == lista[2]:
            j -= 1
            if n==lista[1]:
                lii=num+1
                if lii!=lif and lii!=lif+1:
                    num=rango(lii,lif)
                else:
                    print(f"Usted pensó en el número {lii}")
                    cpu+=1
                    print("¡Excelente!!! He acertado.",end="")
                    break
            else:
                lif=num-1
                if lii!=lif and lii!=lif+1:
                    num=rango(lii,lif)
                else:
                    print(f"Usted pensó en el número {lii}")
                    cpu+=1
                    print("¡Excelente!!! He acertado.",end="")
                    break
        else:
            print("Ingrese valores correctos")
        if j==0:
            print("He fallado...")
            while True:
                num=input("¿Cuál fue el número que tuviste en mente?\n")
                if num.isnumeric():
                    num=int(num)
                    if lii<=num<=lif:
                        user+=1
                        break
            break
    while True:
        s=input("¿Quieres volver a jugar? (S/N)\n")
        s=s.upper()
        if s=="S":
            break
        elif s=="N":
            print("HASTA LUEGO")
            break
        else:
            pass
    if s=="N":
        break
input()