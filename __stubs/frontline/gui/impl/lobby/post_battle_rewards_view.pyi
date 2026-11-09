# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/impl/lobby/post_battle_rewards_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import defaultdict as defaultdict
from future.utils import viewitems as viewitems
import SoundGroups as SoundGroups
from epic_constants import EPIC_SELECT_BONUS_NAME as EPIC_SELECT_BONUS_NAME, EPIC_SKILL_TOKEN_NAME as EPIC_SKILL_TOKEN_NAME
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings, WindowFlags as WindowFlags, WindowLayer as WindowLayer
from frontline.gui.bonus import FrontlineSkillBonus as FrontlineSkillBonus
from frontline.gui.frontline_bonus_packers import packBonusModelAndTooltipData as packBonusModelAndTooltipData
from frontline.gui.impl.gen.view_models.views.lobby.views.post_battle_rewards_view_model import PostBattleRewardsViewModel as PostBattleRewardsViewModel
from gui.impl.gen import R as R
from gui.impl.lobby.common.view_wrappers import createBackportTooltipDecorator as createBackportTooltipDecorator
from gui.impl.lobby.tooltips.additional_rewards_tooltip import AdditionalRewardsTooltip as AdditionalRewardsTooltip
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.lobby_window import LobbyNotificationWindow as LobbyNotificationWindow
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from gui.server_events.bonuses import mergeBonuses as mergeBonuses
from gui.shared.event_dispatcher import showEpicRewardsSelectionWindow as showEpicRewardsSelectionWindow, showFrontlineAwards as showFrontlineAwards
from gui.sounds.epic_sound_constants import EPIC_METAGAME_WWISE_SOUND_EVENTS as EPIC_METAGAME_WWISE_SOUND_EVENTS
from helpers import dependency as dependency
from skeletons.gui.battle_results import IBattleResultsService as IBattleResultsService
from skeletons.gui.game_control import IEpicBattleMetaGameController as IEpicBattleMetaGameController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.server_events import IEventsCache as IEventsCache
from PlayerEvents import g_playerEvents as g_playerEvents

class _PostBattleRewardsCtx(object):
    __epicController: Any
    __slots__: tuple
    __ctx: Any
    __currLevel: Any
    __currFamePoints: Any
    __prevLevel: Any
    __prevFamePoints: Any
    __currProgress: Any
    __prevProgress: Any
    def __init__(self, ctx=None):
        ...
    @property
    def currLevel(self):
        ...
    @property
    def currFamePoints(self):
        ...
    @property
    def currProgress(self):
        ...
    @property
    def prevLevel(self):
        ...
    @property
    def prevFamePoints(self):
        ...
    @property
    def prevProgress(self):
        ...
    @property
    def boosterXP(self):
        ...
    @property
    def achievedXP(self):
        ...
    @property
    def arenaUniqueID(self):
        ...
    @property
    def playerRank(self):
        ...
    @property
    def maxLevel(self):
        ...
    def isOnMaxLevel(self):
        ...
    def isMaxLevelReached(self):
        ...
    @property
    def newRewardsCount(self):
        ...
    @property
    def bonuses(self):
        ...
    def __packLevel(self, level, famePoints):
        ...
    def __getBonuses(self):
        ...
    def __getAbilityPointsRewardBonus(self, level):
        ...

class PostBattleRewardsView(ViewImpl, IGlobalListener):
    _MAX_VISIBLE_AWARDS = 6
    _BONUS_ORDER_PRIORITY: dict
    _MIDDLE_PRIORITY = 50
    __battleResultsService: Any
    __epicController: Any
    __eventsCache: Any
    __lobbyContext: Any
    __ctx: Any
    __tooltipItems: Any
    __rewardsList: Any
    __rewardsSelectionWindow: Any
    __isProgressBarAnimating: Any
    def __init__(self, layoutID=..., ctx=None):
        ...
    @property
    def viewModel(self):
        ...
    # decorador original: @createBackportTooltipDecorator(...)
    def createToolTip(self, event):
        ...
    def getTooltipData(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _fillModel(self):
        ...
    def _addListeners(self):
        ...
    def _removeListeners(self):
        ...
    def __fillRewards(self, vm):
        ...
    def __onClaimRewards(self):
        ...
    def __onEpicUpdated(self, diff):
        ...
    def __onClose(self):
        ...
    def __onContinue(self):
        ...
    def __onServerSettingsChanged(self, *_):
        ...
    def __onIntroStartsPlaying(self):
        ...
    def __onRibbonStartsPlaying(self):
        ...
    def __onProgressBarAnimationStart(self):
        ...
    def __onProgressBarAnimationComplete(self):
        ...

class PostBattleRewardsWindow(LobbyNotificationWindow):
    def __init__(self, ctx=None, parent=None):
        ...
