def fim_de_jogo(jogador):
    print("\nFim de jogo!")
    print(f"Nível final: {jogador.level}")
    print(f"Saúde final: {jogador.vida}")
    print(f"Ataque final: {jogador.ataque}")

def parar_jogo():
    decisao = input("Sair do jogo? [S/N]")
    if decisao.lower() in "sS":
        print("Saindo do jogo...")
        exit()
    else:
        print("Continuando o jogo.")