class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def quemSouEu(self):
        return "Classe Pessoa - Primária"

#É necessário repetir todos os parâmetros da classe pai.
class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula, periodo):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula
        self.periodo = periodo
    def quemSouEu(self):
        return 'Classe Aluno - Herda Pessoa'

class Professor(Pessoa):
    super(Pessoa)

aluno1 = Aluno('Filipe', 30, 22222, 4)

print(aluno1.quemSouEu())