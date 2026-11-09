# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/gui_items/vehicle_mechanics/interfaces.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from typing import Set as Set, Optional as Optional
from items.vehicle_mechanics_types import VehicleMechanicKey as VehicleMechanicKey
from items.vehicles import VehicleDescr as VehicleDescr
VehicleModule: Any

class IMechanicFactory(object):
    @classmethod
    def getMechanics(cls, guiItem, vehDescr, mechanics=None, withOverrides=False):
        ...
