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
            Inimigo('Goblin', 20, 8, 1),        # Nível baixo
            Inimigo('Orc', 40, 16, 2),          # Nível médio
            Inimigo('Troll', 60, 20, 3),        # Nível alto
            Inimigo('Dragão', 100, 24, 4),      # Nível muito alto
            Inimigo('Demon', 150, 28, 5),       # Extreme
            Inimigo('Demon God', 250, 30, 6),   # Fodeu
        ]

        pot_xp_mob = Inimigo('Pot/xp Mob', 50, 1, 1 )    # Mob fraco para poção
    
        if level_jogador < 3:
            inimigos_disponiveis = mobs[:2]  # Escolhe entre Goblin e Orc
        elif level_jogador < 5:
             inimigos_disponiveis = mobs[1:3]  # Escolhe entre Orc e Troll
        else:
             inimigos_disponiveis = mobs[3:] # Escolhe entre Troll e Dragão
        
        inimigos_disponiveis.append(pot_xp_mob)

        inimigo_escolhido = choice(inimigos_disponiveis)
        
        return inimigo_escolhido
