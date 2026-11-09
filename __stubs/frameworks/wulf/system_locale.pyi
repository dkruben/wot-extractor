# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/frameworks/wulf/system_locale.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from .gui_constants import NumberFormatType as NumberFormatType, RealFormatType as RealFormatType
from .gui_constants import TimeFormatType as TimeFormatType, DateFormatType as DateFormatType
from .py_object_binder import PyObjectEntity as PyObjectEntity

class SystemLocale(PyObjectEntity):
    @classmethod
    def create(cls, proxy):
        ...
    def destroy(self):
        ...
    def getNumberFormat(self, value, formatType=...):
        ...
    def getRealFormat(self, value, formatType=..., fractionLen=2):
        ...
    def getTimeFormat(self, value, formatType=...):
        ...
    def getDateFormat(self, value, formatType=...):
        ...
    def caseMap(self, value, caseType):
        ...
