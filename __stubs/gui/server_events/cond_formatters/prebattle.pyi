# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/server_events/cond_formatters/prebattle.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import ArenaType as ArenaType
from constants import ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from gui.Scaleform.locale.QUESTS import QUESTS as QUESTS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.server_events import formatters as formatters
from gui.server_events.cond_formatters import packSimpleTitle as packSimpleTitle, packDescriptionField as packDescriptionField
from gui.server_events.cond_formatters.formatters import ConditionFormatter as ConditionFormatter, MissionsBattleConditionsFormatter as MissionsBattleConditionsFormatter, SimpleMissionsFormatter as SimpleMissionsFormatter
from gui.shared.formatters import icons as icons, text_styles as text_styles
from gui.shared.utils.functions import makeTooltip as makeTooltip
from helpers import i18n as i18n
from items.vehicles import CAMOUFLAGE_KINDS as CAMOUFLAGE_KINDS
from personal_missions_constants import CONDITION_ICON as CONDITION_ICON
from shared_utils import findFirst as findFirst
from soft_exception import SoftException as SoftException
ICON_SIZE = 32
VERTICAL_SPACE = -11

class MissionsPreBattleConditionsFormatter(MissionsBattleConditionsFormatter):
    def __init__(self):
        ...
    def format(self, conditions, event):
        ...
    def _packCondition(self, *args, **kwargs):
        ...
    def _getFormattedField(self, *args, **kwargs):
        ...
    def _packConditions(self, *args, **kwargs):
        ...

class _BattleBonusTypeFormatter(ConditionFormatter):
    def _format(self, condition, event):
        ...

class _BattleSquadFormatter(ConditionFormatter):
    def _format(self, condition, event):
        ...

class _BattleClanMembershipFormatter(ConditionFormatter):
    def _format(self, condition, event):
        ...

class _BattleCamouflageFormatter(ConditionFormatter):
    def _format(self, condition, event):
        ...

class _BattleMapFormatter(ConditionFormatter):
    def _format(self, condition, event):
        ...

class _InstalledModulesGroupFormatter(ConditionFormatter):
    def _format(self, condition, event):
        ...

class _InstalledItemsConditionFormatter(SimpleMissionsFormatter):
    @classmethod
    def _getTitle(cls, condition):
        ...
    @classmethod
    def _getIconKey(cls, condition=None):
        ...
    def _getDescription(self, condition):
        ...

class _CorrespondedCamouflageFormatter(SimpleMissionsFormatter):
    def _getDescription(self, condition):
        ...
    @classmethod
    def _getIconKey(cls, condition=None):
        ...
    @classmethod
    def _getTitle(cls, *args, **kwargs):
        ...
