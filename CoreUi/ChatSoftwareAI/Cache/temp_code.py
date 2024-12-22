import random

def jogar():
    opcoes = ["pedra", "papel", "tesoura"]
    computador = random.choice(opcoes)

    jogador = input("Escolha pedra, papel ou tesoura: ").lower()

    if jogador not in opcoes:
        print("Op��o inv�lida! Tente novamente.")
        return

    print(f"\nVoc� escolheu: {jogador}")
    print(f"O computador escolheu: {computador}")

    if jogador == computador:
        print("Empate!")
    elif (jogador == "pedra" and computador == "tesoura") or \
         (jogador == "papel" and computador == "pedra") or \
         (jogador == "tesoura" and computador == "papel"):
        print("Voc� ganhou!")
    else:
        print("Voc� perdeu!")

def main():
    enquanto_jogar = True
    while enquanto_jogar:
        jogar()
        continuar = input("\nDeseja jogar novamente? (s/n): ").lower()
        if continuar != 's':
            enquanto_jogar = False
            print("Obrigado por jogar!")

if __name__ == "__main__":
    main()