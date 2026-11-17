# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/profile/ProfileStatistics.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from debug_utils import LOG_ERROR as LOG_ERROR
from gui.Scaleform.daapi.view.lobby.profile.ProfileSection import BattleTypesDropDownItems as BattleTypesDropDownItems
from gui.Scaleform.daapi.view.lobby.profile.profile_statistics_vos import getStatisticsVO as getStatisticsVO
from gui.Scaleform.daapi.view.lobby.profile.seasons_manager import makeStatisticsSeasonManagers as makeStatisticsSeasonManagers
from gui.Scaleform.daapi.view.meta.ProfileStatisticsMeta import ProfileStatisticsMeta as ProfileStatisticsMeta
from gui.Scaleform.genConsts.BATTLE_TYPES import BATTLE_TYPES as BATTLE_TYPES
from gui.Scaleform.genConsts.PROFILE_DROPDOWN_KEYS import PROFILE_DROPDOWN_KEYS as PROFILE_DROPDOWN_KEYS
from gui.Scaleform.genConsts.RANKEDBATTLES_CONSTS import RANKEDBATTLES_CONSTS as RANKEDBATTLES_CONSTS
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.ranked_battles.constants import RankedDossierKeys as RankedDossierKeys, ARCHIVE_SEASON_ID as ARCHIVE_SEASON_ID
from gui.shared.formatters import text_styles as text_styles
from helpers import dependency as dependency
from skeletons.gui.game_control import IRankedBattlesController as IRankedBattlesController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from gui.shared.event_bus import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import ProfileStatisticEvent as ProfileStatisticEvent
from gui.shared import g_eventBus as g_eventBus
_FRAME_LABELS: dict

class ProfileStatistics(ProfileStatisticsMeta):
    lobbyContext: Any
    __rankedController: Any
    _seasonsManagers: Any
    _battlesType: Any
    __ctx: Any
    def __init__(self, *args):
        ...
    def setSeason(self, seasonId):
        ...
    def showPlayersStats(self):
        ...
    def onCompletedSeasonsInfoChanged(self):
        ...
    def requestDossier(self, bType):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _setInitData(self, accountDossier=None):
        ...
    def _sendAccountData(self, targetData, accountDossier):
        ...
    def _setStatisticsVO(self, targetData, accountDossier):
        ...
    def _receiveFortDossier(self, accountDossier):
        ...
    def _getNecessaryStats(self, accountDossier=None):
        ...
    @classmethod
    def __updateStaticDropdownData(cls, vo):
        ...

def _packProviderType(mainType, addValue=None):
    ...
def _parseProviderType(value):
    ...
