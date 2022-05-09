#classe_abstrata.py

# Este trecho de código fala sobre Abstract Base Classes (abc).

# O módulo `abc` fornece recursos para criar
# Classes básicas abstratas.

# Para criar uma classe base abstrata, defina o método mágico `__metaclass__`
# para `abc.ABCMeta`. Isso marcará a respectiva classe como um Resumo
# Classe básica.

# Agora, para especificar os métodos que devem ser aplicados no
# classes filhas, ou seja, para criar Métodos Abstratos, usamos o decorador
# @abc.abstractmethod sobre os métodos que precisamos.

# A classe filha que herda de uma classe base abstrata pode implementar
# métodos próprios, mas *deve sempre* implementar os métodos definidos em
# a classe ABC pai.

import abc


class My_ABC_Class(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def set_val(self, val):
        return

    @abc.abstractmethod
    def get_val(self):
        return



# Classe Base Abstrata definida acima ^^^

# Classe personalizada herdada da classe base abstrata acima, abaixo


class MyClass(My_ABC_Class):
    def set_val(self, input):
        self.val = input

    def get_val(self):
        print("\nCalling the get_val() method")
        print("I'm part of the Abstract Methods defined in My_ABC_Class()")
        return self.val

    def hello(self):
        print("\nCalling the hello() method")
        print("I'm *not* part of the Abstract Methods defined in My_ABC_Class()")


my_class = MyClass()

my_class.set_val(10)
print(my_class.get_val())
my_class.hello()
