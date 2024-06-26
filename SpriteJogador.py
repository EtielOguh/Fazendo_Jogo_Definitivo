import pygame
from Inimigo import *
from SpriteMonstro import *
from Jogador import *
import os
import time
import math

BLACK = (0, 0, 0)
AZUL = (0,0,255)

class SpriteJogador(pygame.sprite.Sprite):
    def __init__(self,jogador):
        super().__init__()
        self.jogador = jogador
        self.image = pygame.image.load('AtaqueJogador/1.png') 
        novo_tamanho = (100 , 81)
        self.image = pygame.transform.scale(self.image, novo_tamanho)
        self.rect = self.image.get_rect() # Superfície do sprite (retângulo inicial)  # Obtém o retângulo associado à imagem
        self.pos_x_anterior = self.rect.x  # Variável para armazenar posição anterior
        self.pos_y_anterior = self.rect.y  # Variável para armazenar posição anterior
        self.imagensAtaque= []
        self.imagensAtaque.append(pygame.transform.scale(pygame.image.load('AtaqueJogador/1.png'), (novo_tamanho)))
        self.imagensAtaque.append(pygame.transform.scale(pygame.image.load('AtaqueJogador/2.png'), (novo_tamanho)))
        self.imagensAtaque.append(pygame.transform.scale(pygame.image.load('AtaqueJogador/3.png'), (novo_tamanho)))
        self.imagensAtaque.append(pygame.transform.scale(pygame.image.load('AtaqueJogador/4.png'), (novo_tamanho)))
        self.imagensAtaque.append(pygame.transform.scale(pygame.image.load('AtaqueJogador/5.png'), (novo_tamanho)))
        self.imagensAtaque.append(pygame.transform.scale(pygame.image.load('AtaqueJogador/6.png'), (novo_tamanho)))
        self.imagensAtaque.append(pygame.transform.scale(pygame.image.load('AtaqueJogador/7.png'), (novo_tamanho)))
        
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
        if self.atacando == False:
            self.atacando = True
            self.indice_ataque = 0
            self.contadorAtaque = 0
            self.image = self.imagensAtaque[self.indice_ataque]

    def update(self):
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

    def draw (self, tela):
        tela.blit(self.image, self.rect.topleft)
        self.barra_vida(tela)
    
    def barra_vida(self, tela):
        barra_largura = self.rect.width
        barra_altura = 5
        barra_x = self.rect.x
        barra_y = self.rect.y - barra_altura - 2

        proporcao_vida = self.jogador.vida / self.jogador.vida_max
        largura_vida = barra_largura * proporcao_vida

        cor_barra = (0, 255, 0)  # Verde
        cor_fundo = (255, 0, 0)  # Vermelho

        # Desenha a parte da vida preenchida
        pygame.draw.rect(tela, cor_barra, (barra_x, barra_y, largura_vida, barra_altura))
        # Desenha a parte da vida vazia
        pygame.draw.rect(tela, cor_fundo, (barra_x + largura_vida, barra_y, barra_largura - largura_vida, barra_altura))

    def receber_dano(self, dano):
        self.jogador.vida -= dano
        if self.jogador.vida < 0:
            self.jogador.vida = 0

    def jogador_vivo(self):
        return self.jogador.vida > 0
    
    def resetar_player(self):
        self.jogador.vida = self.jogador.vida_max
    
    def subir_nivel(self):
        self.jogador.level += 1
        self.jogador.exp_para_proximo_lvl *= 1.5
        self.jogador.ataque += 3
        self.jogador.vida_max += 20
        print(f"{self.jogador.nome} subiu para o nível {self.jogador.level}!")
    
    def ganhar_experiencia(self, inimigo):
        experiencia_recebida = 10 * inimigo.level
        self.jogador.experiencia += experiencia_recebida
        print(Fore.BLUE + f"{self.jogador.nome} ganhou {experiencia_recebida} pontos de experiência!")

        while self.jogador.experiencia >= self.jogador.exp_para_proximo_lvl:
            self.jogador.experiencia -= self.jogador.exp_para_proximo_lvl
            self.subir_nivel()
            self.resetar_player()
            print(f"Vida: {self.jogador.vida} \nAtaque: {self.jogador.ataque}")

    def atacar(self, inimigo_sprite, distancia_ataque):
        if self.checar_proximidade(inimigo_sprite, distancia_ataque):
            inimigo_sprite.receber_dano(self.jogador.ataque)
    
    def checar_proximidade(self, outro_sprite, distancia_ataque):
        distancia = math.sqrt((self.rect.centerx - outro_sprite.rect.centerx) ** 2 + (self.rect.centery - outro_sprite.rect.centery) ** 2)
        return distancia <= distancia_ataque

    def ganhar_pocao(self):
        self.jogador.pocao_vida += 1
        print(Fore.GREEN + 'Você recebeu uma poção!')
    
    def usar_pocao(self):
        if self.jogador.pocao_vida > 0:
            self.jogador.pocao_vida -= 1
            self.jogador.vida = min(self.jogador.vida + 40, self.jogador.vida_max)
            print(f'{self.jogador.nome} usou uma poção e restaurou sua vida para {self.jogador.vida}.')
        else:
            print(f'{self.jogador.nome} não tem poções disponíveis.')