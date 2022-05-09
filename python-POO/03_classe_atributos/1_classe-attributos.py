# classe-attributos.py

# Aqui definimos um atributo na classe `YourClass`
# bem como um atributo dentro da função.

# O atributo definido na classe é chamado de `atributos de classe`
# e o atributo definido na função é chamado de `atributos de instância`.


class YourClass(object):
    classy = 10

    def set_val(self):
        self.insty = 100


dd = YourClass()
dd.classy  # Isto irá buscar o atributo de classe 10.
dd.set_val()
dd.insty  # Isso buscará o atributo de instância 100.


# Uma vez que `dd` é instanciado, podemos acessar tanto a classe quanto a instância
# atributos, ou seja, dd.classy e dd.insty.
