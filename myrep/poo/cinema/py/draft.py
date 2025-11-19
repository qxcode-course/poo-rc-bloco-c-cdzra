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
        self.__acentos: list[Cliente | None] = [None] * capacidade
        self.__capacidade = capacidade

    def busca(self, id: str) -> int:
        for i, cliente in enumerate(self.__acentos):
            if cliente is not None and cliente.getId() == id:
                return i
        return -1

    def verificarIndex(self, index: int) -> bool:
        return 0 <= index < self.__capacidade
    
    def reservar(self, id: str, fone: int, index: int) -> bool:
        if index < 0 or index >= len(self.__acentos):
            print("fail: cadeira nao existe")
            return False
        if self.busca(id) != -1:
            print("fail: cliente ja esta no cinema")
            return False
        if self.__acentos[index] is not None:
            print("fail: cadeira ja esta ocupada")
            return False
        self.__acentos[index] = Cliente(id, fone)
        return True
    
    def cancelar(self, id: str) -> bool:
        pos = self.busca(id)
        if pos == -1:
            print("fail: cliente nao esta no cinema")
            return False
        self.__acentos[pos] = None
        return True
    
    def getAcentos(self):
        return self.__acentos
    
    def __str__(self):
        out = []
        for acentos in self.__acentos:
            if acentos is None:
                out.append("-")
            else:
                out.append(str(acentos))
        return f"[{" ".join(out)}]"
        
def main():
    cinema = Cinema(0)
    while True:
        line = input()
        print("$" + line)
        args: list[str] = line.split()
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(cinema)
        elif args[0] == "init":
            cine = int(args[1])
            cinema = Cinema(cine)
        elif args[0] == "reserve":
            id = args[1]
            fone = int(args[2])
            index = int(args[3])
            cinema.reservar(id, fone, index)
        elif args[0] == "cancel":
            id = args[1]
            cinema.cancelar(id)
main()