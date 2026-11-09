# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/tank_setup/backports/tooltips.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.impl.backport import createTooltipData as createTooltipData
from gui.impl.gen.view_models.views.lobby.tank_setup.tank_setup_constants import TankSetupConstants as TankSetupConstants
from gui.impl.gen.view_models.views.lobby.tank_setup.tank_setup_fields import TankSetupFields as TankSetupFields
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.game_control import ILoadoutController as ILoadoutController
_PanelSlotTooltip: Any
PANEL_SLOT_TOOLTIPS: dict

class HangarModuleTooltipBuilder(object):
    itemsCache: Any
    @classmethod
    def getPanelSlotTooltip(cls, vehicle, slotID, intCD=None):
        ...
    @classmethod
    def getInSlotTooltipData(cls, vehicle, slotID, intCD):
        ...
    @classmethod
    def getTooltipData(cls, vehicle, slotID, intCD):
        ...
    @classmethod
    def getEmptyTooltip(cls, *args):
        ...
    @classmethod
    def getSpecialInfoSlotTooltip(cls, *args):
        ...
    @classmethod
    def getVehicle(cls, vehicle, currentSection=None):
        ...
    @classmethod
    def _getTooltipSpecialAlias(cls):
        ...
    @classmethod
    def _getInSlotTooltipAlias(cls):
        ...
    @classmethod
    def _getSlotItem(cls, vehicle, slotID):
        ...

class OptDeviceTooltipBuilder(HangarModuleTooltipBuilder):
    __loadoutController: Any
    @classmethod
    def getEmptyTooltip(cls, vehicle, slotID, intCD):
        ...
    @classmethod
    def getVehicle(cls, vehicle, currentSection=None):
        ...
    @classmethod
    def _getInSlotTooltipAlias(cls):
        ...
    @classmethod
    def _getSlotItem(cls, vehicle, slotID):
        ...

class ConsumableToolitpBuilder(HangarModuleTooltipBuilder):
    __loadoutController: Any
    @classmethod
    def getEmptyTooltip(cls, *args):
        ...
    @classmethod
    def getVehicle(cls, vehicle, currentSection=None):
        ...
    @classmethod
    def _getSlotItem(cls, vehicle, slotID):
        ...

class BattleBoostersTooltipBuilder(HangarModuleTooltipBuilder):
    itemsCache: Any
    __loadoutController: Any
    @classmethod
    def getEmptyTooltip(cls, *_):
        ...
    @classmethod
    def getVehicle(cls, vehicle, currentSection=None):
        ...
    @classmethod
    def _getTooltipSpecialAlias(cls):
        ...
    @classmethod
    def _getInSlotTooltipAlias(cls):
        ...
    @classmethod
    def _getSlotItem(cls, vehicle, slotID):
        ...

class VehModuleTooltipBuilder(HangarModuleTooltipBuilder):
    ...

class ShellTooltipBuilder(HangarModuleTooltipBuilder):
    itemsCache: Any
    __loadoutController: Any
    @classmethod
    def _getSlotItem(cls, vehicle, slotID):
        ...
    @classmethod
    def _getInSlotTooltipAlias(cls):
        ...
    @classmethod
    def _getTooltipSpecialAlias(cls):
        ...
    @classmethod
    def getVehicle(cls, vehicle, currentSection=None):
        ...

class BattleAbilitiesToolitpBuilder(HangarModuleTooltipBuilder):
    itemsCache: Any
    @classmethod
    def getInSlotTooltipData(cls, vehicle, slotID, intCD):
        ...
    @classmethod
    def getTooltipData(cls, _, slotID, intCD):
        ...
    @classmethod
    def getEmptyTooltip(cls, *_):
        ...
    @classmethod
    def getSpecialInfoSlotTooltip(cls, vehicle, slotID, intCD):
        ...
    @classmethod
    def getVehicle(cls, vehicle, currentSection=None):
        ...
    @classmethod
    def _getSlotItem(cls, vehicle, slotID):
        ...

def getSlotTooltipData(event, vehicle, currentSlotID, currentSection=None, tooltipsMap=None):
    ...
def getSlotSpecTooltipData(event, tooltipId):
    ...
def getShellsPriceDiscountTooltipData(event, tooltipId):
    ...
