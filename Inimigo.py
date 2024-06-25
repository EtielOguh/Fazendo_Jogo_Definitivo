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
    
    def inimigo_escolhido(jogador):
        # Lista de listas para armazenar os inimigos por zona
        inimigos_por_zona = [
            [Inimigo('Besouro Carniçal', 50, 8, 1), Inimigo('Lagarto Sombrio', 60, 10, 1), Inimigo('Rato Espreitador', 50, 1, 1)],
            [Inimigo('Morcego Vampírico', 65, 15, 3), Inimigo('Aranha de Gelo', 70, 18, 4), Inimigo('Corvo Infernal', 75, 20, 5)],
            [Inimigo('Serpente de Fogo', 80, 23, 6), Inimigo('Urso Espectral', 90, 25, 7), Inimigo('Leão Fantasma', 100, 28, 8)],
            [Inimigo('Falcão Tempestuoso', 110, 30, 9), Inimigo('Lobo solitário', 120, 38, 10), Inimigo('Gorila Mutante', 150, 40, 11)],
            [Inimigo('Tigre das Sombras', 170, 45, 12), Inimigo('Dragão de Cristal', 200, 50, 13)],
        ]
        # Obter inimigos disponíveis
        if 0 < jogador.zona <= len(inimigos_por_zona):
            inimigos_disponiveis = inimigos_por_zona[jogador.zona - 1]
        else:
            raise ValueError(f"Zona inválida: {jogador.zona}")
        
        inimigo_escolhido = choice(inimigos_disponiveis)

        return inimigo_escolhido
