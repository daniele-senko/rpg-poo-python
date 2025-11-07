from personagem import Personagem
from inventario import Inventario
from item import Item

class Heroi(Personagem):
    # A classe Heroi herda Personagem para reaproveitar atributos e métodos básicos
    # Adiciona características próprias do jogador, como nível, experiência e inventário

    def __init__(self, nome: str, pontosDeVida: int = 100, pontosDeAtaque: int = 10, pontosDeDefesa: int = 5):
        # Inicializa o herói com valores padrão para vida, ataque e defesa
        # Cria o inventário dentro do herói, aplicando composição
        super().__init__(nome, pontosDeVida, pontosDeAtaque, pontosDeDefesa)
        self.nivel = 1  # Nível inicial do herói
        self.experiencia = 0  # Experiência acumulada
        self.inventario = Inventario(capacidade=10)  # Inventário é parte do herói, não existe sem ele

    def ganharExperiencia(self, xp: int):
        # Incrementa a experiência do herói
        # Método separado permite controlar regras de subida de nível
        self.experiencia += xp
        print(f"{self.nome} ganhou {xp} de experiência. Total de XP: {self.experiencia}")
        self.subirDeNivel()

    def subirDeNivel(self):
        # Sobrescreve o nível do herói quando a experiência atinge determinado limite
        # Cada nível aumenta atributos básicos, fortalecendo o personagem
        limite_xp = 100 * self.nivel
        while self.experiencia >= limite_xp:
            self.nivel += 1
            self.experiencia -= limite_xp
            self.pontosDeVida += 20  # Aumenta vida a cada nível
            self.pontosDeAtaque += 5  # Aumenta ataque
            self.pontosDeDefesa += 2  # Aumenta defesa
            print(f"{self.nome} subiu para o nível {self.nivel}!")

    def usarItem(self, item: Item):
        # Permite que o herói use um item do inventário
        # Essa relação é de agregação: o item pode existir fora do inventário
        if item in self.inventario.itens:
            if hasattr(item, 'cura'):
                # Se o item for uma poção de cura, aplica efeito
                self.pontosDeVida += item.cura
                print(f"{self.nome} usou {item.nome} e recuperou {item.cura} de vida. Vida atual: {self.pontosDeVida}")
            # Remove item após uso
            self.inventario.removerItem(item)
        else:
            print(f"{item.nome} não está no inventário.")

    def atacar(self, alvo):
        # Implementação do ataque padrão do herói
        # Pode ser sobrescrito por subclasses (como Guerreiro ou Mago)
        print(f"{self.nome} ataca {alvo.nome} causando {self.pontosDeAtaque} de dano.")
        alvo.receberDano(self.pontosDeAtaque)

    def defender(self):
        # Implementação padrão da defesa do herói
        # Pode ser sobrescrito por subclasses
        print(f"{self.nome} se defende, reduzindo dano no próximo ataque.")
        self.pontosDeDefesa += 2  # Bônus temporário simples
