# main.py
# Versão narrativa e cinematográfica do jogo "A Sombra de Aethelgard"
# Mostra herói, inventário, inimigo e batalha com mensagens envolventes

from guerreiro import Guerreiro
from arma import Arma
from pocao import Pocao
from gremlin import GremlinDaSombra
from batalha import Batalha

def main():
    try:
        # ======================
        # Criação do Herói
        # ======================
        print("\n=== Nasce um Herói ===")
        heroi = Guerreiro(nome='Aldric')
        print(f"No reino de Aethelgard, surge {heroi.nome}, último descendente da linhagem de guardiões.")
        print(f"Ele possui {heroi.pontosDeVida} pontos de vida, {heroi.pontosDeAtaque} de ataque e {heroi.pontosDeDefesa} de defesa.\n")

        # ======================
        # Inventário e itens
        # ======================
        print("=== Preparando Equipamentos ===")
        espada = Arma(nome='Lâmina Solar', descricao='Forjada com a luz residual do sol.', danoExtra=7)
        pocao = Pocao(nome='Poção de Cura', descricao='Restaura a energia vital.', cura=20)

        heroi.inventario.adicionarItem(espada)
        heroi.inventario.adicionarItem(pocao)

        heroi.pontosDeAtaque += espada.danoExtra
        print(f"{heroi.nome} empunha a {espada.nome}, sentindo seu poder aumentar para {heroi.pontosDeAtaque} de ataque.\n")

        print("Itens no inventário:")
        heroi.inventario.listarItens()
        print()

        # ======================
        # Aparição do inimigo
        # ======================
        print("=== Uma Sombra se aproxima ===")
        gremlin = GremlinDaSombra()
        print(f"Das trevas surge {gremlin.nome}! Vida: {gremlin.pontosDeVida}, Ataque: {gremlin.pontosDeAtaque}, Defesa: {gremlin.pontosDeDefesa}\n")

        # ======================
        # Início da batalha
        # ======================
        print("=== A Batalha Começa ===")
        batalha = Batalha(jogador=heroi, inimigo=gremlin)
        turno = 1
        while heroi.estaVivo() and gremlin.estaVivo():
            print(f"--- Turno {turno} ---")
            if turno % 2 == 0:
                print(f"{heroi.nome} concentra sua força para um ataque poderoso!")
                heroi.ataquePoderoso(gremlin)
            else:
                print(f"{heroi.nome} investe contra {gremlin.nome}.")
                heroi.atacar(gremlin)

            if gremlin.estaVivo():
                print(f"{gremlin.nome} contra-ataca com ferocidade!")
                gremlin.atacar(heroi)
            else:
                print(f"{gremlin.nome} recua, derrotado pelo herói.")

            print(f"Status: {heroi.nome} (Vida: {heroi.pontosDeVida}) | {gremlin.nome} (Vida: {gremlin.pontosDeVida})\n")
            turno += 1

        # ======================
        # Pós-batalha
        # ======================
        print("=== Conclusão da Batalha ===")
        if heroi.estaVivo():
            print(f"{heroi.nome} triunfou sobre as trevas!")
            heroi.ganharExperiencia(gremlin.xpConcedida)
            print(f"{heroi.nome} recupera forças usando {pocao.nome}.")
            heroi.usarItem(pocao)
        else:
            print(f"As sombras vencem. {heroi.nome} cai diante de {gremlin.nome}...\n")

        print("=== Status Final do Herói ===")
        print(f"Nome: {heroi.nome}")
        print(f"Vida: {heroi.pontosDeVida}")
        print(f"Nível: {heroi.nivel}")
        print(f"Experiência: {heroi.experiencia}\n")

    except Exception as e:
        print(f"Ocorreu um erro durante o jogo: {e}")

if __name__ == '__main__':
    main()
