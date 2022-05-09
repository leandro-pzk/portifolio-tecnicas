# metodos_instancia.py


# Métodos de instância também são conhecidos como métodos Bound, pois os métodos
# dentro de uma classe são vinculados à instância criada a partir da classe, via
# 'self'.


class A(object):
    def method(*argv):
        return argv


a = A()
print(a.method)


# A função print() imprimirá o seguinte:
# python 17-instance_methods-1.py
# <método vinculado A.método de <__main__.Um objeto em 0x7fc91d83e790>>

# A saída mostra que 'método' é um método vinculado
