from random import randint
import Inimigo

class Jogador:
    def __init__(self,nome):
        self.nome = nome
        self.vida = 100
        self.vida_max = 100
        self.ataque = 10
        self.level = 1
        self.experiencia = 0
        self.exp_para_proximo_lvl = 50
        self.pocao_vida = 0
        self.inventario = []
        self.mao = []
    
    def jogador_vivo(self):
        return self.vida > 0
    
    def receber_dano(self, dano):
        self.vida -= dano
        print(f"{self.nome} recebeu {dano} de dano. Saúde atual: {self.vida}")
    
    def atacar_inimigo(self, inimigo):
        dano = randint(self.ataque -1, self.ataque + 5)
        if dano > inimigo.vida:
            dano = inimigo.vida
        inimigo.receber_dano(dano)
    
    def subir_nivel(self):
        self.level += 1
        self.exp_para_proximo_lvl *= 2
        self.ataque += 6
        self.vida_max += 10
        print(f"{self.nome} subiu para o nível {self.level}!")

    def ganhar_experiencia(self, exp):
        self.experiencia += exp
        print(f"{self.nome} ganhou {exp} pontos de experiência.\nSua vida atual é de {self.vida}")
        if self.experiencia >= self.exp_para_proximo_lvl:
            self.subir_nivel()
            self.resetar_player()
            print(f"Vida: {self.vida} \nAtaque: {self.ataque}")
    
    def expeciencia_ganha(jogador,inimigo):
        experiencia_recebida = 10 * inimigo.level
        jogador.ganhar_experiencia(experiencia_recebida)
    
    def resetar_player(self):
        self.vida = self.vida_max
    
    def mostrar_atributos(self):
        print(f'Level do Jogador: {self.level}')
        print(f'Dano do Jogador: {self.ataque}')
        print(f'Vida do Jogador: {self.vida}')
        print('Inventário:')
        for i, item in enumerate(self.inventario):
            print(f'{i}: {item.nome} (Ataque: {item.ataque})')

    def equipar_item(self, indice): #Item equipado na mão
        if 0 <= indice < len(self.inventario):
            # Se já houver um item equipado, desequipe-o primeiro
            if self.mao:
                item_atual = self.mao.pop()
                self.ataque -= item_atual.ataque
                print(f'{item_atual.nome} foi desequipado!')
                
            # Equipar o novo item
            item = self.inventario[indice]
            self.mao.append(item)
            self.ataque += item.ataque
            print(f'{item.nome} foi equipado!')
        else:
            print("Índice inválido!")