from random import randint, choice
from Jogador import *

class Inimigo:
    def __init__(self, nome, nivel, ataque, vida, vida_max, sprite_path):
        self.nome = nome
        self.nivel = nivel
        self.ataque = ataque
        self.vida = vida
        self.vida_max = vida_max
        self.sprite_path = sprite_path