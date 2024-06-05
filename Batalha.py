from PararJogo import *
from Jogador import *
from random import randint
from Inimigo import *
from Itens import *

Mochila = []

def Batalha():
    nome_jogador = input('Digite um nome: ')
    jogador0 = Jogador(nome_jogador)
    print(f"Bem-vindo ao jogo RPG, {nome_jogador}!")

    while jogador0.jogador_vivo():
        inimigo = Inimigo.inimigo_escolhido(jogador0.level)
        print('-'*20)
        print(f'Inimigo: {inimigo.nome} Nivel {inimigo.level}')
        print('-'*20)
        while inimigo.inimigo_vivo() and jogador0.jogador_vivo():
            acao = input('\nEscolha uma opção: \n[A] Atacar\n[F] Fugir\n[P] Usar poção \n[S] Parar o jogo\nSua escolha: ')
            if acao in 'Aa':
                jogador0.atacar_inimigo(inimigo)
                if inimigo.inimigo_vivo():
                    inimigo.atacar_jogador(jogador0)
                if not inimigo.inimigo_vivo():
                    print(f'Você derrotou o MOB {inimigo.nome}')
                    jogador0.expeciencia_ganha(inimigo)
                    Item_dropado = Itens.dropar_item()
                    Itens.adicionar_ao_inventario(jogador0, Item_dropado)
                    jogador0.mostrar_atributos()
                    if not jogador0.jogador_vivo():
                        print('Fim de jogo!,você perdeu!')
                        break
            elif acao in 'Ff':
                print('Você fugiu!')
                break
            elif acao in 'sS':
                parar_jogo() #Função de parar o jogo
                    
    fim_de_jogo(jogador0)