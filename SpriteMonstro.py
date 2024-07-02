import pygame
from Inimigo import *
from SpriteInimigo import *
from Monstros import *
from Monstros import inimigo_escolhido
import os
import time
import math

BLACK = (0, 0, 0)
AZUL = (0,0,255)
VERDE = (0,255,0)
VERMELHO = (255,0,0)

class SpriteInimigo(pygame.sprite.Sprite):
    def __init__(self, inimigo, jogador):
        super().__init__()
        self.inimigo = inimigo
        self.respawn(jogador)  # Inicializa o inimigo ao criar a instância
        self.distancia_minima = 90
        self.velocidade = 2
        self.dano_recebido = 0
        self.tempo_dano = 0
        self.ultimo_ataque = time.time()  # Tempo do último ataque
        self.intervalo_ataque = 0.5  # Intervalo entre ataques em segundos

    def respawn(self, jogador):
        # Escolhe um novo inimigo
        self.inimigo = inimigo_escolhido(jogador)
        self.image = pygame.image.load(self.inimigo.sprite_path)
        novo_tamanho = (80, 80)
        self.image = pygame.transform.scale(self.image, novo_tamanho)
        self.rect = self.image.get_rect()
        largura_tela, altura_tela = 800, 600
        self.rect.x = 150
        self.rect.y = 450
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
        proporcao_vida = self.inimigo.vida / self.inimigo.vida_max
        largura_vida = barra_largura * proporcao_vida
        cor_barra = VERDE 
        cor_fundo = VERMELHO
        pygame.draw.rect(tela, cor_barra, (barra_x, barra_y, largura_vida, barra_altura))
        pygame.draw.rect(tela, cor_fundo, (barra_x + largura_vida, barra_y, barra_largura - largura_vida, barra_altura))


    def receber_dano(self, dano):
        self.inimigo.vida -= dano
        if self.inimigo.vida < 0:
            self.inimigo.vida = 0
        self.dano_recebido = dano
        self.tempo_dano = 30  # número de frames para exibir o dano
    
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
    
    def exibir_dano(self, tela):
        if self.tempo_dano > 0:
            texto_dano = f"-{self.dano_recebido}"
            fonte = pygame.font.SysFont(None, 24)
            texto_surface = fonte.render(texto_dano, True, (VERMELHO))
            tela.blit(texto_surface, (self.rect.x, self.rect.y - 30))
            self.tempo_dano -= 3