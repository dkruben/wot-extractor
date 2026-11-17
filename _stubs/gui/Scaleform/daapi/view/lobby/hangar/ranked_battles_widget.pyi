# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/hangar/ranked_battles_widget.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from future.utils import lrange as lrange
import SoundGroups as SoundGroups
from PlayerEvents import g_playerEvents as g_playerEvents
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import ENABLE_RANKED_ANIMATIONS as ENABLE_RANKED_ANIMATIONS
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.Scaleform.daapi.view.meta.RankedBattlesHangarWidgetMeta import RankedBattlesHangarWidgetMeta as RankedBattlesHangarWidgetMeta
from gui.Scaleform.genConsts.RANKEDBATTLES_ALIASES import RANKEDBATTLES_ALIASES as RANKEDBATTLES_ALIASES
from gui.Scaleform.genConsts.RANKEDBATTLES_CONSTS import RANKEDBATTLES_CONSTS as RANKEDBATTLES_CONSTS
from gui.ranked_battles.ranked_builders.widget_vos import StateBlock as StateBlock, WidgetPreferences as WidgetPreferences, getQualAddVOs as getQualAddVOs, getVOsSequence as getVOsSequence, getLeagueAdditionalVOs as getLeagueAdditionalVOs
from gui.ranked_battles.ranked_helpers.web_season_provider import UNDEFINED_LEAGUE_ID as UNDEFINED_LEAGUE_ID
from helpers import dependency as dependency
from skeletons.gui.game_control import IRankedBattlesController as IRankedBattlesController
_logger: Any

class _RankedWidgetSoundManager(object):
    __sound: Any
    __isHangarBlocked: Any
    class CALLER(object):
        HANGAR = 'hangar'
        POST_BATTLE = 'post_battle'
    def __init__(self):
        ...
    def switchHangarLock(self, *args, **kwargs):
        ...
    def playInstantSound(self, eventName, caller):
        ...
    def __callerBlocked(self, caller):
        ...

class RankedBattleResultsWidget(RankedBattlesHangarWidgetMeta):
    rankedController: Any
    _soundMgr: Any
    __slots__: tuple
    _maxRank: Any
    _clientMaxRank: Any
    _soundCallerType: Any
    def __init__(self):
        ...
    def update(self, lastRank=None, clientMaxRank=None, currentRank=None, ranksChain=None):
        ...
    def _update(self, lastRankID=None, clientMaxRankID=None, currentRankID=None, ranksChain=None):
        ...
    def onAnimationFinished(self):
        ...
    def onSoundTrigger(self, triggerName):
        ...
    def onWidgetClick(self):
        ...
    def _dispose(self):
        ...
    def _buildStatesSequence(self, lastRankID, currentRankID, maxRankID, ranks):
        ...
    def __extendWithQualificationStatesSequence(self, statesSequence):
        ...
    def __extendWithLeagueStatesSequence(self, statesSequence):
        ...
    @classmethod
    def _isAnimationEnabled(cls):
        ...
    @classmethod
    def _isHuge(cls):
        ...
    @classmethod
    def _hasAdditionalRankInfo(cls):
        ...

class RankedBattlesHangarWidget(RankedBattleResultsWidget):
    _soundCallerType: Any
    def __init__(self):
        ...
    def onWidgetClick(self):
        ...
    def onAnimationFinished(self):
        ...
    def _populate(self):
        ...
    def _update(self, lastRankID=None, clientMaxRankID=None, currentRankID=None, ranksChain=None):
        ...
    def _dispose(self):
        ...
    @classmethod
    def _isAnimationEnabled(cls):
        ...
    @classmethod
    def _isHuge(cls):
        ...
    @classmethod
    def _hasAdditionalRankInfo(cls):
        ...
    def __dossierUpdateCallBack(self, *args):
        ...
