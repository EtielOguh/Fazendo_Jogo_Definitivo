from Inimigo import *

class Demon(Inimigo):
    def __init__(self):
        super().__init__('Demon', 2, 12, 100, 100, 'SpriteInimigo/Demon.png')