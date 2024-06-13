from PararJogo import *
from Jogador import *
from random import randint
from Inimigo import *
from Itens import *
import time
from colorama import Fore

def Batalha():
    nome_jogador = input('Digite um nome: ')
    jogador0 = Jogador(nome_jogador)
    print(f"Boa jornada no JoHugo {nome_jogador}!")

    while jogador0.jogador_vivo():
        inimigo = Inimigo.inimigo_escolhido(jogador0)
        print(Fore.RED +'--------------------------------------------')
        print(Fore.RED +f'Inimigo: {inimigo.nome} Nivel {inimigo.level}')
        print(Fore.RED +'--------------------------------------------')
        while inimigo.inimigo_vivo() and jogador0.jogador_vivo():
            print(Fore.GREEN +"\nEscolha uma opção:")
            print(Fore.GREEN + "+-------------------------------------------------------+")
            print(Fore.GREEN +"| [A] Atacar [F] Fugir [P] Usar Poção [S] Parar o jogo  |")
            print(Fore.GREEN +"|        [E] Equipar item [Z] Selcionar Zona            |")
            print(Fore.GREEN +"+-------------------------------------------------------+")
            acao = input("Sua escolha: ")
            if acao in 'Aa':
                while inimigo.inimigo_vivo() and jogador0.jogador_vivo():
                    jogador0.atacar_inimigo(inimigo)
                    time.sleep(1)
                    if inimigo.inimigo_vivo():
                        inimigo.atacar_jogador(jogador0)
                    if not inimigo.inimigo_vivo():
                        print(Fore.RED +'-'*20)
                        print(Fore.RED +f'{inimigo.nome} Derrotado!')
                        jogador0.expeciencia_ganha(inimigo)
                        print(Fore.RED +'-'*20)
                        Item_dropado = Itens.dropar_item(inimigo)
                        Itens.adicionar_ao_inventario(jogador0, Item_dropado)
                        if random() <= 0.7:
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
                if len(jogador0.inventario) == 0:
                    print(Fore.YELLOW + 'Sem itens no inventário!')
                    break
                while True:
                    try:
                        jogador0.mostrar_inventario()
                        indice_item = int(input("\nDigite o índice do item a ser equipado: "))
                        jogador0.equipar_item(indice_item)
                        jogador0.inventario.pop(indice_item)
                        print(Fore.RED + '--------------------------------------------')
                        print(Fore.RED + f'Inimigo: {inimigo.nome} Nivel {inimigo.level}')
                        print(Fore.RED + '--------------------------------------------')
                        break
                    except ValueError:
                        print("\nEntrada inválida! Por favor, digite um número válido.")
            elif acao in 'pP':
                Itens.usar_pocao(jogador0)
                Itens.pocao_disponivel(jogador0)
                print(Fore.RED + '--------------------------------------------')
                print(Fore.RED + f'Inimigo: {inimigo.nome} Nivel {inimigo.level}')
                print(Fore.RED + '--------------------------------------------')
            elif acao in 'zZ':
                jogador0.selecionarZona()
                inimigo = Inimigo.inimigo_escolhido(jogador0)
                print(Fore.RED + '--------------------------------------------')
                print(Fore.RED + f'Inimigo: {inimigo.nome} Nivel {inimigo.level}')
                print(Fore.RED + '--------------------------------------------')
            else:
                print('Opção inválida!')
                    
    fim_de_jogo(jogador0)