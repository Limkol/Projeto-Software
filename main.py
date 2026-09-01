from Pessoa import Pessoa
from Produto import Produto
from Retangulo import Retangulo

# ex.1
"""
pessoa1 = Pessoa("Leonardo", 34)
pessoa2 = Pessoa("ViniJr", 24)

print(pessoa1.apresentar())
print(pessoa2.apresentar())
"""

# ex.2
"""
prod1 = Produto("ps5", 15000, 5)
prod2 = Produto("Iphone", 22699, 20)
prod3 = Produto("Notebook", 400, 7)

print(prod1.exibirResumo())
print(prod2.exibirResumo())
print(prod3.exibirResumo())
"""

# ex.3
ret1 = Retangulo(22, 30)
ret2 = Retangulo(4, 10)

print(""ret1.calcularArea())
print(ret1.calcularPerimetro())
print(ret2.calcularArea())
print(ret2.calcularPerimetro())