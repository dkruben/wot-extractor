# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/missions/cards_formatters.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from debug_utils import LOG_ERROR as LOG_ERROR
from gui.Scaleform.genConsts.MISSIONS_ALIASES import MISSIONS_ALIASES as MISSIONS_ALIASES
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.Scaleform.locale.QUESTS import QUESTS as QUESTS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.server_events import formatters as formatters
from gui.server_events.cond_formatters import CONDITION_SIZE as CONDITION_SIZE, FORMATTER_IDS as FORMATTER_IDS, FormattableField as FormattableField, getCondIconBySize as getCondIconBySize, postbattle as postbattle
from gui.server_events.cond_formatters.bonus import BattlesCountFormatter as BattlesCountFormatter, MissionsBonusConditionsFormatter as MissionsBonusConditionsFormatter
from gui.server_events.cond_formatters.formatters import ConditionsFormatter as ConditionsFormatter
from gui.server_events.cond_formatters.tokens import TokensConditionFormatter as TokensConditionFormatter
from gui.server_events.formatters import TOKEN_SIZES as TOKEN_SIZES
from gui.shared.formatters import icons as icons, text_styles as text_styles
from gui.shared.utils.functions import makeTooltip as makeTooltip
from helpers import i18n as i18n
from personal_missions_constants import CONDITION_ICON as CONDITION_ICON
from soft_exception import SoftException as SoftException
MAX_ACHIEVEMENTS_IN_TOOLTIP = 5
CARD_FIELDS_FORMATTERS: dict
NORMAL_FORMATTERS: dict
MINIMIZED_FORMATTERS: dict

class MissionBonusAndPostBattleCondFormatter(ConditionsFormatter):
    bonusCondFormatter: Any
    postBattleCondFormatter: Any
    def __init__(self):
        ...
    def format(self, event):
        ...
    @classmethod
    def _packSeparator(cls, key):
        ...

class CardBattleConditionsFormatters(MissionBonusAndPostBattleCondFormatter):
    MAX_CONDITIONS_IN_CARD = 3
    MAX_DESC_LINES = 3
    ALT_DESCR_LINES = 2
    ICON_SIZE = CONDITION_SIZE.MINIMIZED
    _formatters: Any
    def __init__(self):
        ...
    def format(self, event):
        ...
    def _getFormattedField(self, field):
        ...
    @classmethod
    def _packSeparator(cls, key):
        ...
    def _packCondition(self, preFormattedCondition, maxDescLines=...):
        ...
    def _packConditions(self, preFormattedConditions, maxDescLines=...):
        ...

class DetailedCardBattleConditionsFormatters(MissionBonusAndPostBattleCondFormatter):
    MAX_CONDITIONS_IN_CARD = 6
    MAX_CONDITIONS_IN_ROW = 3
    MAX_OR_SECTIONS = 2
    MAX_LINES_IN_DESCR = 3
    MIN_LINES_IN_DESCR = 2
    _formatters: Any
    def __init__(self):
        ...
    def format(self, event):
        ...
    def _packConditions(self, size, conditions):
        ...
    def _packCondition(self, size, preFormattedCondition):
        ...
    @classmethod
    def _packSeparator(cls, key):
        ...
    def _getFormattedField(self, size, formattableField):
        ...
    def __andFormat(self, result):
        ...
    def __orFormat(self, result):
        ...

class CardTokenConditionFormatter(ConditionsFormatter):
    MAX_TOKENS_COUNT = 3
    tokensCondFormatter: Any
    def __init__(self):
        ...
    def format(self, event):
        ...
    def getPreformattedConditions(self, event):
        ...
    @classmethod
    def _getLabel(cls, preFormattedCondition):
        ...
    @classmethod
    def _getIconData(cls, preFormattedCondition):
        ...
    @classmethod
    def _packBattleCondition(cls, preFormattedCondition):
        ...
    def _packConditions(self, preFormattedConditions):
        ...
    def _packFullCondition(self, preFormattedCondition, popoverEnable):
        ...
    def __packSimplifiedCondition(self, preFormattedCondition, popoverEnable):
        ...
    def _packConditionFromDescription(self, event):
        ...
    def _packCondition(self, *args, **kwargs):
        ...
    def _getFormattedField(self, *args, **kwargs):
        ...

class DetailedCardTokenConditionFormatter(CardTokenConditionFormatter):
    @classmethod
    def _packBattleCondition(cls, preFormattedCondition):
        ...
    @classmethod
    def _getLabel(cls, preFormattedCondition):
        ...
    @classmethod
    def _getIconData(cls, preFormattedCondition):
        ...
    def _packConditions(self, preFormattedConditions):
        ...
    def _packConditionFromDescription(self, event):
        ...

def _packNoGuiCondition(event):
    ...
def _packProgress(preFormattedCondition):
    ...
def _getTooltipData(conditionData):
    ...
def _packAchievementsTooltipData(data):
    ...
def _packPlayBattleCondition():
    ...
