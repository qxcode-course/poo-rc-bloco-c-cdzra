class Crianca:
    def __init__(self, nome: str, idade: int):
        self.__nome = nome
        self.__idade = idade

    def getNome(self):
        return self.__nome
    
    def getIdade(self):
        return self.__idade
    
    def setNome(self, nome: str):
        self.__nome = nome

    def setIdade(self, idade: int):
        self.__idade = idade

    def __str__(self):
        return f"{Crianca.getNome}:{Crianca.getIdade}"
    
class Trampolim:
    def __init__(self):
        self.brincando: list[Crianca] = []
        self.esperando: list[Crianca] = []

    def removeFromList(self, nome: str, listC: list[Crianca]) -> Crianca | None:
        for i, crianca in enumerate(listC):
            if crianca.getNome() == nome:
                return listC.pop(i)
            return None
        
    def removerCrianca(self, nome: str) -> Crianca | None:
        crianca = self.removeFromList(nome, self.esperando)
        if crianca is not None:
            return crianca
        return self.removeFromList(nome, self.brincando)
    
    def arrive(self, crianca: Crianca):
        self.esperando.insert(0, crianca)
        

