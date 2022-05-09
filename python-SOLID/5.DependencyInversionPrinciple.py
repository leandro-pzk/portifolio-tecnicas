"""
D - Dependency Inversion Principle

Princípio de Inversão de Dependência (pt-BR)

A dependência deve ser em abstrações e não em concreções A. Módulos de alto nível
não deve depender de módulos de baixo nível. Ambos devem depender de abstrações.
B. As abstrações não devem depender de detalhes. Os detalhes devem depender
abstrações.

Chega um ponto no desenvolvimento de software em que nosso aplicativo será amplamente
composto por módulos. Quando isso acontece, temos que esclarecer as coisas usando
Injeção de dependência. Componentes de alto nível dependendo de componentes de baixo nível
funcionar.
"""

class XMLHttpService(XMLHttpRequestService):
    pass

class Http:
    def __init__(self, xml_http_service: XMLHttpService):
        self.xml_http_service = xml_http_service
    
    def get(self, url: str, options: dict):
        self.xml_http_service.request(url, 'GET')

    def post(self, url: str, options: dict):
        self.xml_http_service.request(url, 'POST')

"""
Aqui, Http é o componente de alto nível, enquanto XMLHttpService é o componente de baixo nível
componente. Este design viola o DIP A: Módulos de alto nível não devem depender de
módulos de baixo nível. Deve depender de sua abstração.

Essa classe Http é forçada a depender da classe XMLHttpService. Se nós fôssemos
alterar o serviço de conexão Http, talvez queiramos nos conectar à internet
através do cURL ou até mesmo Mock o serviço http. Teremos que nos mover meticulosamente
através de todas as instâncias do Http para editar o código e isso viola o OCP
princípio.

A classe Http deve se importar menos com o tipo de serviço Http que você está usando. Nós fazemos
uma Interface de conexão:
"""

class Connection:
    def request(self, url: str, options: dict):
        raise NotImplementedError

"""
A interface Connection possui um método de solicitação. Com isso, passamos um argumento
do tipo Connection para nossa classe Http:
"""

class Http:
    def __init__(self, http_connection: Connection):
        self.http_connection = http_connection
    
    def get(self, url: str, options: dict):
        self.http_connection.request(url, 'GET')

    def post(self, url: str, options: dict):
        self.http_connection.request(url, 'POST')

"""
Então agora, não importa o tipo de serviço de conexão Http passado para Http, ele pode
conectar-se facilmente a uma rede sem se preocupar em saber o tipo de rede
conexão.

Agora podemos reimplementar nossa classe XMLHttpService para implementar o Connection
interface:
"""

class XMLHttpService(Connection):
    xhr = XMLHttpRequest()

    def request(self, url: str, options:dict):
        self.xhr.open()
        self.xhr.send()

"""

Podemos criar muitos tipos de conexão Http e passá-los para nossa classe Http sem
qualquer alarido sobre erros.
"""
class NodeHttpService(Connection):
    def request(self, url: str, options:dict):
        pass

class MockHttpService(Connection):
    def request(self, url: str, options:dict):
        pass

"""
Agora, podemos ver que tanto os módulos de alto nível quanto os módulos de baixo nível dependem
abstrações. A classe Http (módulo de alto nível) depende da conexão
interface (abstração) e os tipos de serviço Http (módulos de baixo nível) por sua vez,
depende da interface de conexão (abstração).

Além disso, este DIP nos forçará a não violar o Princípio da Substituição de Liskov:
Os tipos de conexão Node-XML-MockHttpService são substituíveis por seu pai
tipo Conexão.
"""
