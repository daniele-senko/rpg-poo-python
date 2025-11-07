from personagem import Personagem

class Monstro(Personagem):
    # A classe Monstro representa qualquer inimigo do jogo
    # Adiciona o tipo do monstro e a quantidade de experiência que ele concede quando derrotado

    def __init__(self, nome: str, tipo: str, pontosDeVida: int, pontosDeAtaque: int, pontosDeDefesa: int, xpConcedida: int):
        # Inicializa o monstro com atributos básicos e específicos
        super().__init__(nome, pontosDeVida, pontosDeAtaque, pontosDeDefesa)
        self.tipo = tipo           # Tipo do monstro, ex: Gremlin, Lobo Vil, etc.
        self.xpConcedida = xpConcedida  # Experiência que o herói ganha ao derrotar

    def atacar(self, alvo):
        # Implementação padrão de ataque do monstro
        # Pode ser sobrescrito por subclasses com ataques especiais
        print(f"{self.nome} ({self.tipo}) ataca {alvo.nome} causando {self.pontosDeAtaque} de dano.")
        alvo.receberDano(self.pontosDeAtaque)

    def defender(self):
        # Implementação padrão de defesa do monstro
        # Subclasses podem modificar para habilidades específicas de defesa
        print(f"{self.nome} se protege, aumentando a defesa temporariamente.")
        self.pontosDeDefesa += 2
