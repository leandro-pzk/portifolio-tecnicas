# multiplas-herancas.py

# Python suporta herança múltipla
# e usa uma ordem de profundidade ao pesquisar métodos.
# Este padrão de pesquisa é chamado de MRO (Method Resolution Order)

# Exemplo para herança "Diamond Shape"
# A pesquisa pode ficar complicada quando várias classes herdam
# de várias classes pai.

# Para evitar ambiguidade ao pesquisar um método
# em várias classes, do Python 2.3, a ordem de pesquisa do MRO tem um
# recurso adicional.

# Ele ainda faz uma pesquisa em profundidade, mas se a ocorrência de uma classe
# acontece várias vezes no caminho MRO, remove a ocorrência inicial
# e mantém o último.

# No exemplo abaixo, a classe `D` herda de `B` e `C`.
# E ambos `B` e `C` herdam de `A`.
# Ambos `A` e `C` tem o método `dothis()`.

# Instanciamos `D` e solicitamos o método 'dothis()'.
# Por padrão, a pesquisa deve ir D -> B -> A -> C -> A.
# Mas a partir do Python 2.3, para reduzir o tempo de pesquisa,
# o MRO pula as classes que ocorrem várias vezes no caminho.

# Portanto, a pesquisa será D -> B -> C -> A.


class A(object):
    def dothis(self):
        print("doing this in A")


class B(A):
    pass


class C(A):
    def dothis(self):
        print("doing this in C")


class D(B, C):
    pass


d_instance = D()
d_instance.dothis()

print("\nPrint the Method Resolution Order")
print(D.mro())
