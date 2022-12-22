print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 24

chute_str = input("Digite o seu número: ")
print("Você digitou: ", chute_str)
chute = int(chute_str)

if (numero_secreto == chute):
    print("Você acertou, essa é a nossa data de namoro!",
          "\n\nAmo você!!!")

else:
    print("Você errou, tente novamente!")


