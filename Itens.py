from random import randint, choice

class Itens:
    
    def __init__(self,nome,ataque):
        self.nome = nome
        self.ataque = ataque
    
    def dropar_item(jogador):
        possiveis_itens = [
            Itens('Espada de Madeira', 10),
            Itens('Espada de Pedra', 15),
            Itens('Espada de Ferro', 20),
            Itens('Espada de Ouro', 25),
            Itens('Espada de Esmeralda', 30),
            Itens('Espada de Diamante', 40),
            Itens('Espada Angelical', 70)
    ]
        if jogador.level <= 1:
            itemDropado = choice(possiveis_itens[0:])
        if jogador.level <= 3:
            itemDropado = choice(possiveis_itens[:3])
        if jogador.level <= 5:
            itemDropado = choice(possiveis_itens[3:4])
        if jogador.level <= 9:
            itemDropado = choice(possiveis_itens[4:5])
        else:
            itemDropado = choice(possiveis_itens)
        
        print(possiveis_itens)
        print(itemDropado.nome)
        print(f'Você dropou {itemDropado.nome} with {itemDropado.ataque} damage')   
        return itemDropado

    def adicionar_ao_inventario(jogador, item):
        if item not in jogador.inventario:
            jogador.inventario.append(item)
            print(f'{item.nome} foi adicionado ao inventário!')