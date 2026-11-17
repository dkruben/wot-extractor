# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/visual_script/vehicle_blocks.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from constants import NULL_ENTITY_ID as NULL_ENTITY_ID
from visual_script.block import Block as Block, Meta as Meta, InitParam as InitParam
from visual_script.misc import errorVScript as errorVScript, ASPECT as ASPECT, EDITOR_TYPE as EDITOR_TYPE
from visual_script.slot_types import SLOT_TYPE as SLOT_TYPE
from vehicle_filters import getVehicleFilters as getVehicleFilters

class VehicleMeta(Meta):
    @classmethod
    def blockColor(cls):
        ...
    @classmethod
    def blockCategory(cls):
        ...
    @classmethod
    def blockIcon(cls):
        ...

class VehicleEventsMeta(Meta):
    @classmethod
    def blockColor(cls):
        ...
    @classmethod
    def blockCategory(cls):
        ...
    @classmethod
    def blockIcon(cls):
        ...

class GetVehicleId(Block, VehicleMeta):
    _vehicle: Any
    _res: Any
    def __init__(self, *args, **kwargs):
        ...
    def _exec(self):
        ...

class GetVehicleOutfitId(Block, VehicleMeta):
    _vehicle: Any
    _id: Any
    def __init__(self, *args, **kwargs):
        ...
    def _getData(self, *args, **kwargs):
        ...

class GetVehicleOutfitLevel(Block, VehicleMeta):
    _vehicle: Any
    _level: Any
    def __init__(self, *args, **kwargs):
        ...
    def _getLevel(self):
        ...

class GetVehicleFilterName(Block, VehicleMeta):
    _filterName: Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def initParams(cls):
        ...
    @classmethod
    def blockAspects(cls):
        ...
    def captionText(self):
        ...
