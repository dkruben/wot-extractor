# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/points_of_interest/components.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import enum as enum
import typing as typing
from points_of_interest_shared import PoiType as PoiType
from helpers.fixed_dict import StatusWithTimeInterval as StatusWithTimeInterval
from points_of_interest.mixins import PointsOfInterestListener as PointsOfInterestListener

# decorador original: @enum.unique
class PoiStateUpdateMask(enum.IntEnum):
    NONE = 0
    PROGRESS = 1
    INVADER = 2
    STATUS = 4
    ALL: Any

class PoiStateComponent(object):
    __slots__: tuple
    id: Any
    type: Any
    _progress: Any
    _invader: Any
    _status: Any
    _updatedFields: Any
    def __init__(self, poiID, poiType, progress, invader, status):
        ...
    @property
    def progress(self):
        ...
    @progress.setter
    def progress(self, progress):
        ...
    @property
    def invader(self):
        ...
    @invader.setter
    def invader(self, invader):
        ...
    @property
    def status(self):
        ...
    @status.setter
    def status(self, status):
        ...
    @property
    def updatedFields(self):
        ...
    def resetUpdatedFields(self):
        ...

class PoiStateUIListenerComponent(object):
    __slots__: tuple
    listener: Any
    def __init__(self, listener):
        ...

class PoiCaptureBlockerStateComponent(object):
    __slots__: tuple
    id: Any
    blockReasons: Any
    def __init__(self, poiID, blockReasons):
        ...

class PoiVehicleStateComponent(object):
    __slots__: tuple
    id: Any
    def __init__(self, poiID):
        ...
