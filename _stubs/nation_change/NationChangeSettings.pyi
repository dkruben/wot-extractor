# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/nation_change/NationChangeSettings.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewvalues as viewvalues
from typing import List as List, Dict as Dict, Iterable as Iterable
from items import _xml as _xml
from realm_utils import ResMgr as ResMgr

class NationGroup(object):
    __slots__: tuple
    ID: Any
    tankList: Any
    def __init__(self, ID):
        ...

class NationChangeSettings(object):
    __groupById: Any
    def __init__(self, xmlPath):
        ...
    def getGroupById(self, groupId):
        ...
    def findVehicleGroup(self, vehicleTypeName):
        ...
    def iterGroups(self):
        ...
    @staticmethod
    def __readSettings(xmlPath):
        ...
