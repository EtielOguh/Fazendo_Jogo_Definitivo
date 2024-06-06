from random import randint, choice, random

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
        chance_de_drop = 0.3

        if random() > chance_de_drop:
            print('Nenhum item foi dropado.')
            return None


        if jogador.level >= 1:
            itemDropado = choice(possiveis_itens[:1])
        if jogador.level >= 3:
            itemDropado = choice(possiveis_itens[:3])
        if jogador.level >=5:
            itemDropado = choice(possiveis_itens[3:4])
        if jogador.level >= 10:
            itemDropado = choice(possiveis_itens[4:5])
        
        print(f'Você dropou {itemDropado.nome} with {itemDropado.ataque} damage')   
        return itemDropado

    def adicionar_ao_inventario(jogador, item):
        if item is None:
            return
        if not any(i.nome == item.nome for i in jogador.inventario):
            jogador.inventario.append(item)
            print(f'{item.nome} foi adicionado ao inventário!')
        else:
            print(f'{item.nome} já está no inventário.')