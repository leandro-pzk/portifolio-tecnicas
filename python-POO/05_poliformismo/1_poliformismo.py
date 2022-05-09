# 1_poliformismo.py

# Polimorfismo significa ter a mesma interface/atributos em diferentes
# classes.

# Polimorfismo é a característica de poder atribuir
# um significado ou uso diferente em contextos diferentes.

# Um exemplo não tão claro/limpo é que diferentes classes podem ter
# o mesmo nome de função.

# Aqui, a classe Dog and Cat tem o mesmo método chamado 'show_affection'
# Mesmo que sejam iguais, ambos realizam ações diferentes na instância.
#
# Como a ordem da pesquisa é
# 'instance' -> 'class' -> 'parent class', mesmo que o
# 'class' e 'classe pai' tem funções com o mesmo nome,
# a instância pegará apenas o primeiro hit,
# ie.. da 'class' e não irá para a classe pai.


class Animal(object):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print("{0} eats {1}".format(self.name, food))


class Dog(Animal):
    def fetch(self, thing):
        print("{0} goes after the {1}!".format(self.name, thing))

    def show_affection(self):
        print("{0} wags tail".format(self.name))


class Cat(Animal):
    def swatstring(self):
        print("{0} shreds more string".format(self.name))

    def show_affection(self):
        print("{0} purrs".format(self.name))


for a in (Dog("Rover"), Cat("Fluffy"), Cat("Lucky"), Dog("Scout")):
    a.show_affection()
