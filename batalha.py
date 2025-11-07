class Batalha:
    # A Batalha associa um herói a um monstro
    # Controla o fluxo do combate, turnos e condição de vitória

    def __init__(self, jogador, inimigo):
        # Inicializa a batalha com as instâncias de herói e monstro
        self.jogador = jogador
        self.inimigo = inimigo

    def iniciar(self):
        # Loop principal da batalha
        # Alterna ataques entre herói e monstro até que um deles seja derrotado
        print(f"Iniciando batalha: {self.jogador.nome} vs {self.inimigo.nome}\n")
        turno = 1
        while self.jogador.estaVivo() and self.inimigo.estaVivo():
            print(f"--- Turno {turno} ---")
            self.turno()
            turno += 1
        self.verificarFimDeBatalha()

    def turno(self):
        # Simula um turno de ataque
        # Herói ataca primeiro
        if self.jogador.estaVivo():
            self.jogador.atacar(self.inimigo)
        # Monstro ataca se ainda estiver vivo
        if self.inimigo.estaVivo():
            self.inimigo.atacar(self.jogador)
        # Mostra o status de vida após o turno
        print(f"Status: {self.jogador.nome} (Vida: {self.jogador.pontosDeVida}) | {self.inimigo.nome} (Vida: {self.inimigo.pontosDeVida})\n")

    def verificarFimDeBatalha(self):
        # Verifica o resultado da batalha
        if self.jogador.estaVivo():
            print(f"{self.jogador.nome} venceu a batalha!")
            # Ganha experiência pelo inimigo derrotado
            if hasattr(self.inimigo, 'xpConcedida'):
                self.jogador.ganharExperiencia(self.inimigo.xpConcedida)
        else:
            print(f"{self.jogador.nome} foi derrotado por {self.inimigo.nome}.")
