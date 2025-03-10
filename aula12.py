# 1. Faça um programa que peça a idade do usuario e imprima se ele for maior ou
# menor de 18
idade = int(input("digite sua idade"))

if idade >= 18:
    print("é de maior!")
else:
    print("é de menor!")

    # 2. faça um programa que peça um numero que mostre se ele é positivo ou negativo.

    numero = int(input("digite um numero inteiro: "))

    if numero >= 0:
        print("o numero é positivo")
    else:
        print("o numero é negativo")
        
# 3. Faça um programa que, dado mum numero digitado, mostra se ele é par ou impar.

numero = int(input("digite um numero inteiro: "))
if numero % 2 == 0:
    print("o numero é par.")
else:
    print("o numero é impar")

    # 4. faça um programa que peça dois numeros e mostre o maior deles.

    n1 = int(input("digite um inteiro: "))
    n2 = int(input("digite outro inteiro: "))

    if n1 > n2:
        print(n1)
    else:
        print(n2)

        # 5.faça um programa que leia a validade das informações:
        # a. idade : entre 0 e 150;
        # b. salario: maior que 0
        # c. sexo: m, f ou outro;

        idade = int(input("digite a idade maior que o menor 150: "))
        if idade > 0 and idade < 150:
          print("idade valida")
        else:
            print("idade invalida")
