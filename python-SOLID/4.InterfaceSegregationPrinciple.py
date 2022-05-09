"""
I - Interface Segregation Principle


Princípio de Segregação de Interface (pt-BR)

Faça interfaces refinadas que sejam específicas do cliente Os clientes não devem ser
forçados a depender de interfaces que eles não usam. Este princípio trata
com as desvantagens de implementar grandes interfaces.

Vejamos a interface IShape abaixo:
"""

class IShape:
    def draw_square(self):
        raise NotImplementedError
    
    def draw_rectangle(self):
        raise NotImplementedError
    
    def draw_circle(self):
        raise NotImplementedError

"""
Esta interface desenha quadrados, círculos, retângulos. classe Círculo, Quadrado ou
Rectangle implementando a interface IShape deve definir os métodos
draw_square(), draw_rectangle(), draw_circle().
"""

class Circle(IShape):
    def draw_square(self):
        pass

    def draw_rectangle(self):
        pass
    
    def draw_circle(self):
        pass

class Square(IShape):
    def draw_square(self):
        pass

    def draw_rectangle(self):
        pass
    
    def draw_circle(self):
        pass

class Rectangle(IShape):
    def draw_square(self):
        pass

    def draw_rectangle(self):
        pass
    
    def draw_circle(self):
        pass

"""
É muito engraçado olhar para o código acima. classe Rectangle implementa métodos
(draw_circle e draw_square) não tem uso, da mesma forma que a implementação do Square
draw_circle e draw_rectangle e classe Circle (draw_square, draw_rectangle).

Se adicionarmos outro método à interface IShape, como draw_triangle(),
"""

class IShape:
    def draw_square(self):
        raise NotImplementedError
    
    def draw_rectangle(self):
        raise NotImplementedError
    
    def draw_circle(self):
        raise NotImplementedError
    
    def draw_triangle(self):
        raise NotImplementedError


"""
As classes devem implementar o novo método ou um erro será lançado.

Vemos que é impossível implementar uma forma que pode desenhar um círculo, mas não
um retângulo ou um quadrado ou um triângulo. Podemos apenas implementar os métodos para
lançar um erro que mostra que a operação não pode ser executada.

O ISP desaprova o design desta interface IShape. clientes (aqui Rectangle,
Círculo e Quadrado) não devem ser forçados a depender de métodos que eles não
precisar ou usar. Além disso, o ISP afirma que as interfaces devem realizar apenas um trabalho (apenas
como o princípio SRP) qualquer agrupamento extra de comportamento deve ser abstraído
para outra interface.

Aqui, nossa interface IShape executa ações que devem ser tratadas de forma independente
por outras interfaces.

Para que nossa interface IShape esteja em conformidade com o princípio ISP, separamos os
ações para diferentes interfaces. Classes (Círculo, Retângulo, Quadrado, Triângulo,
etc) podem apenas herdar da interface IShape e implementar seu próprio desenho
comportamento.
"""

class IShape:
    def draw(self):
        raise NotImplementedError

class Circle(IShape):
    def draw(self):
        pass

class Square(IShape):
    def draw(self):
        pass

class Rectangle(IShape):
    def draw(self):
        pass

"""
Podemos então usar as interfaces I para criar especificações de forma como Semi Circle,
Triângulo de ângulo reto, triângulo equilátero, retângulo de arestas sem corte, etc.
"""