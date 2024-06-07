from random import randint, choice
from Jogador import *

class Inimigo:
    def __init__(self, nome, vida, ataque, level):
        self.nome = nome
        self.level = level
        self.vida = vida
        self.ataque = ataque
    
    def inimigo_vivo(self):
        return self.vida > 0

    def receber_dano(self, dano):
        self.vida -= dano
        print(f"{self.nome} recebeu {dano} de dano. Saúde atual: {self.vida}")

    def atacar_jogador(self, jogador):
        dano = randint(self.ataque - 1, self.ataque + 5)
        if dano > jogador.vida:
            dano = jogador.vida
        jogador.receber_dano(dano)
    
    def inimigo_escolhido(level_jogador):
        mobs = [
            Inimigo('Besouro Carniçal', 40, 8, 1), # 0
            Inimigo('Lagarto Sombrio', 45, 10, 2), # 1
            Inimigo('Morcego Vampírico', 50, 15, 3), # 2
            Inimigo('Aranha de Gelo', 55, 18, 4), # 3
            Inimigo('Corvo Infernal', 60, 20, 5), # 4
            Inimigo('Serpente de Fogo', 65, 23, 6), # 5  
            Inimigo('Urso Espectral', 75, 25, 7), # 6
            Inimigo('Leão Fantasma', 80, 28, 8), # 7
            Inimigo('Falcão Tempestuoso', 85, 30, 9), # 8 
            Inimigo('Lobo solitário', 90, 38, 10), # 9
            Inimigo('Gorila Mutante', 95, 40, 11), # 10
            Inimigo('Tigre das Sombras', 100, 45, 12), # 11 
            Inimigo('Dragão de Cristal', 125, 50, 13), # 12 
            Inimigo('DEMON', 500, 100, 14), #13
        ]

        pot_xp_mob = Inimigo('Rato Espreitador', 50, 1, 1 )    # Mob fraco para poção
    
        if level_jogador < 2:
            inimigos_disponiveis = mobs[:2]  # 0,1
        elif level_jogador < 4:
             inimigos_disponiveis = mobs[2:5]  # 2,3,4
        elif level_jogador < 7:
             inimigos_disponiveis = mobs[5:9] # 5,6,7,8
        elif level_jogador < 10:
            inimigos_disponiveis = mobs[9:13] # 9,10,11,12
        else:
            inimigos_disponiveis = mobs[11:14] # 11,12,13
        
        inimigos_disponiveis.append(pot_xp_mob)

        inimigo_escolhido = choice(inimigos_disponiveis)
        
        return inimigo_escolhido
