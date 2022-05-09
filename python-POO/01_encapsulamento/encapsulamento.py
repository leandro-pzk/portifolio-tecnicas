# Encapsulamento.py

# Metodos:
# set_val(), get_val(), and increment_val().


class MyInteger(object):
    def set_val(self, val):
        try:
            val = int(val)
        except ValueError:
            return
        self.val = val

    def get_val(self):
        print(self.val)

    def increment_val(self):
        self.val = self.val + 1
        print(self.val)


a = MyInteger()
a.set_val(10)
a.get_val()
a.increment_val()
print("\n")

# Tentativa de quebra do encasulamento de uma nova instacia com inteiros
c = MyInteger()
c.val = 15
c.get_val()
c.increment_val()
print("\n")

# Tentativa de quebra do encasulamento de uma nova instacia com string
b = MyInteger()
b.val = "MyString"  # <== Quebra com sucesso!
b.get_val()  # <== Imprime o val quebrando o encapsulamento
b.increment_val()  # Isso falhará, pois str + int não funcionará
print("\n")
