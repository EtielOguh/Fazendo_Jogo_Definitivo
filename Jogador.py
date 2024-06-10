from random import randint
import Inimigo
from colorama import Fore

class Jogador:
    def __init__(self,nome):
        self.nome = nome
        self.zona = 1
        self.vida = 200
        self.vida_max = 200
        self.ataque = 20
        self.level = 1
        self.experiencia = 0
        self.exp_para_proximo_lvl = 50
        self.pocao_vida = 0
        self.inventario = []
        self.mao = []
    
    def jogador_vivo(self):
        return self.vida > 0
    
    def receber_dano(self, dano):
        self.vida -= dano
        print(f"{self.nome} recebeu {dano} de dano. Saúde atual: {self.vida}")
    
    def atacar_inimigo(self, inimigo):
        dano = randint(self.ataque -1, self.ataque + 5)
        if dano > inimigo.vida:
            dano = inimigo.vida
        inimigo.receber_dano(dano)
    
    def subir_nivel(self):
        self.level += 1
        self.exp_para_proximo_lvl *= 1.3
        self.ataque += 3
        self.vida_max += 20
        print(Fore.BLUE + f"{self.nome} subiu para o nível {self.level}!")

    def ganhar_experiencia(self, exp):
        self.experiencia += exp
        print(Fore.BLUE + f"{self.nome} ganhou {exp} pontos de experiência!")
        while self.experiencia >= self.exp_para_proximo_lvl:
            self.experiencia -= self.exp_para_proximo_lvl
            self.subir_nivel()
            self.resetar_player()
            print(f"Vida: {self.vida} \nAtaque: {self.ataque}")
    
    def expeciencia_ganha(jogador,inimigo):
        experiencia_recebida = 10 * inimigo.level
        jogador.ganhar_experiencia(experiencia_recebida)
    
    def resetar_player(self):
        self.vida = self.vida_max
    
    def mostrar_atributos(self):
        print(Fore.BLACK + f'Level: {self.level}', end=' ')
        print(Fore.BLACK + f'Dano: {self.ataque}', end= ' ')
        print(Fore.BLACK + f'Vida: {self.vida}')
    
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
        zona = int(input(Fore.LIGHTBLUE_EX + 'Selecione uma zona:' + '\n1: lvl 3-5 \n2: 6-8 \n4: 9-11 \n5: 12-13 \nSua escolha: '))
        jogador.zona = zona

