# 2_decoradores_classe.py

# Referência: https://www.youtube.com/watch?v=Slf1b3yUocc
# Palestra de Mike Burns

# Até os exemplos anteriores, vimos decoradores de funções.
# Mas decoradores também podem ser aplicados a Classes.
# Este exemplo trata de decoradores de classe.

# NOTA: Se você estiver criando um decorador para uma classe, você
# para retornar uma classe.

# NOTA: Da mesma forma, se você estiver criando um decorador para uma função,
# você precisará dele para retornar uma função.


def honirific(cls):
    class HonirificCls(cls):
        def full_name(self):
            return "Dr. " + super(HonirificCls, self).full_name()

    return HonirificCls


@honirific
class Name(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return " ".join([self.first_name, self.last_name])


result = Name("Vimal", "A.R").full_name()
print("Full name: {0}".format(result))


# Isso precisa de verificação adicional. Errando fora.
