# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/server_events/cond_formatters/postbattle.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from constants import ATTACK_REASON as ATTACK_REASON
from debug_utils import LOG_WARNING as LOG_WARNING, LOG_ERROR as LOG_ERROR
from dossiers2.custom.records import DB_ID_TO_RECORD as DB_ID_TO_RECORD
from gui.Scaleform.genConsts.MISSIONS_ALIASES import MISSIONS_ALIASES as MISSIONS_ALIASES
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.Scaleform.locale.QUESTS import QUESTS as QUESTS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.impl import backport as backport
from gui.server_events import formatters as events_fmts
from gui.server_events.cond_formatters import POSSIBLE_BATTLE_RESUTLS_KEYS as POSSIBLE_BATTLE_RESUTLS_KEYS, BATTLE_RESULTS_KEYS as BATTLE_RESULTS_KEYS, BATTLE_RESULTS_AGGREGATED_KEYS as BATTLE_RESULTS_AGGREGATED_KEYS, FORMATTER_IDS as FORMATTER_IDS, FormattableField as FormattableField, packDescriptionField as packDescriptionField, packSimpleTitle as packSimpleTitle, TOP_RANGE_LOWEST as TOP_RANGE_LOWEST, getResultsData as getResultsData
from gui.server_events.cond_formatters.formatters import ConditionFormatter as ConditionFormatter, SimpleMissionsFormatter as SimpleMissionsFormatter, MissionsVehicleListFormatter as MissionsVehicleListFormatter, MissionsBattleConditionsFormatter as MissionsBattleConditionsFormatter, EmptyMissionsFormatter as EmptyMissionsFormatter
from gui.server_events.formatters import RELATIONS_SCHEME as RELATIONS_SCHEME
from gui.shared.gui_items.dossier import factories as factories
from helpers import i18n as i18n
from personal_missions_constants import CONDITION_ICON as CONDITION_ICON

class MissionsPostBattleConditionsFormatter(MissionsBattleConditionsFormatter):
    def __init__(self):
        ...

class _ClanKillsFormatter(SimpleMissionsFormatter):
    def _getDescription(self, condition):
        ...
    @classmethod
    def _getIconKey(cls, condition=None):
        ...
    @classmethod
    def _getTitle(cls, condition):
        ...

class _WinFormatter(SimpleMissionsFormatter):
    def _getDescription(self, condition):
        ...
    @classmethod
    def _getIconKey(cls, condition=None):
        ...
    @classmethod
    def _getTitle(cls, *args, **kwargs):
        ...

class _PMWinFormatter(_WinFormatter):
    def _getDescription(self, condition):
        ...

class _SurviveFormatter(SimpleMissionsFormatter):
    def _getDescription(self, condition):
        ...
    @classmethod
    def _getIconKey(cls, condition=None):
        ...
    @classmethod
    def _getTitle(cls, *args, **kwargs):
        ...

class _PMSurviveFormatter(_SurviveFormatter):
    def _getDescription(self, condition):
        ...

class _AchievementsFormatter(SimpleMissionsFormatter):
    def _getDescription(self, condition):
        ...
    @classmethod
    def _getIconKey(cls, condition=None):
        ...
    def _packGui(self, condition):
        ...
    @classmethod
    def _getTitle(cls, *args, **kwargs):
        ...

class VehiclesKillFormatter(MissionsVehicleListFormatter):
    @classmethod
    def _getIconKey(cls, condition=None):
        ...
    @classmethod
    def _getTitleKey(cls, condition=None):
        ...

class VehiclesDamageFormatter(MissionsVehicleListFormatter):
    UTILITY_DAMAGE_TAGS: set
    @classmethod
    def _getIconKey(cls, condition=None):
        ...
    @classmethod
    def _getTitleKey(cls, condition=None):
        ...

class VehiclesStunFormatter(MissionsVehicleListFormatter):
    @classmethod
    def _getIconKey(cls, condition=None):
        ...
    @classmethod
    def _getTitleKey(cls, condition=None):
        ...

class _MultiStunEventFormatter(SimpleMissionsFormatter):
    @classmethod
    def _getDescription(cls, condition):
        ...
    @classmethod
    def _getIconKey(cls, condition=None):
        ...
    @classmethod
    def _getTitle(cls, condition):
        ...
    @classmethod
    def _getTitleKey(cls, condition=None):
        ...

class _FirstBloodFormatter(EmptyMissionsFormatter):
    ...

class _BattleResultsFormatter(SimpleMissionsFormatter):
    @classmethod
    def _getTitle(cls, condition):
        ...
    def _getDescription(self, condition):
        ...
    @classmethod
    def _getIconKey(cls, condition=None):
        ...
    def _getSortKey(self, condition):
        ...

class _UnitResultsFormatter(SimpleMissionsFormatter):
    def _format(self, condition, event):
        ...
    def _getDescription(self, condition):
        ...
    @classmethod
    def _getIconKey(cls, condition=None):
        ...

class _CritFormatter(SimpleMissionsFormatter):
    @classmethod
    def _getTitle(cls, condition):
        ...
    def _getDescription(self, condition):
        ...
    @classmethod
    def _getIconKey(cls, condition=None):
        ...

class _VehicleBlockedByArmorFormatter(MissionsVehicleListFormatter):
    @classmethod
    def _getDescription(cls, condition=None):
        ...
    @classmethod
    def _getIconKey(cls, condition=None):
        ...
    @classmethod
    def _getTitleKey(cls, condition=None):
        ...

class _CritsFormatter(ConditionFormatter):
    def _format(self, condition, event):
        ...

def _packAchieveElement(achieveRecordID):
    ...
def _packAchievementsList(achivementsIDs):
    ...
def _makeKeyNegativeIf(key, cond):
    ...
