import pygame
import sys
from SpriteJogador import *
from Jogador import *
from SpriteMonstro import *
from Botao import *
from Inimigo import *

# Definição de cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0,0,255)

class Tela:
    def __init__(self):
        # Inicialização do Pygame
        pygame.init()
        # Configuração da tela
        self.largura, self.altura = 800, 600
        self.screen = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption("Jogo")
        #Criando Jogador
        self.jogador = Jogador()
        self.inimigo = Inimigo() #nome,vida,ataque,lvl
        # Criando um sprite
        self.inimigoSprite = SpriteInimigo(self.inimigo)
        self.jogadorSprite = SpriteJogador(self.jogador)
        # Criando um grupo de sprites e adicionando o sprite criado
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.jogadorSprite, self.inimigoSprite)
        #Fonte
        self.fonte = pygame.font.SysFont(None, 18)
        self.fonte2 = pygame.font.SysFont(None, 30)
        fonte_botao = pygame.font.SysFont(None, 36) 
        # Botões
        self.botao = Botao(300, 500, 200, 50, "Usar Poção", BRANCO, CINZA, fonte_botao)

    def Run(self):
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
                    if self.botao.foi_clicado(event.pos):
                        self.jogadorSprite.usar_pocao()  # Verifica se o botão foi clicado

            self.inimigoSprite.seguir_jogador(self.jogadorSprite, 90)
            # Atualizações
            self.all_sprites.update()

            if not self.inimigoSprite.alive():
                self.jogadorSprite.ganhar_experiencia(self.inimigo)
                self.inimigoSprite.respawn()
                self.jogadorSprite.ganhar_pocao()
                self.all_sprites.add(self.inimigoSprite)
            
            if not self.jogadorSprite.jogador_vivo():
                sys.exit()
            
            # Desenho na tela
            self.screen.fill(BLACK)  # preenche a tela com a cor preta
            self.all_sprites.draw(self.screen)  # desenha todos os sprites no grupo na tela

            self.jogadorSprite.exibir_dano(self.screen)
            self.inimigoSprite.exibir_dano(self.screen)

            self.desenhar_barra_experiencia()

            self.inimigoSprite.draw(self.screen)
            self.jogadorSprite.draw(self.screen)

            self.botao.desenhar(self.screen)

            pygame.display.flip()  # atualiza a tela

            clock.tick(60)

        pygame.quit()
        sys.exit()

    def desenhar_barra_experiencia(self):
        # Calcula a largura da barra de experiência proporcional à experiência atual do jogador
        largura_barra = 100
        proporcao_experiencia = self.jogador.experiencia / self.jogador.exp_para_proximo_lvl
        largura_atual = int(largura_barra * proporcao_experiencia)

        # Desenha a barra de fundo
        pygame.draw.rect(self.screen, WHITE, (20, 20, largura_barra, 5))
        # Desenha a barra de experiência atual
        pygame.draw.rect(self.screen, BLUE, (20, 20, largura_atual, 5))

        # Desenha o texto indicando a experiência atual e necessária para o próximo nível
        texto_exp = f"XP: {self.jogador.experiencia:.1f}/{self.jogador.exp_para_proximo_lvl:.1f}"
        texto_LVL = f"LVL: {self.jogador.level}"
        texto_pot = f"POT: {self.jogador.pocao_vida}"
        texto_surface = self.fonte.render(texto_exp, True, WHITE)
        texto_telalvl = self.fonte.render(texto_LVL, True, WHITE)
        texto_telapot = self.fonte2.render(texto_pot, True, WHITE)
        self.screen.blit(texto_surface, (20, 30))
        self.screen.blit(texto_telalvl, (125, 18))
        self.screen.blit(texto_telapot, (700, 18))

if __name__ == "__main__":
    jogo = Tela()
    jogo.Run()