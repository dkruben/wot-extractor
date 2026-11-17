# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/gui_items/vehicle_mechanics/vehicle_mechanic_item.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui import GUI_SETTINGS as GUI_SETTINGS
from gui.impl.gen.view_models.common.vehicle_mechanic_model import MechanicsEnum as MechanicsEnum, MechanicsRank as MechanicsRank
from gui.shared.gui_items.gui_item import GUIItem as GUIItem
from gui.shared.gui_items.vehicle_mechanics.constants import VEHICLE_MECHANICS_GUI_MAP as VEHICLE_MECHANICS_GUI_MAP
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from items import vehicles as vehicles
from items.vehicle_mechanics_types import VehicleMechanicKey as VehicleMechanicKey

# decorador original: @ReprInjector.simple(...)
class VehicleMechanicItem(GUIItem):
    __slots__: tuple
    __mechanic: Any
    __vehIntCD: Any
    def __init__(self, mechanic, vehIntCD):
        ...
    @property
    def isHidden(self):
        ...
    @property
    def hasVideo(self):
        ...
    @property
    def guiName(self):
        ...
    @property
    def mechanic(self):
        ...
    @property
    def priority(self):
        ...
    @property
    def rank(self):
        ...
    @property
    def staticParams(self):
        ...
    def __getMechanicProperties(self):
        ...
