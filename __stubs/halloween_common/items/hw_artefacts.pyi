# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/common/halloween_common/items/hw_artefacts.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from typing import TYPE_CHECKING as TYPE_CHECKING
from collections import namedtuple as namedtuple
from items.artefacts import DynComponentsGroupEquipment as DynComponentsGroupEquipment
from items import _xml as _xml
from halloween_common.hw_utils import formatVehicleInfoString as formatVehicleInfoString
from items.vehicles import VehicleDescriptor as VehicleDescriptor
HWEquipmentVariant: Any

class HWEquipment(DynComponentsGroupEquipment):
    __slots__: tuple
    equipmentItem: Any
    usageCost: Any
    variantIdFormat: Any
    variants: Any
    _fallbackVariant: Any
    def _readConfig(self, xmlCtx, scriptSection):
        ...
    @property
    def fallbackVariant(self):
        ...
    def getVariant(self, vehTypeDescr):
        ...
    @staticmethod
    def _readVariant(xmlCtx, section):
        ...
