# 2_poliformismo.py

# Outro exemplo de polimorfismo são as vários
# funções em Python. Tomemos, por exemplo, a função interna
# chamado 'len'.

# 'len' está disponível para quase todos os tipos, como strings,
# ints, floats, dicionários, listas, tuplas etc.
# Quando len é chamado em um tipo, ele na verdade chama os inbuilts
# função privada 'len' nesse tipo ou __len__

# Todo tipo de objeto que suporta 'len' terá um private
# função 'len' embutida.

# Assim, por exemplo, um tipo de lista já possui um 'len()'
# função embutida no código Python e quando você executa o
# função len() no tipo de dado, verifica se o len
# função privada está disponível para esse tipo ou não.
# Se estiver disponível, ele o executa.

text = ["Hello", "Hola", "helo"]
print(len(text))

print(len("Hello"))
print(len({"a": 1, "b": 2, "c": 3}))
