# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/Scaleform/daapi/view/battle/tooltips/epic_skills.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems, viewvalues as viewvalues
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from debug_utils import LOG_ERROR as LOG_ERROR
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.Scaleform.genConsts.BLOCKS_TOOLTIP_TYPES import BLOCKS_TOOLTIP_TYPES as BLOCKS_TOOLTIP_TYPES
from gui.shared.gui_items.Vehicle import VEHICLE_CLASS_NAME as VEHICLE_CLASS_NAME, Vehicle as Vehicle
from gui.shared.formatters import text_styles as text_styles, icons as icons
from gui.shared.tooltips import TOOLTIP_TYPE as TOOLTIP_TYPE
from gui.shared.tooltips import formatters as formatters
from gui.shared.tooltips.common import BlocksTooltipData as BlocksTooltipData
from gui.shared.tooltips.battle_ability_tooltip_params import g_battleAbilityTooltipMgr as g_battleAbilityTooltipMgr
from gui.shared.utils.functions import replaceHyphenToUnderscore as replaceHyphenToUnderscore
from helpers import dependency as dependency
from skeletons.gui.game_control import IEpicBattleMetaGameController as IEpicBattleMetaGameController
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.shared.tooltips.advanced import BaseAdvancedTooltip as BaseAdvancedTooltip, MODULE_MOVIES as MODULE_MOVIES
_TOOLTIP_MIN_WIDTH = 460
_SETUP_INFO_TOOLTIP_MIN_WIDTH = 440

class EpicSkillBaseTooltipData(BlocksTooltipData):
    _epicMetaGameCtrl: Any
    _itemsCache: Any
    def __init__(self, ctx):
        ...
    def _packBlocks(self, skillID, level=None):
        ...
    @staticmethod
    def _constructHeader(skillInfo):
        ...
    def __constructDescr(self, skillLevel):
        ...
    def __constructStatsBlock(self, skillInfo):
        ...
    @staticmethod
    def __constructModesInfoBlock(isPurchased):
        ...
    @staticmethod
    def __constructInactiveStateBlock(skillInfo):
        ...

class EpicSkillSlotTooltipAdvanced(BaseAdvancedTooltip):
    _epicMetaGameCtrl: Any
    def _getBlocksList(self, *args, **kwargs):
        ...

class EpicSkillSlotTooltip(EpicSkillBaseTooltipData):
    def _packBlocks(self, skillID, _=None):
        ...

class EpicSkillSlotSetupInfoTooltip(BlocksTooltipData):
    _epicMetaGameCtrl: Any
    _itemsCache: Any
    def __init__(self, ctx):
        ...
    def _packBlocks(self, vehicleCD=None):
        ...

def _equipmentToEpicSkillConverter(epicMetaGameCtrl, eqCompDescr):
    ...
