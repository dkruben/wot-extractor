# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/tooltips/achievement.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import constants as constants
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from debug_utils import LOG_ERROR as LOG_ERROR
from gui.Scaleform.genConsts.BLOCKS_TOOLTIP_TYPES import BLOCKS_TOOLTIP_TYPES as BLOCKS_TOOLTIP_TYPES
from gui.shared.formatters import text_styles as text_styles
from gui.shared.utils import getPlayerName as getPlayerName
from helpers import dependency as dependency
from helpers.i18n import makeString as makeString
from dossiers2.custom.config import RECORD_CONFIGS as RECORD_CONFIGS
from dossiers2.ui.achievements import MARK_OF_MASTERY_RECORD as MARK_OF_MASTERY_RECORD
from gui.shared.tooltips import ToolTipParameterField as ToolTipParameterField, ToolTipDataField as ToolTipDataField, ToolTipData as ToolTipData, ToolTipMethodField as ToolTipMethodField, ToolTipBaseData as ToolTipBaseData, TOOLTIP_TYPE as TOOLTIP_TYPE, formatters as formatters
from gui.shared.tooltips.common import BlocksTooltipData as BlocksTooltipData
from gui.shared.gui_items.dossier.achievements.abstract import achievementHasVehiclesList as achievementHasVehiclesList, isSeriesAchievement as isSeriesAchievement
from skeletons.gui.shared import IItemsCache as IItemsCache
_ACHIEVEMENT_VEHICLES_MAX = 5
_ACHIEVEMENT_VEHICLES_SHOW = 5
_logger: Any

class AchievementParamsField(ToolTipParameterField):
    def _getValue(self):
        ...

class AchievementStatsField(ToolTipDataField):
    def _getValue(self):
        ...

class AchievementIsInDossierField(ToolTipDataField):
    def _getValue(self):
        ...

class AchievementRecordsField(ToolTipDataField):
    itemsCache: Any
    def _getValue(self):
        ...

class AchievementTooltipData(ToolTipData):
    fields: Any
    def __init__(self, context):
        ...

class GlobalRatingTooltipData(ToolTipBaseData):
    def __init__(self, context):
        ...
    def getDisplayableData(self, *args):
        ...

class BadgeTooltipData(BlocksTooltipData):
    def __init__(self, context):
        ...
    def _packBlocks(self, badgeID):
        ...
