# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/Scaleform/daapi/view/lobby/tooltips/epic_battle_widget_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.daapi.view.lobby.epicBattle.after_battle_reward_view_helpers import getProgressionIconVODict as getProgressionIconVODict
from gui.Scaleform.daapi.view.lobby.epicBattle.epic_helpers import getTimeToEndStr as getTimeToEndStr
from .common_blocks import packEpicBattleInfoBlock as packEpicBattleInfoBlock, packEpicBattleSeasonBlock as packEpicBattleSeasonBlock
from gui.Scaleform.genConsts.BLOCKS_TOOLTIP_TYPES import BLOCKS_TOOLTIP_TYPES as BLOCKS_TOOLTIP_TYPES
from gui.Scaleform.genConsts.PROGRESSCOLOR_CONSTANTS import PROGRESSCOLOR_CONSTANTS as PROGRESSCOLOR_CONSTANTS
from gui.game_control.epic_meta_game_ctrl import EPIC_PERF_GROUP as EPIC_PERF_GROUP
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import text_styles as text_styles, icons as icons
from gui.shared.tooltips import formatters as formatters
from gui.shared.tooltips.common import BlocksTooltipData as BlocksTooltipData
from helpers import dependency as dependency, time_utils as time_utils
from skeletons.gui.game_control import IEpicBattleMetaGameController as IEpicBattleMetaGameController

class EpicBattleWidgetTooltip(BlocksTooltipData):
    __epicController: Any
    def __init__(self, context):
        ...
    def _packBlocks(self):
        ...
    def __getCycleStatusTooltipPack(self, season):
        ...
    @staticmethod
    def __packLevelBlock(playerLevel):
        ...
    @staticmethod
    def __getPlayerProgressToLevelBlock(playerFamePts, famePtsToProgress, progressColor='orange'):
        ...
    @staticmethod
    def __getCurrentMaxProgressBlock(playerFamePts, famePtsToProgress):
        ...
    def __packPerformanceWarningBlock(self):
        ...
    def __packRewardsToChooseBlock(self, numRewards, style):
        ...
