# 1_heranca.py

# O código abaixo mostra como uma classe pode herdar de outra classe.
# Temos duas classes, `Date` e `Time`. Aqui `Time` herda de
# `Data`.

# Qualquer classe herdada de outra classe (também chamada de classe pai)
# herda os métodos e atributos da classe Parent.

# Portanto, qualquer instância criada a partir da classe `Time` pode acessar
# os métodos podem ter certeza na classe pai `Date`.


class Date(object):
    def get_date(self):
        print("2016-05-14")


class Time(Date):
    def get_time(self):
        print("07:00:00")



# Criando uma instância de `Date`
dt = Date()
dt.get_date()  # Acessando o método `get_date()` de `Date`
print("--------")

# Criando uma instância de `Time`.
tm = Time()
tm.get_time()  # Acessando o método `get_time()` de `Time`.

# Acessando o `get_date() que está definido na classe pai `Date`.
tm.get_date()
