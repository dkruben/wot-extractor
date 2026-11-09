# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/server_events/cond_formatters/bonus.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from debug_utils import LOG_WARNING as LOG_WARNING, LOG_ERROR as LOG_ERROR
from gui.Scaleform.genConsts.MISSIONS_ALIASES import MISSIONS_ALIASES as MISSIONS_ALIASES
from gui.Scaleform.locale.QUESTS import QUESTS as QUESTS
from gui.server_events import formatters as formatters
from gui.server_events.cond_formatters import POSSIBLE_BATTLE_RESUTLS_KEYS as POSSIBLE_BATTLE_RESUTLS_KEYS, BATTLE_RESULTS_KEYS as BATTLE_RESULTS_KEYS, FORMATTER_IDS as FORMATTER_IDS, FormattableField as FormattableField, packDescriptionField as packDescriptionField
from personal_missions_constants import CONDITION_ICON as CONDITION_ICON
from gui.server_events.cond_formatters.formatters import CumulativableFormatter as CumulativableFormatter, MissionFormatter as MissionFormatter, MissionsVehicleListFormatter as MissionsVehicleListFormatter, MissionsBattleConditionsFormatter as MissionsBattleConditionsFormatter
from gui.server_events.cond_formatters.postbattle import VehiclesDamageFormatter as VehiclesDamageFormatter
from gui.server_events.cond_formatters.postbattle import VehiclesKillFormatter as VehiclesKillFormatter
from gui.server_events.cond_formatters.postbattle import VehiclesStunFormatter as VehiclesStunFormatter
from helpers import i18n as i18n, dependency as dependency
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared import IItemsCache as IItemsCache
ZERO_COUNT = 0
DEFAULT_GROUP_BY_KEY = None
GROUP_BY_FORMATTERS_DATA: dict

class MissionsBonusConditionsFormatter(MissionsBattleConditionsFormatter):
    def __init__(self):
        ...

class _CumulativableFormatter(MissionFormatter, CumulativableFormatter):
    __eventsCache: Any
    def _format(self, condition, event):
        ...
    def _cumulativeFormat(self, condition, event):
        ...
    def _getProgressData(self, condition, event):
        ...
    def _groupedByFormat(self, condition, event, progressData):
        ...
    @classmethod
    def _getComplexTitle(cls, current, total):
        ...
    @classmethod
    def _getTitle(cls, current, total):
        ...

class _CumulativeResultFormatter(_CumulativableFormatter):
    @classmethod
    def _getIconKey(cls, condition=None):
        ...
    def _getDescription(self, condition):
        ...
    def _packGui(self, title, condition, progressType, current, total, earned=None, progressData=None):
        ...

class _VehicleCumulativeFormatter(_CumulativableFormatter, MissionsVehicleListFormatter):
    def _cumulativeFormat(self, condition, event):
        ...
    def _groupedByFormat(self, condition, event, progressData):
        ...
    @classmethod
    def _getConditionTitle(cls, condition, current, total):
        ...

class _VehicleKillsCumulativeFormatter(_VehicleCumulativeFormatter, VehiclesKillFormatter):
    ...

class _VehicleDamageCumulativeFormatter(_VehicleCumulativeFormatter, VehiclesDamageFormatter):
    ...

class _VehicleStunCumulativeFormatter(_VehicleCumulativeFormatter, VehiclesStunFormatter):
    @classmethod
    def _getLabelKey(cls, condition=None):
        ...

class _CumulativeSumFormatter(_CumulativableFormatter):
    __eventsCache: Any
    def _packGui(self, title, condition, progressType, current, total, earned=None, progressData=None):
        ...
    def _getDescription(self, condition):
        ...

class BattlesCountFormatter(_CumulativeResultFormatter):
    __hasPostBattleConditions: Any
    def __init__(self, hasPostBattleConditions):
        ...
    @classmethod
    def _getIconKey(cls, condition=None):
        ...
    def _getDescription(self, condition):
        ...

def packMissionVehicleProgress(groupByKey, current, total):
    ...
def packMissionNationProgress(groupByKey, current, total):
    ...
def packMissionLevelProgress(groupByKey, current, total):
    ...
def packMissionClassProgress(groupByKey, current, total):
    ...
