"""A leopard"""

import animal

class Leopard(animal.Animal):

    def __init__(self):
        kind = 'leopard'

    def get_kind(self):
        return self.kind
