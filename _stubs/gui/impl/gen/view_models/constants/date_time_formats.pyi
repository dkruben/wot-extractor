# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/constants/date_time_formats.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import ViewModel as ViewModel

class DateTimeFormatsEnum(Enum):
    DAYMONTHNUMERIC = 'dayMonthNumeric'
    DAYMONTHFULL = 'dayMonthFull'
    DAYMONTHFULLTIME = 'dayMonthFullTime'
    DAYMONTHABBREVIATED = 'dayMonthAbbreviated'
    DAYMONTHABBREVIATEDTIME = 'dayMonthAbbreviatedTime'
    SHORTDATE = 'shortDate'
    SHORTTIME = 'ShortTime'
    SHORTDATETIME = 'ShortDateTime'
    FULLDATE = 'fullDate'
    FULLTIME = 'fullTime'
    FULLDATETIME = 'fullDateTime'

class DateTimeFormats(ViewModel):
    __slots__: tuple
    def __init__(self, properties=0, commands=0):
        ...
    def _initialize(self):
        ...
