from item import Item

class Arma(Item):
    # Arma é um item que concede bônus de ataque
    # Pode ser adicionada ao inventário do herói, mas existe independentemente

    def __init__(self, nome: str, descricao: str, danoExtra: int):
        # Inicializa a arma com nome, descrição e dano adicional
        super().__init__(nome, descricao)
        self.danoExtra = danoExtra  # Bônus de ataque concedido ao herói que equipa a arma
