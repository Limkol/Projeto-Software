class Produto:
    def __init__(self, nome, preco, quantidadeEmEstoque):
        self.nome = nome
        self.preco = preco
        self.quantidadeEmEstoque = quantidadeEmEstoque

    def exibirResumo(self):
        return f'Produto: {self.nome}\nValor: {self.preco}\nQuantidade: {self.quantidadeEmEstoque}'