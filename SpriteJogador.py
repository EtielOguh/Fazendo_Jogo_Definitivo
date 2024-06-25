import pygame
from Jogador import *
import os
import time

BLACK = (0, 0, 0)
AZUL = (0,0,255)

class SpriteJogador(pygame.sprite.Sprite):
    def __init__(self,jogador):
        super().__init__()
        self.jogador = jogador
        self.image = pygame.image.load('SpritesJogador/1.png')  # Superfície do sprite (retângulo inicial)
        self.rect = self.image.get_rect()  # Obtém o retângulo associado à imagem

        self.imagensAtaque= []
        self.imagensAtaque.append(pygame.image.load('AtaqueJogador/1.png'))
        self.imagensAtaque.append(pygame.image.load('AtaqueJogador/2.png'))
        self.imagensAtaque.append(pygame.image.load('AtaqueJogador/3.png'))
        self.imagensAtaque.append(pygame.image.load('AtaqueJogador/4.png'))
        self.imagensAtaque.append(pygame.image.load('AtaqueJogador/5.png'))
        self.imagensAtaque.append(pygame.image.load('AtaqueJogador/6.png'))
        self.imagensAtaque.append(pygame.image.load('AtaqueJogador/7.png'))
        
        self.atacando = False
        self.indice_ataque = 0
        self.duracaoAtaque = 1
        self.contadorAtaque = 0
    
    def atualizar_animacao_ataque(self):
        if self.contadorAtaque >= self.duracaoAtaque:
            self.indice_ataque += 1
            self.contadorAtaque = 0

            if self.indice_ataque >= len(self.imagensAtaque):
                self.atacando = False
                self.image = self.imagensAtaque[0]
                self.indice_ataque = 0
            else:
                self.image = self.imagensAtaque[self.indice_ataque]
        else:
            self.contadorAtaque += 1

    def iniciar_ataque(self):
        print('Entrou aqui')
        if self.atacando == False:
            self.atacando = True
            self.indice_ataque = 0
            self.contadorAtaque = 0
            self.image = self.imagensAtaque[self.indice_ataque]

    def update(self):
        print('Aqui Update')
        if self.atacando:
            # time.sleep(0.5)
            self.atualizar_animacao_ataque()
        # Atualização da posição do sprite baseada na posição do jogador
        self.rect.centerx = self.jogador.pos_x  # Definir posição x do jogador na tela
        self.rect.centery = self.jogador.pos_y  # Definir posição y do jogador na tela

    def mover_horizontal(self, direcao):
        self.jogador.pos_x += direcao * self.jogador.velocidade_horizontal

    def mover_vertical(self, direcao):
        self.jogador.pos_y += direcao * self.jogador.velocidade_vertical

    def atacar(self, inimigo_sprite):
        if self.rect.colliderect(inimigo_sprite.rect):
            inimigo_sprite.receber_dano(self.jogador.ataque)

    def draw (self, tela):
        tela.blit(self.image, self.rect.topleft)
        self.barra_vida(tela)
    
    def barra_vida(self, tela):
        barra_largura = self.rect.width
        barra_altura = 5
        barra_x = self.rect.x
        barra_y = self.rect.y
        barra_y = self.rect.y - barra_altura - 2

        proporcao_vida = self.jogador.vida / self.jogador.vida_max
        if proporcao_vida > 0.5:
            cor_barra = (0, 255, 0)  # Verde
        elif proporcao_vida > 0.2:
            cor_barra = (255, 255, 0)  # Amarelo
        else:
            cor_barra = (255, 0, 0)  # Vermelho

        preencher = (0,255,0)
        esvaziar = (255,0,0)
        pygame.draw.rect(tela, cor_barra, (barra_x, barra_y, barra_largura, barra_altura))
    
    def receber_dano(self, dano):
        self.jogador.vida -= dano
        if self.jogador.vida < 0:
            self.jogador.vida = 0

    def jogador_vivo(self):
        return self.jogador.vida > 0
    
    def resetar_player(self):
        self.jogador.vida = self.jogador.vida_max
    
