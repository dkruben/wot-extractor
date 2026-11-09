# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/formatters/personal_reserves.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.impl import backport as backport
from gui.impl.gen import R as R
from helpers import html as html
from messenger import g_settings as g_settings
from messenger.formatters.service_channel import GeneralFormatter as GeneralFormatter

class IPersonalReservesFormatter(GeneralFormatter):
    def __init__(self):
        ...

class IPersonalReservesExpirableFormatter(GeneralFormatter):
    def __init__(self):
        ...

class ReleaseFormatter(IPersonalReservesFormatter):
    def getTitle(self, message, *args):
        ...
    def getText(self, message, *args):
        ...

class PersonalReservesSoonExpirationFormatter(IPersonalReservesExpirableFormatter):
    def getTitle(self, message, *args):
        ...
    def getText(self, message, *args):
        ...
