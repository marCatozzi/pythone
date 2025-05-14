#Es. P10.8 di pag.661 Python
class Person:
    def __init__(self, nome, anno_nascita):
        self.nome = nome
        self.anno_nascita = anno_nascita
    def __str__(self):
        return f"Nome: {self.nome}, Anno di nascita: {self.anno_nascita}"

class Student(Person):
    def __init__(self, nome, anno_nascita, corso_laurea):
        super().__init__(nome, anno_nascita)
        self.corso_laurea = corso_laurea
    def __str__(self):
        return super().__str__() + f", Corso di laurea: {self.corso_laurea}"

class Instructor(Person):
    def __init__(self, nome, anno_nascita, salario):
        super().__init__(nome, anno_nascita)
        self.salario = salario
    def __str__(self):
        return super().__str__() + f", Salario: {self.salario}"

maryuri = Student("Maryuri", "01/02/98", "Grafica")
federico = Student("Federico", "21/02/96", "Criminologia")
andrea = Instructor ("Andrea", "13/03/93", "1000€")

print(maryuri)
print(federico)
print(andrea)