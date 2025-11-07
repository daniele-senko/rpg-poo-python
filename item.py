from abc import ABC

class Item(ABC):
    # Item é uma classe base abstrata
    # Serve como modelo para qualquer objeto que o herói possa coletar ou usar
    # Pode ser agregado a inventários, mas existe independentemente deles

    def __init__(self, nome: str, descricao: str):
        # Inicializa o item com nome e descrição
        # Esses atributos são públicos, pois não é necessário encapsulamento rígido aqui
        self.nome = nome
        self.descricao = descricao
