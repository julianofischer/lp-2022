#!/usr/bin/python3

x = 10
class Calculadora:
    def calcula(self, empregados):
        for e in empregados:
            print(f'O empregado {e.nome} ({e.id}) possui o salario {e.calcula_salario()}')


class Empregado:
    def __init__(self, idx, nome):
        self.id = idx
        self.nome = nome


class Assalariado(Empregado):
    def __init__(self, idx, nome, salario):
        super().__init__(idx, nome)
        self.salario = salario

    def calcula_salario(self):
        return self.salario


class Comissionado(Assalariado):
    def __init__(self, idx, nome, salario, comissao):
        super().__init__(idx, nome, salario)
        self.comissao = comissao

    def calcula_salario(self):
        return super().calcula_salario() + self.comissao


class Freelancer(Empregado):
    def __init__(self, idx, nome, valor_hora, horas_trabalhadas):
        super().__init__(idx, nome)
        self.valor_hora = valor_hora
        self.horas_trabalhadas = horas_trabalhadas

    def calcula_salario(self):
        return self.valor_hora * self.horas_trabalhadas

    

if __name__ == '__main__':
    a = Assalariado(1, 'Assalariado', 1250)
    print(a.calcula_salario())
    c = Comissionado(2, 'Comissionado', 1250, 50)
    print(c.calcula_salario())
    f = Freelancer(3, 'Freelancer', 50, 80)
    print(f.calcula_salario())
    calc = Calculadora()
    calc.calcula([a,c,f])