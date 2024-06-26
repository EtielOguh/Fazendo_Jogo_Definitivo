import pygame
from Inimigo import *
import os
import time
import math

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
        self.distancia_minima = 90
        self.velocidade = 2
        self.inimigo.vida = self.inimigo.vida_max
        self.ultimo_ataque = time.time()  # Tempo do último ataque
        self.intervalo_ataque = 0.5  # Intervalo entre ataques em segundos
        # Pega a instancia do inimigo criado
        self.respawn()
    
    def respawn(self):
        largura_tela, altura_tela = 800, 600
        self.rect.x = randint(20, largura_tela - self.rect.width)
        self.rect.y = randint(20, altura_tela - self.rect.height)
        self.inimigo.vida = self.inimigo.vida_max
    
    def inimigo_vivo(self):
        return self.inimigo.vida > 0
    
    def update(self):
        if self.inimigo.vida <= 0:
            self.kill()

    def draw (self, tela):
        tela.blit(self.image, self.rect.topleft)
        self.barra_vida(tela)
    
    def barra_vida(self, tela):
        barra_largura = self.rect.width
        barra_altura = 5
        barra_x = self.rect.x
        barra_y = self.rect.y
        barra_y = self.rect.y - barra_altura - 2
        # if proporcao_vida > 0.5:
        #     cor_barra = (0, 255, 0)  # Verde
        # elif proporcao_vida > 0.2:
        #     cor_barra = (255, 255, 0)  # Amarelo
        # else:
        #     cor_barra = (255, 0, 0)  # Vermelho

        proporcao_vida = self.inimigo.vida / self.inimigo.vida_max
        largura_vida = barra_largura * proporcao_vida

        cor_barra = (0, 255, 0)  # Verde
        cor_fundo = (255, 0, 0)  # Vermelho

        # Desenha a parte da vida preenchida
        pygame.draw.rect(tela, cor_barra, (barra_x, barra_y, largura_vida, barra_altura))
        # Desenha a parte da vida vazia
        pygame.draw.rect(tela, cor_fundo, (barra_x + largura_vida, barra_y, barra_largura - largura_vida, barra_altura))

        preencher = (0,255,0)
        esvaziar = (255,0,0)
        # pygame.draw.rect(tela, cor_barra, (barra_x, barra_y, barra_largura, barra_altura))
        #preencher_barra = int(barra_largura * (self.vida_atual / self.vida_max))
        #pygame.draw.rect(tela,preencher,(barra_x, barra_y, preencher_barra, barra_altura))
        #pygame.draw.rect(tela,esvaziar, (barra_x + preencher_barra, barra_y, barra_largura - preencher_barra, barra_altura))


    def receber_dano(self, dano):
        self.inimigo.vida -= dano
        if self.inimigo.vida < 0:
            self.inimigo.vida = 0
    
    def atacarJogador(self, jogador_sprite, distancia_ataque):
        agora = time.time()
        if self.checar_proximidade(jogador_sprite, distancia_ataque) and agora - self.ultimo_ataque >= self.intervalo_ataque:
            jogador_sprite.receber_dano(self.inimigo.ataque)
            self.ultimo_ataque = agora

    def checar_proximidade(self, outro_sprite, distancia_ataque):
        distancia = math.sqrt((self.rect.centerx - outro_sprite.rect.centerx) ** 2 + (self.rect.centery - outro_sprite.rect.centery) ** 2)
        return distancia <= distancia_ataque

    def seguir_jogador(self, jogador_sprite, distancia_ataque):
        dx, dy = jogador_sprite.rect.centerx - self.rect.centerx, jogador_sprite.rect.centery - self.rect.centery
        dist = math.hypot(dx, dy)
        if dist > self.distancia_minima:
            dx, dy = dx / dist, dy / dist  # Normaliza o vetor de direção
            self.rect.x += dx * self.velocidade
            self.rect.y += dy * self.velocidade
        if self.checar_proximidade(jogador_sprite, distancia_ataque):
            self.atacarJogador(jogador_sprite, distancia_ataque)
    