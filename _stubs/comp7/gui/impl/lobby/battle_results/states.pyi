# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/battle_results/states.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from functools import partial as partial
from comp7.gui.Scaleform.genConsts.COMP7_HANGAR_ALIASES import COMP7_HANGAR_ALIASES as COMP7_HANGAR_ALIASES
from constants import ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from frameworks_common.state_machine.transitions import TransitionType as TransitionType
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.battle_results.settings import PLAYER_TEAM_RESULT as PLAYER_TEAM_RESULT
from gui.impl.lobby.battle_results.states import generatePostBattleStateClasses as generatePostBattleStateClasses, PostBattleResultsEntryProto as PostBattleResultsEntryProto, LoadingProto as LoadingProto, LoadingWithRetainedCameraProto as LoadingWithRetainedCameraProto, PostBattleResultsProto as PostBattleResultsProto, OverviewTabProto as OverviewTabProto, TeamScoreTabProto as TeamScoreTabProto, MissionProgressTabProto as MissionProgressTabProto, FinancialReportTabProto as FinancialReportTabProto, PBSSceneSetup as PBSSceneSetup, shouldHijackPBSEntry as shouldHijackPBSEntry
from gui.lobby_state_machine.states import SubScopeSubLayerState as SubScopeSubLayerState
from gui.lobby_state_machine.transitions import HijackTransition as HijackTransition
from gui.shared.utils.functions import getArenaImage as getArenaImage
from gui.subhangar.subhangar_observer import selectItemByTankSize as selectItemByTankSize
from gui.subhangar.subhangar_state_groups import SubhangarStateGroups as SubhangarStateGroups, SubhangarStateGroupConfig as SubhangarStateGroupConfig
from helpers import dependency as dependency
from skeletons.gui.battle_results import IBattleResultsService as IBattleResultsService
_COMP7_PBS_SUBHANGAR_GROUPS_BY_SIZE: tuple
_COMP7_BONUS_TYPE_RANGE: tuple
_TANK_SIZE_LOWER_BOUNDS: tuple
Comp7PostBattleResultsEntryState: Any
Comp7LoadingState: Any
Comp7LoadingStateWithRetainedCamera: Any
Comp7PostBattleResultsState: Any
Comp7OverviewTab: Any
Comp7TeamScoreTab: Any
Comp7MissionProgressTab: Any
Comp7FinancialReportTab: Any

class Comp7PostBattleResultsEntryProto(PostBattleResultsEntryProto):
    STATE_ID = 'comp7/postBattleResultsEntry'
    __battleResults: Any
    def getSubhangarStateGroupConfig(self):
        ...

class Comp7LoadingProto(LoadingProto):
    STATE_ID = 'comp7/loading'

class Comp7LoadingWithRetainedCameraProto(LoadingWithRetainedCameraProto):
    STATE_ID = 'comp7/loadingWithRetainedCamera'
    __battleResults: Any
    def getSubhangarStateGroupConfig(self):
        ...

class Comp7PostBattleResultsProto(PostBattleResultsProto):
    STATE_ID = 'comp7/postBattleResults'
    VIEW_KEY: Any
    __battleResults: Any
    def getSubhangarStateGroupConfig(self):
        ...

class Comp7OverviewTabProto(OverviewTabProto):
    STATE_ID = 'comp7/overview'

class Comp7TeamScoreTabProto(TeamScoreTabProto):
    STATE_ID = 'comp7/teamScore'

class Comp7MissionProgressTabProto(MissionProgressTabProto):
    STATE_ID = 'comp7/missionProgress'

class Comp7FinancialReportTabProto(FinancialReportTabProto):
    STATE_ID = 'comp7/financialReport'

def _getReusable(battleResultsService, arenaUniqueID):
    ...
def registerStates(lsm):
    ...
def registerTransitions(lsm):
    ...
