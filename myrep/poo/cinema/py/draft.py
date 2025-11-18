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
    
class Cinema:
    def __init__(self, capacidade: int):
        self.__acentos = list[Cliente | None] = [None] * capacidade
        self.__capacidade = capacidade

    def busca(self, id: str) -> int:
        for i, cliente in enumerate(self.__acentos):
            if cliente is not None and cliente.getId() == id:
                return i
        return -1

    def verificarIndex(self, index: int) -> bool:
        return 0 <= index < self.__capacidade
    
    