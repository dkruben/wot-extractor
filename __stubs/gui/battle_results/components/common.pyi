# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_results/components/common.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as ARENA_BONUS_TYPE_CAPS
from constants import ARENA_GUI_TYPE as ARENA_GUI_TYPE, FINISH_REASON as FINISH_REASON
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.battle_results.pbs_helpers.common import getArenaNameStr as getArenaNameStr, getRegularFinishResultResource as getRegularFinishResultResource
from gui.battle_results.components import base as base
from gui.battle_results.components import style as style
from gui.battle_results.settings import PLAYER_TEAM_RESULT as _TEAM_RESULT, UI_VISIBILITY as UI_VISIBILITY
from gui.shared.utils import toUpper as toUpper
from helpers import i18n as i18n, dependency as dependency
from helpers.time_utils import ONE_MINUTE as ONE_MINUTE
from player_satisfaction_schema import playerSatisfactionSchema as playerSatisfactionSchema
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from gui.battle_control.battle_constants import WinStatus as WinStatus
_ARENA_TYPE_FORMAT = '#arenas:type/{0}/name'
_ARENA_TYPE_EXT_FORMAT = '#menu:loading/battleTypes/{0}'
_ARENA_FULL_NAME_FORMAT = '#battle_results:common/arena/fullName'

class ArenaShortTimeVO(base.StatsItem):
    __slots__: tuple
    def _convert(self, record, reusable):
        ...

class ArenaDateTimeItem(base.StatsItem):
    __slots__: tuple
    def _convert(self, record, reusable):
        ...

class RegularArenaFullNameItem(base.StatsItem):
    __slots__: tuple
    def _convert(self, record, reusable):
        ...

class ArenaNameItem(base.StatsItem):
    __slots__: tuple
    def _convert(self, record, reusable):
        ...

class ArenaIconItem(base.StatsItem):
    __slots__: tuple
    def _convert(self, record, reusable):
        ...

class ArenaDurationItem(base.StatsItem):
    __slots__: tuple
    def _convert(self, record, reusable):
        ...

class ObjectivesReachedVO(base.StatsItem):
    __slots__: tuple
    def _convert(self, record, reusable):
        ...

class ObjectivesDestroyedVO(base.StatsItem):
    __slots__: tuple
    def _convert(self, record, reusable):
        ...

class BasesCapturedVO(base.StatsItem):
    __slots__: tuple
    def _convert(self, record, reusable):
        ...

class ArenaDurationVO(ArenaDurationItem):
    __slots__: tuple
    def _convert(self, record, reusable):
        ...

class PlayerKillingTimeVO(base.StatsItem):
    __slots__: tuple
    def _convert(self, record, reusable):
        ...

class FinishResultMeta(base.DictMeta):
    __slots__: tuple
    def __init__(self, finishReasonLabel, finishReasonClarificationLabel, shortResultLabel, fullResultLabel):
        ...

class RegularFinishResultBlock(base.StatsBlock):
    __slots__: tuple
    finishReasonLabel: Any
    finishReasonClarificationLabel: Any
    shortResultLabel: Any
    fullResultLabel: Any
    def __init__(self, meta=None, field='', *path):
        ...
    def setRecord(self, result, reusable):
        ...

class StrongholdBattleFinishResultBlock(RegularFinishResultBlock):
    sessionProvider: Any
    finishReasonLabel: Any
    shortResultLabel: Any
    fullResultLabel: Any
    finishReasonClarificationLabel: Any
    def setRecord(self, result, reusable):
        ...

class EpicBattleBattleFinishResultBlock(RegularFinishResultBlock):
    sessionProvider: Any
    finishReasonLabel: Any
    shortResultLabel: Any
    fullResultLabel: Any
    finishReasonClarificationLabel: Any
    def setRecord(self, result, reusable):
        ...

class AllyTeamClanTitle(base.StatsItem):
    __slots__: tuple
    def _convert(self, value, reusable):
        ...

class EnemyTeamClanTitle(base.StatsItem):
    __slots__: tuple
    def _convert(self, value, reusable):
        ...

class ClanInfoBlock(base.StatsBlock):
    __slots__: tuple
    clanDBID: Any
    clanAbbrev: Any
    def __init__(self, meta=None, field='', *path):
        ...
    def setRecord(self, record, reusable):
        ...

class ClansInfoBlock(base.StatsBlock):
    __slots__: tuple
    allies: Any
    enemies: Any
    def __init__(self, meta=None, field='', *path):
        ...
    def setRecord(self, record, reusable):
        ...

class TeamsUiVisibility(base.StatsItem):
    def _convert(self, value, reusable):
        ...

class EligibleForCrystalRewards(base.StatsItem):
    def _convert(self, value, reusable):
        ...

class ShowRateSatisfactionCmp(base.StatsItem):
    def _convert(self, value, reusable):
        ...

class SortieTeamsUiVisibility(TeamsUiVisibility):
    def _convert(self, value, reusable):
        ...

def makeArenaFullName(arenaTypeName, i18nKey):
    ...
def makeRegularFinishResultLabel(finishReason, teamResult):
    ...
def makeEpicBattleFinishResultLabel(finishReason, teamResult):
    ...
