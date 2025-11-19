class Slot:
    def __init__(self, nome: str, preco: int, qtd: int):
        self.nome = nome
        self.preco = preco
        self.qtd = qtd

    def getNome(self):
        return self.nome
    
    def getPreco(self):
        return self.preco
    
    def getQtd(self):
        return self.qtd
    
    def setNome(self, nome: str):
        self.nome = nome

    def setPreco(self, preco: int):
        self.preco = preco

    def setQtd(self, qtd: int):
        self.qtd = qtd

    def __str__(self):
        return f"{self.nome}:{self.preco}:{self.qtd}"