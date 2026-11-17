# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/tank_setup/tank_setup_helper.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from BWUtil import AsyncReturn as AsyncReturn
from frameworks.wulf.view.array import fillViewModelsArray as fillViewModelsArray
from gui.impl.lobby.tank_setup.tank_setup_sounds import playSlotActionSound as playSlotActionSound
from gui.impl.gen.view_models.common.vehicle_mechanic_model import MechanicsEnum as MechanicsEnum, VehicleMechanicModel as VehicleMechanicModel
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.shell_mechanic_subtypes_model import ShellMechanicSubtypesModel as ShellMechanicSubtypesModel
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.shell_mechanic_column_config_model import ShellMechanicColumnConfigModel as ShellMechanicColumnConfigModel
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.shell_specification_model import ShellSpecificationModel as ShellSpecificationModel
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.param_value_model import ParamValueModel as ParamValueModel, MechanicState as MechanicState
from gui.impl.lobby.common.vehicle_model_helpers import fillVehicleMechanicModel as fillVehicleMechanicModel
from gui.shared.gui_items.vehicle_mechanics.constants import VEHICLE_MECHANICS_GUI_MAP as VEHICLE_MECHANICS_GUI_MAP
from gui.shared.items_parameters.formatters import formatParameter as formatParameter, MEASURE_UNITS as MEASURE_UNITS
from gui.shared.items_parameters.shell_mechanics_helper import ShellMechanicState as ShellMechanicState
from helpers import i18n as i18n
from items.components.supply_slot_categories import SlotCategories as SlotCategories
from wg_async import wg_async as wg_async, wg_await as wg_await, await_callback as await_callback
from gui.shared.gui_items.vehicle_mechanics.shell_mechanic_item import ShellMechanicItem as ShellMechanicItem
from items.vehicle_mechanics_types import VehicleMechanicKey as VehicleMechanicKey
_logger: Any
NONE_ID = -1
_CATEGORY_MASK: dict
_MECHANIC_STATES: dict
_MECHANIC_SUBTYPE_TO_STATE: dict

class TankSetupAsyncCommandLock(object):
    __slots__: tuple
    __inProcess: Any
    def __init__(self):
        ...
    @property
    def isLocked(self):
        ...
    # decorador original: @wg_async
    def tryAsyncCommand(self, func, *args, **kwargs):
        ...
    # decorador original: @wg_async
    def tryAsyncCommandWithCallback(self, func, *args, **kwargs):
        ...
    def _lock(self):
        ...
    def _unlock(self):
        ...

def createShellSpecificationModel(paramName, parameters, mechanic):
    ...
def createShellMechanicsModels(shellMechanicItems, minPriority=0):
    ...
def createShellMechanicsSubtypesModel(shellMechanicItems, minPriority=0):
    ...
def getCategoriesMask(categories):
    ...
def setLastSlotAction(viewModel, vehicle, setupName, actionType, intCD=..., slotID=..., leftID=..., rightID=..., leftIntCD=..., rightIntCD=...):
    ...
def clearLastSlotAction(viewModel):
    ...
