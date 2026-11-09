# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/gui_items/vehicle_adjusters.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from gui.Scaleform.daapi.view.lobby.vehicle_compare import cmp_helpers as cmp_helpers
from helpers import dependency as dependency
from adisp import adisp_process as adisp_process
from debug_utils import LOG_WARNING as LOG_WARNING
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.gui_items.processors import module as installer_module
from items import tankmen as tankmen
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from gui.shared.gui_items.fitting_item import FittingItem as FittingItem

# decorador original: @adisp_process
def installModulesSet(vehicle, modules, notFitted):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def installEquipment(vehicle, intCD, slotIndex, itemsCache=None):
    ...
def swapEquipment(vehicle, leftID, rightID):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def installOptionalDevice(vehicle, newId, slotIndex, itemsCache=None):
    ...
def removeOptionalDevice(vehicle, slotIndex):
    ...
def swapOptionalDevice(vehicle, leftID, rigthID):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def installBattleBoosterOnVehicle(vehicle, intCD, itemsCache=None):
    ...
def changeShell(vehicle, slotIndex):
    ...
def applyTankmanSkillOnVehicle(vehicle, skillsByRolesIdx):
    ...
