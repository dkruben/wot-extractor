# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/gui_items/vehicle_mechanics/factories/base_factory.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems
from itertools import chain as chain
import typing as typing
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.gui_items.vehicle_mechanics.constants import MECHANIC_OVERRIDES as MECHANIC_OVERRIDES
from gui.shared.gui_items.vehicle_mechanics.interfaces import IMechanicFactory as IMechanicFactory
from items.vehicle_mechanics_types import getVehicleMechanicKey as getVehicleMechanicKey, VEHICLE_MECHANIC_VALUES as VEHICLE_MECHANIC_VALUES, VehicleMechanic as VehicleMechanic
from items.vehicle_mechanics_types import VehicleMechanicKey as VehicleMechanicKey
from items.vehicles import VehicleDescr as VehicleDescr
VehicleModule: Any
MechanicsParams: Any

class BaseMechanicFactory(IMechanicFactory):
    @classmethod
    def getMechanics(cls, guiItem, vehDescr, mechanics=None, withOverrides=False):
        ...
    @classmethod
    def _getMechanicsChecks(cls, guiItem, vehDescr):
        ...
    @classmethod
    def _getMechanicsParams(cls, _, __):
        ...
