# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_light/scripts/client/comp7_light/gui/impl/lobby/battle_results/states.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from functools import partial as partial
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
from comp7_light.gui.Scaleform.genConsts.COMP7_LIGHT_HANGAR_ALIASES import COMP7_LIGHT_HANGAR_ALIASES as COMP7_LIGHT_HANGAR_ALIASES
from skeletons.gui.battle_results import IBattleResultsService as IBattleResultsService
_TANK_SIZE_LOWER_BOUNDS: tuple
_PBS_SUBHANGAR_GROUPS_BY_SIZE: tuple
Comp7LightPostBattleResultsEntryState: Any
Comp7LightLoadingState: Any
Comp7LightLoadingStateWithRetainedCamera: Any
Comp7LightPostBattleResultsState: Any
Comp7LightOverviewTab: Any
Comp7LightTeamScoreTab: Any
Comp7LightMissionProgressTab: Any
Comp7LightFinancialReportTab: Any

class Comp7LightPostBattleResultsEntryProto(PostBattleResultsEntryProto):
    STATE_ID = 'comp7Light/postBattleResultsEntry'
    __battleResults: Any
    def getSubhangarStateGroupConfig(self):
        ...

class Comp7LightLoadingProto(LoadingProto):
    STATE_ID = 'comp7Light/loading'

class Comp7LightLoadingWithRetainedCameraProto(LoadingWithRetainedCameraProto):
    STATE_ID = 'comp7Light/loadingWithRetainedCamera'
    def getSubhangarStateGroupConfig(self):
        ...

class Comp7LightPostBattleResultsProto(PostBattleResultsProto):
    STATE_ID = 'comp7Light/postBattleResults'
    VIEW_KEY: Any
    __battleResults: Any
    def getSubhangarStateGroupConfig(self):
        ...

class Comp7LightOverviewTabProto(OverviewTabProto):
    STATE_ID = 'comp7Light/overview'

class Comp7LightTeamScoreTabProto(TeamScoreTabProto):
    STATE_ID = 'comp7Light/teamScore'

class Comp7LightMissionProgressTabProto(MissionProgressTabProto):
    STATE_ID = 'comp7Light/missionProgress'
    def registerTransitions(self):
        ...

class Comp7LightFinancialReportTabProto(FinancialReportTabProto):
    STATE_ID = 'comp7Light/financialReport'

def registerStates(lsm):
    ...
def registerTransitions(lsm):
    ...
