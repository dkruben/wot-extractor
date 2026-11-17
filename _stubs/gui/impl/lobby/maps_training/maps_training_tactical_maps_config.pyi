# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/maps_training/maps_training_tactical_maps_config.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
import ResMgr as ResMgr
from maps_training_common.maps_training_constants import VEHICLE_CLASSES_ORDER as VEHICLE_CLASSES_ORDER
MapConfig: Any
Team: Any
Point: Any
Scenario: Any
_BASE_OFFSET: tuple
_POINT_OFFSET: tuple

class TacticalMapsConfig(object):
    _mapsData: Any
    def __init__(self, mapsData):
        ...
    def getMapConfig(self, geometryName):
        ...

class TacticalMapsConfigReader(object):
    @staticmethod
    def readXml(xmlPath):
        ...
