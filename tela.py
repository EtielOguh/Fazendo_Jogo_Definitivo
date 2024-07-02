import pygame
import sys
from Monstros import *
from Monstros import inimigo_escolhido
from SpriteJogador import *
from Jogador import *
from SpriteMonstro import *
from Botao import *
from Inimigo import *

# Definição de cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0,0,255)
GREEN = (0,255,0)

class Tela:
    def __init__(self):
        # Inicialização do Pygame
        pygame.init()
        # Configuração da tela
        self.largura, self.altura = 1280, 720
        self.screen = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption("Jogo")
        # Carregar a imagem de fundo
        self.imagem_fundo = pygame.image.load("Fundo/Fundo.png")
        self.imagem_fundo = pygame.transform.scale(self.imagem_fundo, (self.largura, self.altura))
        #Criando Jogador
        self.jogador = Jogador()
        self.inimigo = inimigo_escolhido(self.jogador)
        # Criando um sprite
        self.inimigoSprite = SpriteInimigo(self.inimigo, self.jogador)
        self.jogadorSprite = SpriteJogador(self.jogador)
        # Criando um grupo de sprites e adicionando o sprite criado
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.jogadorSprite, self.inimigoSprite)
        #Fonte
        self.fonte = pygame.font.SysFont(None, 18)
        self.fonte2 = pygame.font.SysFont(None, 30)
        fonte_botao = pygame.font.SysFont(None, 20) 
        # Botões
        self.botao = Botao(130, 670, 80, 40, "Troca Zona", BRANCO, CINZA, fonte_botao,"zona")
        self.botao_atacar = Botao(30, 670, 80, 40, "Voltar Zona", BRANCO, CINZA, fonte_botao,"zona1")

    def Run(self):
        botoes = [self.botao, self.botao_atacar]
        # Loop principal do jogo
        running = True
        clock = pygame.time.Clock()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # Verificar eventos de teclado para movimento do jogador
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.jogadorSprite.mover_horizontal(-1)
                    elif event.key == pygame.K_RIGHT:
                        self.jogadorSprite.mover_horizontal(1)
                    elif event.key == pygame.K_UP:
                        self.jogadorSprite.mover_vertical(-1)
                    elif event.key == pygame.K_DOWN:
                        self.jogadorSprite.mover_vertical(1)
                    elif event.key == pygame.K_f:
                        distancia_ataque = 150  # Defina a distância de ataque adequada
                        self.jogadorSprite.iniciar_ataque()
                        self.jogadorSprite.atacar(self.inimigoSprite, distancia_ataque)
                    elif event.key == pygame.K_d:
                        self.jogadorSprite.usar_pocao()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    distancia_ataque = 150
                    for botao in botoes:
                        if botao.foi_clicado(event.pos):
                            if botao.id == "zona":
                                custo = 150
                                if self.jogadorSprite.jogador.dinheiro >= custo:
                                    self.jogadorSprite.jogador.dinheiro -= custo
                                    if self.jogadorSprite.jogador.zona != 2:
                                        self.jogadorSprite.jogador.zona += 1
                                        self.inimigoSprite.respawn(self.jogador)
                            elif botao.id == "zona1":
                                if self.jogadorSprite.jogador.zona > 1:
                                    self.jogadorSprite.jogador.zona -= 1
                                    self.inimigoSprite.respawn(self.jogador)

            self.inimigoSprite.seguir_jogador(self.jogadorSprite, 90)
            # Atualizações
            self.all_sprites.update()

            if not self.inimigoSprite.inimigo_vivo():
                self.jogadorSprite.ganharDinheiro(self.inimigo)
                self.jogadorSprite.ganhar_experiencia(self.inimigo)
                self.jogadorSprite.ganhar_pocao()
                self.inimigoSprite.respawn(self.jogador)
                self.all_sprites.add(self.inimigoSprite)
                
            if not self.jogadorSprite.jogador_vivo():
                sys.exit()
            
            # Desenho na tela
            self.screen.blit(self.imagem_fundo, (0, 0))
            self.all_sprites.draw(self.screen)  # desenha todos os sprites no grupo na tela

            self.jogadorSprite.exibir_dano(self.screen)
            self.inimigoSprite.exibir_dano(self.screen)

            self.desenhar_barra_experiencia()

            self.inimigoSprite.draw(self.screen)
            self.jogadorSprite.draw(self.screen)

            for botao in botoes:
                botao.desenhar(self.screen)


            pygame.display.flip()  # atualiza a tela

            clock.tick(60)

        pygame.quit()
        sys.exit()

    def desenhar_barra_experiencia(self): # tem mais coisa que somente exp
        # Calcula a largura da barra de experiência proporcional à experiência atual do jogador
        largura_barra = 180
        proporcao_experiencia = self.jogador.experiencia / self.jogador.exp_para_proximo_lvl
        largura_atual = int(largura_barra * proporcao_experiencia)

        # Desenha a barra de fundo
        pygame.draw.rect(self.screen, WHITE, (20, 40, largura_barra, 15))
        # Desenha a barra de experiência atual
        pygame.draw.rect(self.screen, GREEN, (20, 40, largura_atual, 15))

        # Desenha o texto indicando a experiência atual e necessária para o próximo nível
        texto_exp = f"XP: {self.jogador.experiencia:.1f}/{self.jogador.exp_para_proximo_lvl:.1f}"
        texto_LVL = f"LVL: {self.jogador.level}"
        texto_pot = f"POT: {self.jogador.pocao_vida}"
        texto_Dinheiro = f"DINHEIRO: {self.jogador.dinheiro}"
        texto_telaZonaJogador = f"Zona Atual: {self.jogador.zona}"
        texto_surface = self.fonte.render(texto_exp, True, WHITE)
        texto_telalvl = self.fonte.render(texto_LVL, True, WHITE)
        texto_telapot = self.fonte2.render(texto_pot, True, BLACK)
        texto_telazona = self.fonte2.render(texto_telaZonaJogador, True, BLACK)
        texto_telaDinheiro = self.fonte2.render(texto_Dinheiro, True, BLACK)
        self.screen.blit(texto_surface, (20, 58))
        self.screen.blit(texto_telalvl, (210, 43))
        self.screen.blit(texto_telapot, (1150, 18))
        self.screen.blit(texto_telazona, (900, 18))
        self.screen.blit(texto_telaDinheiro, (700, 18))

if __name__ == "__main__":
    jogo = Tela()
    jogo.Run()