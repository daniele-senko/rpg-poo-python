from item import Item

class Pocao(Item):
    # Pocao é um item que pode ser usado pelo herói para recuperar vida
    # Pode existir fora do inventário e ser agregado quando necessário

    def __init__(self, nome: str, descricao: str, cura: int):
        # Inicializa a poção com nome, descrição e quantidade de cura
        super().__init__(nome, descricao)
        self.cura = cura  # Quantidade de vida que será restaurada ao usar a poção
