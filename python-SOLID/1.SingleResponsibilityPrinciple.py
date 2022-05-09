"""
S - Single Responsibility Principle

Princípio de Responsabilidade Única (pt-BR)

Uma classe deve ter apenas um trabalho. Se uma classe tiver mais de uma responsabilidade,
torna-se acoplado. Uma mudança em uma responsabilidade resulta na modificação de
a outra responsabilidade.

"""

class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        pass

    def save(self, animal: Animal):
        pass

"""
A classe Animal viola o SRP.

Como isso viola o SRP?

SRP afirma que as classes devem ter uma responsabilidade, aqui, podemos extrair
duas responsabilidades: 
* Gerenciamento de banco de dados de animais;
* Gerenciamento de propriedades de animais.

O "construtor" (init) e "get_name" gerenciam as propriedades do Animal enquanto o
save gerencia o armazenamento de animais em um banco de dados.

Como esse design causará problemas no futuro?

Se o aplicativo mudar de maneira que afete o gerenciamento do banco de dados
funções. As classes que fazem uso de propriedades Animal terão que ser
tocado e recompilado para compensar as novas mudanças.

Você vê este sistema cheira a rigidez, é como um efeito dominó, toque um
carta afeta todas as outras cartas na fila.

Para fazer isso de acordo com o SRP, criamos outra classe que lidará com o único
responsabilidade de armazenar um animal em um banco de dados:

"""

class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        pass


class AnimalDB:
    def get_animal(self, id) -> Animal:
        pass

    def save(self, animal: Animal):
        pass

"""
Ao projetar nossas classes, devemos procurar reunir recursos relacionados, para que
sempre que tendem a mudar, mudam pela mesma razão. E devemos tentar
para separar recursos se eles forem alterados por motivos diferentes. - Steve Fenton
"""

"""
A desvantagem desta solução é que os clientes deste código têm que lidar
com duas aulas. Uma solução comum para este dilema é aplicar o Facade
padronizar. A classe Animal será a Fachada para gerenciamento de banco de dados de animais e
gestão de propriedades animais.
"""

class Animal:
    def __init__(self, name: str):
        self.name = name
        self.db = AnimalDB()

    def get_name(self) -> str:
        return self.name

    def get(self, id):
        return self.db.get_animal(id)
    
    def save(self):
        self.db.save(animal=self)


"""
Os métodos mais importantes são mantidos na classe Animal e usados ​​como Fachada para
as funções menores.
"""