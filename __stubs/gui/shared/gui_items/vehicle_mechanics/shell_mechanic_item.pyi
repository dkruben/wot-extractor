# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/gui_items/vehicle_mechanics/shell_mechanic_item.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.shared.gui_items.vehicle_mechanics.module_mechanic_item import ModuleMechanicItem as ModuleMechanicItem
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from items import vehicles as vehicles
from items.vehicle_mechanics_types import VehicleMechanicKey as VehicleMechanicKey, VehicleMechanicKeys as VehicleMechanicKeys
_SHELL_MECHANIC_PRIORITY: dict

# decorador original: @ReprInjector.withParent(...)
class ShellMechanicItem(ModuleMechanicItem):
    __slots__: tuple
    _GUI_SUPPORTED_MECHANICS: set
    __rank: Any
    __mechanicSubtype: Any
    def __init__(self, mechanic, *args, **kwargs):
        ...
    @property
    def hasVideo(self):
        ...
    @property
    def priority(self):
        ...
    @property
    def rank(self):
        ...
    @property
    def mechanicSubtype(self):
        ...
