"""
L - Liskov Substitution Principle

Princípio da Substituição de Liskov (pt-BR)

Uma subclasse deve ser substituível por sua superclasse. O objetivo disto
princípio é assegurar que uma subclasse pode assumir o lugar de sua
superclasse sem erros. Se o código se encontrar verificando o tipo de classe
então, deve ter violado este princípio.

Vamos usar nosso exemplo Animal.
"""

def animal_leg_count(animals: list):
    for animal in animals:
        if isinstance(animal, Lion):
            print(lion_leg_count(animal))
        elif isinstance(animal, Mouse):
            print(mouse_leg_count(animal))
        elif isinstance(animal, Pigeon):
            print(pigeon_leg_count(animal))
        
animal_leg_count(animals)

"""
Para fazer esta função seguir o princípio LSP, seguiremos este LSP
requisitos postulados por Steve Fenton:

Se a superclasse (Animal) tiver um método que aceite um tipo de superclasse
(Animal) parâmetro. Sua subclasse (Pigeon) deve aceitar como argumento um
tipo de superclasse (tipo de animal) ou tipo de subclasse (tipo de pombo). Se o
superclasse retorna um tipo de superclasse (Animal). Sua subclasse deve retornar um
tipo de superclasse (tipo Animal) ou tipo de subclasse (Pombo). Agora, podemos
reimplemente a função animal_leg_count:
"""

def animal_leg_count(animals: list):
    for animal in animals:
        print(animal.leg_count())
        
animal_leg_count(animals)

"""
A função animal_leg_count se importa menos com o tipo de Animal passado, apenas
chama o método leg_count. Tudo o que ele sabe é que o parâmetro deve ser de um
Tipo Animal, seja a classe Animal ou sua subclasse.

A classe Animal agora tem que implementar/definir um método leg_count. E os seus
subclasses precisam implementar o método leg_count:
"""

class Animal:
    def leg_count(self):
        pass


class Lion(Animal):
    def leg_count(self):
        pass


"""
Quando é passado para a função animal_leg_count, ele retorna o número de pernas
um leão tem.

Veja bem, o animal_leg_count não precisa saber o tipo de Animal para retornar
sua contagem de pernas, ele apenas chama o método leg_count do tipo Animal porque, por
contratar uma subclasse da classe Animal deve implementar a função leg_count.
"""
