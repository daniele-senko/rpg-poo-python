from monstro import Monstro
import random

class GremlinDaSombra(Monstro):
    # GremlinDaSombra é uma especialização de Monstro
    # Possui menos vida, ataque baixo, mas pode ter chance de esquivar

    def __init__(self):
        # Inicializa o Gremlin com valores específicos
        super().__init__(nome="Gremlin da Sombra", tipo="Gremlin", pontosDeVida=30, pontosDeAtaque=5, pontosDeDefesa=1, xpConcedida=20)
        self.chanceEsquiva = 0.3  # 30% de chance de esquivar de ataques

    def atacar(self, alvo):
        # Ataque padrão do Gremlin
        print(f"{self.nome} morde {alvo.nome} causando {self.pontosDeAtaque} de dano.")
        alvo.receberDano(self.pontosDeAtaque)

    def defender(self):
        # Defesa do Gremlin inclui chance de esquiva
        if random.random() < self.chanceEsquiva:
            print(f"{self.nome} esquiva do ataque!")
        else:
            # Se não esquivar, aumenta defesa temporária
            print(f"{self.nome} se defende, aumentando a defesa temporariamente.")
            self.pontosDeDefesa += 1
