from Inimigo import *

class Demon(Inimigo):
    def __init__(self):
        super().__init__('Demon', 5, 12, 200, 300, 'SpriteInimigo/Demon.png')