class Cliente:
    def __init__(self, id: str, fone: int):
        self.__id = id
        self.__fone = fone

    def getId(self):
        return self.__id
    
    def getFone(self):
        return self.__fone
    
    def setId(self, id: str):
        self.__id = id

    def setFone(self, fone: int):
        self.__fone = fone
    
    def __str__(self):
        return f"{self.__id}:{self.__fone}"