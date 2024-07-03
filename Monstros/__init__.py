from Inimigo import *
from random import choice
from .Dragon import Dragon
from .Lanceiro import Lanceiro
from .Gosma import Gosma
from .Demon import Demon
from .Curandeira import Curandeira

__all__ = ["Inimigo", "Gosma", "Dragon", "Lanceiro", "Demon", "Curandeira"]

def inimigo_escolhido(jogador):
    inimigos_por_zona = [
         [Gosma(), Lanceiro(), Curandeira()],
         [Dragon(), Demon(), Curandeira()]
         # Adicione mais listas para outras zonas
    ]
    
    if 0 < jogador.zona <= len(inimigos_por_zona):
        inimigos_disponiveis = inimigos_por_zona[jogador.zona - 1]
    else:
        raise ValueError(f"Zona inválida: {jogador.zona}")
    
    inimigo_escolhido = choice(inimigos_disponiveis)
    return inimigo_escolhido
