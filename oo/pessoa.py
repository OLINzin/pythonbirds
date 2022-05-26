class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=14):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    renzo = Pessoa(nome='Renzo')
    gabriel = Pessoa(renzo, nome='Gabriel')
    print(Pessoa.cumprimentar(gabriel))
    print(id(gabriel))
    print(gabriel.cumprimentar())
    print (gabriel.nome)
    print(gabriel.idade)
    for filho in gabriel.filhos:
        print(filho.nome)
    gabriel.sobrenome = 'Eurich'
    del gabriel.filhos
    gabriel.olhos = 1
    del gabriel.olhos
    print(gabriel.__dict__)
    print(renzo.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(gabriel.olhos)
    print(renzo.olhos)
    print(id(Pessoa.olhos), id(gabriel.olhos), id(renzo.olhos))
