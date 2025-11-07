from heroi import Heroi

class Guerreiro(Heroi):
    # O Guerreiro herda de Heroi para reutilizar atributos e métodos básicos
    # Adiciona características próprias de um guerreiro, como ataque mais forte e vida maior

    def __init__(self, nome: str):
        # Inicializa o herói como Guerreiro, aplicando bônus específicos
        super().__init__(nome)
        self.pontosDeVida += 30   # Bônus de vida para o guerreiro
        self.pontosDeAtaque += 5  # Bônus de ataque para o guerreiro

    def ataquePoderoso(self, alvo):
        # Método exclusivo do Guerreiro
        # Demonstra polimorfismo: diferente do ataque padrão do herói
        dano_extra = self.pontosDeAtaque * 2
        print(f"{self.nome} realiza um ataque poderoso em {alvo.nome}, causando {dano_extra} de dano!")
        alvo.receberDano(dano_extra)

    def atacar(self, alvo):
        # Sobrescreve o método atacar do Heroi
        # Herói normal dá um ataque padrão, Guerreiro dá bônus natural
        print(f"{self.nome} ataca {alvo.nome} causando {self.pontosDeAtaque} de dano.")
        alvo.receberDano(self.pontosDeAtaque)

    def defender(self):
        # Sobrescreve o método defender do Heroi
        # O Guerreiro recebe bônus maior de defesa ao se defender
        print(f"{self.nome} se posiciona para defender, aumentando a defesa temporariamente.")
        self.pontosDeDefesa += 3
