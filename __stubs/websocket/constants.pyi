# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/websocket/constants.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum, unique as unique

# decorador original: @unique
class ConnectionStatus(Enum):
    Undefined = 0
    Opening = 1
    Opened = 2
    Failed = 3
    Closing = 4
    Closed = 5

# decorador original: @unique
class CloseStatus(Enum):
    Undefined = 0
    OmitHandshake = 1
    ForceTcpDrop = 2
    Normal = 1000
    GoingWay = 1001
    ProtocolError = 1002
    UnsupportedData = 1003
    NoStatus = 1005
    AbnormalClose = 1006
    InvalidPayload = 1007
    PolicyViolation = 1008
    MessageTooBig = 1009
    ExtensionRequired = 1010
    InternalEndpointRrror = 1011
    TryAgainLater = 1013
    BadGateway = 1014
    TlsHandshake = 1015
    SubprotocolError = 3000
    InvalidSubprotocolData = 3001

# decorador original: @unique
class OpCode(Enum):
    Continuation = 0
    Text = 1
    Binary = 2
    Rsv3 = 3
    Rsv4 = 4
    Rsv5 = 5
    Rsv6 = 6
    Rsv7 = 7
    Close = 8
    Ping = 9
    Pong = 10
    ControlRsvb = 11
    ControlRsvc = 12
    ControlRsvd = 13
    ControlRsve = 14
    ControlRsvf = 15
