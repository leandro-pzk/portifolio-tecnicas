# 1_decoradores_funcao.py
# Decoradores, o mais simples possível :)

# Referência: Decorators 101 - A Gentil Introdução à Programação Funcional.
# Por Jillian Munson - PyGotham 2014.
# https://www.youtube.com/watch?v=yW0cK3IxlHc

# Decoradores são funções que complementam outras funções,
# ou em outras palavras, modificar uma função ou método.

# No exemplo abaixo, temos uma função chamada `decorated`.
# Esta função apenas imprime "Isso aconteceu".
# Temos um decorador criado chamado `inner_decorator()`.
# Esta função de decorador tem uma função dentro, que
# faz algumas operações (imprime coisas para simplificar) e depois
# retorna o valor de retorno da função interna.

# Como funciona?
# a) A função `decorated()` é chamada.
# b) Como o decorador `@my_decorator` é definido acima
# `decorated()`, `my_decorator()` é chamado.
# c) my_decorator() recebe um nome de função como args e, portanto, `decorated()`
# é passado como o argumento.
# d) `my_decorator()` faz seu trabalho, e quando atinge `myfunction()`
# chama a função real, ou seja, decorado()
# e) Assim que a função `decorated()` for concluída, ela volta para `my_decorator()`.
# f) Assim, usar um decorador pode mudar drasticamente o comportamento do
# função que você está realmente executando.


def my_decorator(my_function):  # <-- (4)
    def inner_decorator():  # <-- (5)
        print("This happened before!")  # <-- (6)
        my_function()  # <-- (7)
        print("This happens after ")  # <-- (10)
        print("This happened at the end!")  # <-- (11)

    return inner_decorator
    # return None


@my_decorator  # <-- (3)
def my_decorated():  # <-- (2) <-- (8)
    print("This happened!")  # <-- (9)


if __name__ == "__main__":
    my_decorated()  # <-- (1)


