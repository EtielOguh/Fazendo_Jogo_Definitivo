from gc import callbacks
import pygame
from SpriteJogador import*
VERDE = (0, 255, 0)
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
CINZA = (100, 100, 100)

class Botao:
    def __init__(self, x, y, largura, altura, texto, cor_base, cor_hover, fonte):
        self.rect = pygame.Rect(x, y, largura, altura)
        self.texto = texto
        self.cor_base = cor_base
        self.cor_hover = cor_hover
        self.fonte = fonte

    def desenhar(self, tela):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(tela, self.cor_hover, self.rect)
        else:
            pygame.draw.rect(tela, self.cor_base, self.rect)
        texto_surface = self.fonte.render(self.texto, True, PRETO)
        texto_rect = texto_surface.get_rect(center=self.rect.center)
        tela.blit(texto_surface, texto_rect)

    def foi_clicado(self, pos_mouse):
        return self.rect.collidepoint(pos_mouse)