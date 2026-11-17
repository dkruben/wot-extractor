# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/gui_items/vehicle_mechanics/module_mechanic_item.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.impl.gen.view_models.common.vehicle_mechanic_model import MechanicsEnum as MechanicsEnum
from gui.shared.gui_items.gui_item import GUIItem as GUIItem
from gui.shared.gui_items.vehicle_mechanics.constants import VEHICLE_MECHANICS_GUI_MAP as VEHICLE_MECHANICS_GUI_MAP
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from items.vehicle_mechanics_types import VehicleMechanicKey as VehicleMechanicKey, VehicleMechanicKeys as VehicleMechanicKeys
VehicleModule: Any

# decorador original: @ReprInjector.simple(...)
class ModuleMechanicItem(GUIItem):
    __slots__: tuple
    _GUI_SUPPORTED_MECHANICS: dict
    _EXTRA_STATUSES: dict
    _mechanic: Any
    def __init__(self, mechanic, *args, **kwargs):
        ...
    @property
    def isHidden(self):
        ...
    @property
    def guiName(self):
        ...
    @property
    def mechanic(self):
        ...
    def getExtraStatuses(self, _):
        ...

class GunMechanicItem(ModuleMechanicItem):
    _GUI_SUPPORTED_MECHANICS: set
    _EXTRA_STATUSES: set

class EngineMechanicItem(ModuleMechanicItem):
    _GUI_SUPPORTED_MECHANICS: set
    _EXTRA_STATUSES: set

class ChassisMechanicItem(ModuleMechanicItem):
    _GUI_SUPPORTED_MECHANICS: set
    _EXTRA_STATUSES: set
    def getExtraStatuses(self, module):
        ...
