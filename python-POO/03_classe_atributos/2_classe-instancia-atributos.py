# 2_classe-instancia-atributos.py

# Este código mostra que uma instância pode acessar sua própria
# atributos, bem como atributos de classe.

# Temos um atributo de classe chamado 'count' e adicionamos 1 a
# cada vez que criamos uma instância. Isso pode ajudar a contar o
# número de instâncias no momento da instanciação.

class InstanceCounter(object):
    count = 0

    def __init__(self, val):
        self.val = val
        InstanceCounter.count += 1

    def set_val(self, newval):
        self.val = newval

    def get_val(self):
        print(self.val)

    def get_count(self):
        print(InstanceCounter.count)


a = InstanceCounter(5)
b = InstanceCounter(10)
c = InstanceCounter(15)

for obj in (a, b, c):
    print("value of obj: %s" % obj.get_val())
    print("Count : %s" % obj.get_count())
