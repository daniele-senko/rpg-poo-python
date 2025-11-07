from heroi import Heroi

class Mago(Heroi):
    def __init__(self, nome: str):
        vida_base = 80
        ataque_base = 8
        defesa_base = 3
        super().__init__(nome, vida_base, ataque_base, defesa_base)
        self.__pontosDeMana = 50

    @property
    def pontosDeMana(self):
        return self.__pontosDeMana

    def lancarFeitico(self, alvo):
        custo = 10
        if self.__pontosDeMana >= custo:
            self.__pontosDeMana -= custo
            dano = int(self.pontosDeAtaque * 2.5)
            print(f"{self.nome} lança um Feitiço causando {dano} de dano bruto!")
            dano_causado = alvo.receberDano(dano)
            print(f"Dano aplicado (após defesa): {dano_causado}")
            return dano_causado
        print(f"Mana insuficiente para lançar feitiço.")
        return 0