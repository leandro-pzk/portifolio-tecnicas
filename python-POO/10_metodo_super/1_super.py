# 1_super.py

# Este é um exemplo de como funciona super()
# na herança.

# Para mais detalhes passo a passo, consulte:
# https://arvimal.wordpress.com/2016/07/01/inheritance-and-super-object-oriented-programming/


class MyClass(object):
    def func(self):
        print("I'm being called from the Parent class")


class ChildClass(MyClass):
    def func(self):
        print("I'm actually being called from the Child class")
        print("But...")
        # Chamando o método `func()` da classe Parent.
        super(ChildClass, self).func()


my_instance_2 = ChildClass()
my_instance_2.func()
