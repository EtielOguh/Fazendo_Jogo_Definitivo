import pygame
import sys
from SpriteJogador import *
from Jogador import *
from Inimigo import *
from SpriteMonstro import *

# Definição de cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

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
        self.inimigo = Inimigo('Demon', 50,5,1) #nome,vida,ataque,lvl
        
        # Criando um sprite
        self.jogadorSprite = SpriteJogador(self.jogador)
        self.inimigoSprite = SpriteInimigo(self.inimigo)

        # Criando um grupo de sprites e adicionando o sprite criado
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.jogadorSprite, self.inimigoSprite)
        

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
                        self.jogadorSprite.iniciar_ataque()
                        self.jogadorSprite.atacar(self.inimigoSprite)
                        self.inimigoSprite.atacarJogador(self.jogadorSprite)
            # Atualizações
            self.all_sprites.update()

            if not self.inimigoSprite.alive():
                self.jogadorSprite.ganhar_experiencia(self.inimigo)
                self.jogadorSprite.resetar_player()
                self.inimigoSprite.respawn()
                self.all_sprites.add(self.inimigoSprite)
            
            if not self.jogadorSprite.jogador_vivo():
                sys.exit()
            
            # Desenho na tela
            self.screen.fill(BLACK)  # preenche a tela com a cor preta
            self.all_sprites.draw(self.screen)  # desenha todos os sprites no grupo na tela

            self.inimigoSprite.draw(self.screen)
            self.jogadorSprite.draw(self.screen)

            pygame.display.flip()  # atualiza a tela

            clock.tick(20)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    jogo = Tela()
    jogo.Run()