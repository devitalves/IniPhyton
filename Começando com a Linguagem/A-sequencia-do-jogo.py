print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 24

chute_str = input("Digite o seu número: ")
print("Você digitou: ", chute_str)

chute = int(chute_str)

acertou = numero_secreto == chute
maior = chute > numero_secreto
menor = chute < numero_secreto

if (acertou):
    print("Você acertou!")

else:
    if(maior):
        print("Você errou, o numero foi maior que o numero secreto.")
    elif (menor):
        print("Você errou, o numero foi menor que o numero secreto.")

print("Fim de jogo")


