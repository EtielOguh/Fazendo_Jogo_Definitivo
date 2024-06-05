from random import randint, choice

class Itens:
    
    def __init__(self,nome,ataque):
        self.nome = nome
        self.ataque = ataque
    
    def dropar_item():
        possiveis_itens = [
            Itens("Espada", 50),
            Itens("Foice", 10),
            Itens("Arco", 30)
    ]
        item_dropado = choice(possiveis_itens)
        print(f'Você dropou {item_dropado.nome} with {item_dropado.ataque} damage')
        return item_dropado

    def adicionar_ao_inventario(self, item):
        self.inventario.append(item)
        print(f'{item.nome} foi adicionado ao inventário!')