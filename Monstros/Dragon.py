from Inimigo import *

class Dragon(Inimigo):
    def __init__(self):
        super().__init__('Dragon', 5, 12, 100, 100, 'SpriteInimigo/Dragon.png')