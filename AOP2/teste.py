class Pessoa:
    def __init__(self, nome:str, idade:int) -> None:
        self.nome = nome
        self.idade = idade

    def __repr__(self) -> str:
        return f"{self.nome} {self.idade}"

class Aluno(Pessoa):
    def __init__(self, nome:str, idade:int, curso:str) -> None:
        super().__init__(nome, idade)
        self.cursando = curso
    
    def __repr__(self) -> str:
        return super().__repr__() + f" está cursando {self.cursando}"

aluno1 = Aluno("Filipe", 30, "ADS")
print(aluno1)