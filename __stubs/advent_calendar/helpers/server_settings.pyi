# wot-extractor: STUB (.pyi) gerado a partir de sources/res/advent_calendar/scripts/client/advent_calendar/helpers/server_settings.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from collections import namedtuple as namedtuple

# base nao representavel no stub: namedtuple(...)
class AdventCalendarConfig:
    __slots__: tuple
    def __new__(cls, **kwargs):
        ...
    def asDict(self):
        ...
    def replace(self, data):
        ...
    @property
    def doorsCount(self):
        ...
    def isSpecialDay(self, dayId):
        ...
