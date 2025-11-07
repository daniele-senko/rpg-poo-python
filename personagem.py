from abc import ABC, abstractmethod

class Personagem(ABC):
    # Classe abstrata que serve como modelo para heróis e monstros
    # Garante que todos os personagens compartilhem atributos e métodos essenciais

    def __init__(self, nome: str, pontosDeVida: int, pontosDeAtaque: int, pontosDeDefesa: int):
        # Construtor que inicializa os atributos principais
        # Atributos são privados para proteger o estado interno e permitir validação em setters
        self.__nome = nome
        self.__pontosDeVida = pontosDeVida
        self.__pontosDeAtaque = pontosDeAtaque
        self.__pontosDeDefesa = pontosDeDefesa

    # GETTERS E SETTERS

    @property
    def nome(self) -> str:
        # Retorna o nome do personagem
        return self.__nome

    @property
    def pontosDeVida(self) -> int:
        # Retorna a quantidade atual de pontos de vida
        return self.__pontosDeVida

    @pontosDeVida.setter
    def pontosDeVida(self, valor: int):
        # Ajusta os pontos de vida
        # Se o valor for negativo, define como zero
        # Isso evita valores inválidos de vida
        self.__pontosDeVida = max(0, valor)

    @property
    def pontosDeAtaque(self) -> int:
        # Retorna o poder de ataque
        return self.__pontosDeAtaque

    @pontosDeAtaque.setter
    def pontosDeAtaque(self, valor: int):
        # Permite alterar o ataque
        # Usado quando o personagem equipa armas ou recebe bônus
        self.__pontosDeAtaque = max(0, valor)

    @property
    def pontosDeDefesa(self) -> int:
        # Retorna o valor de defesa atual
        return self.__pontosDeDefesa

    @pontosDeDefesa.setter
    def pontosDeDefesa(self, valor: int):
        # Permite ajustar a defesa
        # Mantém a defesa nunca negativa
        self.__pontosDeDefesa = max(0, valor)

    # MÉTODOS COMUNS

    def estaVivo(self) -> bool:
        # Retorna True se o personagem ainda possui vida
        # Centralizar esta verificação evita repetição em subclasses
        return self.__pontosDeVida > 0

    def receberDano(self, dano: int):
        # Aplica o dano recebido considerando a defesa
        # Calcula o dano final subtraindo a defesa e ajusta vida para não ficar negativa
        danoFinal = max(0, dano - self.__pontosDeDefesa)
        self.__pontosDeVida = max(0, self.__pontosDeVida - danoFinal)
        print(f"{self.__nome} recebeu {danoFinal} de dano. Vida restante: {self.__pontosDeVida}")

    # MÉTODOS ABSTRATOS

    @abstractmethod
    def atacar(self, alvo):
        # Método abstrato que deve ser implementado pelas subclasses
        # Permite que cada tipo de personagem tenha sua forma de atacar
        pass

    @abstractmethod
    def defender(self):
        # Método abstrato que deve ser implementado pelas subclasses
        # Garante que todos os personagens tenham comportamento defensivo
        pass
