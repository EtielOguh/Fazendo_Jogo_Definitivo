from PararJogo import *
from Jogador import *
from random import randint
from Inimigo import *
from Itens import *
import time

def Batalha():
    nome_jogador = input('Digite um nome: ')
    jogador0 = Jogador(nome_jogador)
    print(f"Seja feliz no mundo de JoHugo, {nome_jogador}!")

    while jogador0.jogador_vivo():
        inimigo = Inimigo.inimigo_escolhido(jogador0.level)
        print('--------------------------------------------')
        print(f'Inimigo: {inimigo.nome} Nivel {inimigo.level}')
        print('--------------------------------------------')
        while inimigo.inimigo_vivo() and jogador0.jogador_vivo():
            print("\nEscolha uma opção:")
            print("+-------------------------------------+")
            print("| [A] Atacar [F] Fugir [P] Usar Poção |")
            print("| [E] Equipar item [S] Parar o jogo   |")
            print("+-------------------------------------+")
            acao = input("Sua escolha: ")
            if acao in 'Aa':
                while inimigo.inimigo_vivo() and jogador0.jogador_vivo():
                    jogador0.atacar_inimigo(inimigo)
                    time.sleep(1)
                    if inimigo.inimigo_vivo():
                        inimigo.atacar_jogador(jogador0)
                    if not inimigo.inimigo_vivo():
                        print('-'*10)
                        print(f'{inimigo.nome} Derrotado!')
                        print('-'*10)
                        jogador0.expeciencia_ganha(inimigo)
                        Item_dropado = Itens.dropar_item(jogador0)
                        Itens.adicionar_ao_inventario(jogador0, Item_dropado)
                        if random() <= 0.6:
                            Itens.ganhar_pocao(jogador0)
                        jogador0.mostrar_atributos()
                    if not jogador0.jogador_vivo():
                        print('Fim de jogo!,você perdeu!')
                        break
            elif acao in 'Ff':
                print('Você fugiu!')
                break
            elif acao in 'sS':
                parar_jogo() #Função de parar o jogo
            elif acao in 'Ee':
                while True:
                    try:
                        jogador0.mostrar_inventario()
                        indice_item = int(input("\nDigite o índice do item a ser equipado: "))
                        jogador0.equipar_item(indice_item)
                        jogador0.inventario.pop(indice_item)
                        break
                    except ValueError:
                        print("\nEntrada inválida! Por favor, digite um número válido.")
            elif acao in 'pP':
                Itens.usar_pocao(jogador0)
                Itens.pocao_disponivel(jogador0) 
                    
    fim_de_jogo(jogador0)