class Inventario:
    # Inventario gerencia os itens do herói
    # Cada herói possui seu próprio inventário, que é criado junto com ele

    def __init__(self, capacidade: int):
        # Inicializa o inventário com capacidade máxima e lista de itens vazia
        self.itens = []  # Lista de objetos Item
        self.capacidade = capacidade  # Número máximo de itens que pode armazenar

    def adicionarItem(self, item):
        # Adiciona um item ao inventário
        # Verifica se ainda há espaço disponível
        if len(self.itens) < self.capacidade:
            self.itens.append(item)
            print(f"{item.nome} foi adicionado ao inventário.")
        else:
            print("Inventário cheio. Não foi possível adicionar o item.")

    def removerItem(self, item):
        # Remove um item do inventário
        if item in self.itens:
            self.itens.remove(item)
            print(f"{item.nome} foi removido do inventário.")
        else:
            print(f"{item.nome} não está no inventário.")

    def listarItens(self):
        # Lista todos os itens do inventário
        if not self.itens:
            print("Inventário vazio.")
        else:
            print("Itens no inventário:")
            for item in self.itens:
                print(f"- {item.nome}: {item.descricao}")
