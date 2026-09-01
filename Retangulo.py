class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcularArea(self):
        return self.largura * self.altura

    def calcularPerimetro(self):
        return (self.largura * 2) + (self.altura * 2) 