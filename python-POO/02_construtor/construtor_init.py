# construtor_init.py

# Adicionado um teste no metodo construtor __init__() para verificar
# se o valor é inteiro ou não.


class MyNum(object):
    def __init__(self, value):
        try:
            value = int(value)
        except ValueError:
            value = 0
        self.value = value

    def increment(self):
        self.value = self.value + 1
        print(self.value)


a = MyNum(10)
a.increment()  # Resultado impresso esperado: 11
a.increment()  # Resultado impresso esperado: 12
