from random import randint
import Inimigo
from colorama import Fore

class Jogador:
    def __init__(self):
        #Informações jogador
        self.nome = 'Knight'
        self.zona = 1
        self.vida = 200
        self.vida_max = 200
        self.ataque = 30
        self.level = 1
        self.experiencia = 0
        self.exp_para_proximo_lvl = 50
        self.pocao_vida = 0
        self.dinheiro = 0
        self.inventario = []
        self.mao = []
        #Posição inicial
        self.pos_x = 650
        self.pos_y = 500
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

