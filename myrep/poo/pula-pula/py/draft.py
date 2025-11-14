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