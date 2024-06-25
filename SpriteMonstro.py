import pygame
from Inimigo import *
import os
import time

BLACK = (0, 0, 0)
AZUL = (0,0,255)

class SpriteInimigo(pygame.sprite.Sprite):
    def __init__(self, inimigo):
        super().__init__()
        self.inimigo = inimigo
        self.image = pygame.image.load('SpriteInimigo/Monstro.png')
        novo_tamanho = (60, 60)
        self.image = pygame.transform.scale(self.image, novo_tamanho)
        self.rect = self.image.get_rect()
        largura_tela, altura_tela = 800, 600    
        self.pos_x = randint(0, largura_tela - self.rect.width)
        self.pos_y = randint(0, altura_tela - self.rect.height)
        self.rect.topleft = (self.pos_x, self.pos_y)
        self.vida_max = 300
        self.vida_atual = self.inimigo.vida # Pega a instancia do inimigo criado

    def update():
        pass

    def draw (self, tela):
        tela.blit(self.image, self.rect.topleft)
        self.barra_vida(tela)
    
    def barra_vida(self, tela):
        barra_largura = self.rect.width
        barra_altura = 5
        barra_x = self.rect.x
        barra_y = self.rect.y
        barra_y = self.rect.y - barra_altura - 2

        preencher = (0,255,0)
        esvaziar = (255,0,0)

        preencher_barra = int(barra_largura * (self.vida_atual / self.vida_max))
        pygame.draw.rect(tela,preencher,(barra_x, barra_y, preencher_barra, barra_altura))
        pygame.draw.rect(tela,esvaziar, (barra_x + preencher_barra, barra_y, barra_largura - preencher_barra, barra_altura))

