# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/session_stats/session_stats_tooltips.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from collections import namedtuple as namedtuple
from account_helpers.settings_core.settings_constants import SESSION_STATS as SESSION_STATS
from constants import ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from dossiers2.ui.achievements import MARK_ON_GUN_RECORD as MARK_ON_GUN_RECORD
from gui.Scaleform.daapi.view.lobby.session_stats.shared import packLastBattleData as packLastBattleData, packBattleEfficiencyData as packBattleEfficiencyData, packEfficiencyPropData as packEfficiencyPropData, packTotalPropData as packTotalPropData
from gui.Scaleform.genConsts.BLOCKS_TOOLTIP_TYPES import BLOCKS_TOOLTIP_TYPES as BLOCKS_TOOLTIP_TYPES
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.Scaleform.genConsts.SESSION_STATS_CONSTANTS import SESSION_STATS_CONSTANTS as SESSION_STATS_CONSTANTS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import text_styles as text_styles
from gui.shared.gui_items.dossier.achievements import isMarkOfMasteryAchieved as isMarkOfMasteryAchieved
from gui.shared.tooltips import formatters as formatters
from gui.shared.tooltips.common import BlocksTooltipData as BlocksTooltipData
from helpers import dependency as dependency, int2roman as int2roman
from skeletons.gui.shared import IItemsCache as IItemsCache
_logger: Any
TankStatsHeaderVO: Any
TankBattleResultsStatsVO: Any
TankBattleEfficiencyStatsVO: Any
TankStatusVO: Any
_TANK_MASTER_TYPES_TEXT: list
_MARK_ON_GUN_ICONS: list
_TOTAL_BLOCK_PARAMS: list

class SessionStatsEfficiencyParam(BlocksTooltipData):
    itemsCache: Any
    _propId: Any
    def __init__(self, context):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...
    def _packInfoBlocks(self):
        ...

class SessionStatsTankInfo(BlocksTooltipData):
    itemsCache: Any
    smallLayout: Any
    vehicle: Any
    _headerPadding: Any
    randomStats: Any
    vehicleStats: Any
    def __init__(self, context):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...
    def _packTankBlocks(self):
        ...
    def _packStatusBlock(self):
        ...
    def _getStatusData(self):
        ...
    def _packBattleResultsBlock(self):
        ...
    def _getBattleResultsData(self):
        ...
    def _packBattleEfficiencyBlock(self):
        ...
    def _getBattleEfficiencyData(self):
        ...
    def _packHeaderBlock(self):
        ...
    def _getHeaderBlockData(self):
        ...
    def _getTankParamsVO(self, smallLayout=False):
        ...
    @staticmethod
    def _getTankParamVO(text, icon):
        ...
    @staticmethod
    def _tankNameToRClassName(name):
        ...
    def _getTankIcon(self):
        ...
