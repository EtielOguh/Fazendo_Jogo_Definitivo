from random import randint
import Inimigo
from colorama import Fore

class Jogador:
    def __init__(self):
        self.nome = 'Knight'
        self.zona = 1 
        self.vida = 300
        self.vida_max = 300
        self.ataque = 10
        self.level = 1
        self.experiencia = 0
        self.exp_para_proximo_lvl = 50
        self.pocao_vida = 0
        self.inventario = []
        self.mao = []

        self.pos_x = 100
        self.pos_y = 100

        # Velocidades de movimento
        self.velocidade_horizontal = 40
        self.velocidade_vertical = 40
    
    def mostrar_inventario(jogador):
        print('Inventário:')
        for i, item in enumerate(jogador.inventario):
            print(f'{i}: {item.nome} (Ataque: {item.ataque})')

    def equipar_item(self, indice): #Item equipado na mão
        if 0 <= indice < len(self.inventario):
            # Se já houver um item equipado, desequipe-o primeiro
            if self.mao:
                item_atual = self.mao.pop()
                self.ataque -= item_atual.ataque
                print(f'{item_atual.nome} foi desequipado!')
                
            # Equipar o novo item
            item = self.inventario[indice]
            self.mao.append(item)
            self.ataque += item.ataque
            print(f'{item.nome} foi equipado!')
        else:
            print("Índice inválido!")
    
    def selecionarZona(jogador):
        zona = int(input(Fore.LIGHTBLUE_EX + 'Selecione uma zona:' + '\n1: lvl 3-5 \n2: lvl 6-8 \n4: lvl 9-11 \n5: lvl 12-13 \nSua escolha: '))
        jogador.zona = zona

