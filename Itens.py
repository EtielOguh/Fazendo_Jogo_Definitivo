from random import randint, choice

class Itens:
    
    def __init__(self,nome,dano):
        self.nome = nome
        self.dano = dano
    
    def dropar_item(itens):
        possiveis_itens = [
            Itens("Espada", 50, 0),
            Itens("Escudo", 10, 100),
            Itens("Poção", 0, 50),
            Itens("Arco", 30, 0)
    ]
        item_dropado = choice(possiveis_itens)