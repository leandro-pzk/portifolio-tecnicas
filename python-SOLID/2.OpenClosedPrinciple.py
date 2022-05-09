"""
O - Open-Closed Principle


Princípio Aberto-Fechado (pt-BR)

Entidades de software (classes, módulos, funções) devem ser abertas para extensão, não
modificação.
"""
class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        pass

animals = [
    Animal('lion'),
    Animal('mouse')
]

def animal_sound(animals: list):
    for animal in animals:
        if animal.name == 'lion':
            print('roar')

        elif animal.name == 'mouse':
            print('squeak')

animal_sound(animals)

"""
A função som_animal não está de acordo com o princípio aberto-fechado porque
não pode ser fechado contra novos tipos de animais. Se adicionarmos um novo animal,
Snake, temos que modificar a função animal_sound. Você vê, para cada novo
animal, uma nova lógica é adicionada à função animal_sound. Isso é bastante
exemplo simples. Quando sua aplicação crescer e se tornar complexa, você verá
que a instrução if seria repetida várias vezes no som_animal
função cada vez que um novo animal é adicionado, em todo o aplicativo.
"""

animals = [
    Animal('lion'),
    Animal('mouse'),
    Animal('snake')
]

def animal_sound(animals: list):
    for animal in animals:
        if animal.name == 'lion':
            print('roar')
        elif animal.name == 'mouse':
            print('squeak')
        elif animal.name == 'snake':
            print('hiss')

animal_sound(animals)


"""
Como fazemos para que (o som_animal) esteja em conformidade com o OCP?
"""

class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        pass

    def make_sound(self):
        pass


class Lion(Animal):
    def make_sound(self):
        return 'roar'


class Mouse(Animal):
    def make_sound(self):
        return 'squeak'


class Snake(Animal):
    def make_sound(self):
        return 'hiss'


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())

animal_sound(animals)

"""
Animal agora tem um método virtual make_sound. Temos cada animal estendendo o
Animal e implemente o método virtual make_sound.

Cada animal adiciona sua própria implementação de como faz um som no
fazer som. O animal_sound itera pelo array de animal e apenas
chama seu método make_sound.

Agora, se adicionarmos um novo animal, animal_sound não precisa ser alterado. Tudo que precisamos
a fazer é adicionar o novo animal ao array animal.

animal_sound agora está em conformidade com o princípio OCP.
"""

"""
Outro exemplo:

Vamos imaginar que você tem uma loja e dá um desconto de 20% no seu favorito
clientes desta classe: Quando você decide oferecer o dobro do desconto de 20% para
clientes VIP. Você pode modificar a classe assim:
"""

class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def give_discount(self):
            if self.customer == 'fav':
                return self.price * 0.2
            if self.customer == 'vip':
                return self.price * 0.4


"""
Não, isso falha no princípio OCP. O OCP proíbe. Se queremos dar uma nova
por cento de desconto talvez, para um diff. tipo de clientes, você verá que um novo
lógica será adicionada.

Para fazê-lo seguir o princípio OCP, adicionaremos uma nova classe que estenderá
o desconto. Nesta nova classe, implementaríamos seu novo comportamento:
"""

class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def get_discount(self):
            return self.price * 0.2


class VIPDiscount(Discount):
    def get_discount(self):
        return super().get_discount() * 2

"""
Se você decidir 80% de desconto para clientes super VIP, deve ser assim:
Você vê, extensão sem modificação.
"""

class SuperVIPDiscount(VIPDiscount):
    def get_discount(self):
        return super().get_discount() * 2
