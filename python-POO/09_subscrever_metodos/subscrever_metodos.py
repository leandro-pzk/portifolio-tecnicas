# subscrever_metodos.py


# Referência: O'Reilly Learning Path:
# http://shop.oreilly.com/product/0636920040057.do
# Capítulo 24: Sobrecarga de Métodos - Estendendo e Fornecendo

# Este código é um exemplo de como podemos estender um método herdado por
# uma classe filha da classe Pai.

# 1) Definimos `MyClass()` como uma classe abstrata,
# e tem três métodos, my_set_val(), my_get_val() e print_doc().
# 2) MyChildClass() herda de MyClass()
# 3) MyChildClass() estende o método my_set_val() do pai
# por seu próprio método my_set_val(). Ele verifica a entrada,
# verifica se é um inteiro, e então chama o método my_set_val()
# método no pai.

# 4) O método print_doc() no Pai é um método abstrato
# e, portanto, deve ser implementado na classe filha MyChildClass()


import abc


class MyClass(object):

    __metaclass__ = abc.ABCMeta

    def my_set_val(self, value):
        self.value = value

    def my_get_val(self):
        return self.value

    @abc.abstractmethod
    def print_doc(self):
        return


class MyChildClass(MyClass):
    def my_set_val(self, value):
        if not isinstance(value, int):
            value = 0
        super(MyChildClass, self).my_set_val(self)

    def print_doc(self):
        print("Documentation for MyChild Class")


my_instance = MyChildClass()
my_instance.my_set_val(100)
print(my_instance.my_get_val())
print(my_instance.print_doc())
