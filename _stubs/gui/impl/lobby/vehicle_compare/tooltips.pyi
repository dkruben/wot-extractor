# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/vehicle_compare/tooltips.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.daapi.view.lobby.vehicle_compare import cmp_helpers as cmp_helpers
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.Scaleform.locale.VEH_COMPARE import VEH_COMPARE as VEH_COMPARE
from gui.impl.backport import createTooltipData as createTooltipData
from gui.impl.gen.view_models.views.lobby.tank_setup.tank_setup_constants import TankSetupConstants as TankSetupConstants
from gui.impl.lobby.tank_setup.backports.tooltips import OptDeviceTooltipBuilder as OptDeviceTooltipBuilder, ConsumableToolitpBuilder as ConsumableToolitpBuilder, BattleBoostersTooltipBuilder as BattleBoostersTooltipBuilder, ShellTooltipBuilder as ShellTooltipBuilder, getSlotTooltipData as getSlotTooltipData
from gui.shared.utils.functions import makeTooltip as makeTooltip
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
CMP_PANEL_SLOT_TOOLTIPS: dict

class CmpOptDeviceTooltipBuilder(OptDeviceTooltipBuilder):
    @classmethod
    def _getTooltipSpecialAlias(cls):
        ...
    @classmethod
    def _getInSlotTooltipAlias(cls):
        ...

class CmpConsumableToolitpBuilder(ConsumableToolitpBuilder):
    _itemsCache: Any
    @classmethod
    def getTooltipData(cls, vehicle, slotID, intCD):
        ...
    @classmethod
    def _getTooltipSpecialAlias(cls):
        ...

class CmpBattleBoostersTooltipBuilder(BattleBoostersTooltipBuilder):
    itemsCache: Any
    @classmethod
    def _getTooltipSpecialAlias(cls):
        ...
    @classmethod
    def _getInSlotTooltipAlias(cls):
        ...

class CmpShellTooltipBuilder(ShellTooltipBuilder):
    itemsCache: Any
    @classmethod
    def getPanelSlotTooltip(cls, vehicle, slotID, *_):
        ...
    @classmethod
    def _getTooltipSpecialAlias(cls):
        ...

class CmpCamouflageTooltipBuilder(object):
    itemsCache: Any
    @classmethod
    def getPanelSlotTooltip(cls, *_):
        ...
    @classmethod
    def getTooltipData(cls, *_):
        ...
    @classmethod
    def getVehicle(cls, vehicle, _=None):
        ...

def getCmpSlotTooltipData(event, vehicle, currentSlotID=None, currentSection=None):
    ...
