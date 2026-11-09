# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/user_missions/hangar_widget/presenters/battle_pass_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from typing import Optional as Optional, Set as Set
import BigWorld as BigWorld
from account_helpers.AccountSettings import AccountSettings as AccountSettings, IS_BATTLE_PASS_START_ANIMATION_SEEN as IS_BATTLE_PASS_START_ANIMATION_SEEN
from battle_pass_common import getPresentLevel as getPresentLevel
from gui.battle_pass.battle_pass_helpers import getTimeExpirations as getTimeExpirations
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.user_missions.widget.battle_pass_model import AppearAnimationState as AppearAnimationState, BattlePassModel as BattlePassModel, WidgetState as WidgetState
from gui.impl.lobby.battle_pass.battle_pass_entry_point_view import BaseBattlePassEntryPointView as BaseBattlePassEntryPointView
from gui.impl.lobby.battle_pass.common import isExtraChapterSeen as isExtraChapterSeen, isExtraContentResolved as isExtraContentResolved, isHolidayChapterSeen as isHolidayChapterSeen, isUmgExtraChapterSeen as isUmgExtraChapterSeen, setUmgExtraChapterSeen as setUmgExtraChapterSeen, setHolidayChapterSeen as setHolidayChapterSeen
from gui.impl.lobby.battle_pass.tooltips.battle_pass_completed_tooltip_view import BattlePassCompletedTooltipView as BattlePassCompletedTooltipView
from gui.impl.lobby.battle_pass.tooltips.battle_pass_in_progress_tooltip_view import BattlePassInProgressTooltipView as BattlePassInProgressTooltipView
from gui.impl.lobby.battle_pass.tooltips.battle_pass_no_chapter_tooltip_view import BattlePassNoChapterTooltipView as BattlePassNoChapterTooltipView
from gui.impl.lobby.user_missions.hangar_widget.overlap_ctrl import OverlapCtrlMixin as OverlapCtrlMixin
from gui.impl.lobby.user_missions.hangar_widget.presenters.base_child_presenter import UserMissionChildPresenter as UserMissionChildPresenter
from gui.impl.lobby.user_missions.hangar_widget.presenters.constants import UserMissionGroups as UserMissionGroups
from gui.impl.lobby.user_missions.hangar_widget.services import IBattlePassService as IBattlePassService
from gui.impl.lobby.user_missions.hangar_widget.tooltip_positioner import TooltipPositionerMixin as TooltipPositionerMixin
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.shared.event_dispatcher import showBattlePass as showBattlePass
from helpers import dependency as dependency
from shared_utils import findFirst as findFirst
from skeletons.gui.game_control import IBattlePassController as IBattlePassController
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
from frameworks.wulf import View as View, ViewEvent as ViewEvent
_SPACE_CREATED_UPDATE_DELAY = 0.7
_g_entryLastState: Any

class _LastEntryState(object):
    rewards: Any
    pointsEarned: Any
    level: Any
    chapterID: Any
    rewardsHash: Any
    def __init__(self):
        ...
    def update(self, rewards=None, level=0, pointsEarned=0, chapterID=0, rewardsHash=0):
        ...
    def getRewardsHash(self, currentRewards):
        ...

# base nao representavel no stub: ViewComponent[...]
class BattlePassPresenter(UserMissionChildPresenter, TooltipPositionerMixin, OverlapCtrlMixin, BaseBattlePassEntryPointView):
    GROUP = UserMissionGroups.BATTLE_PASS
    __hangarSpace: Any
    __battlePass: Any
    battlePassService: Any
    _firstUpdatePerformed: Any
    _readyForAnimations: Any
    _isOffersUpdatedCall: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def isVisible(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    @property
    def hasDeferModelUpdate(self):
        ...
    def _createInProgressTooltipView(self):
        ...
    @staticmethod
    def _onIntroAnimationPlayed():
        ...
    @staticmethod
    def _isIntroAnimationPlayed():
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _onBattlePassChanged(self):
        ...
    def _onClick(self):
        ...
    def _onWidgetUnmounted(self):
        ...
    def _onPointsUpdated(self, *_):
        ...
    def _onOffersUpdated(self, *_):
        ...
    def _delayedUpdateAfterSpaceCreated(self):
        ...
    def _onSpaceCreate(self):
        ...
    def _finalize(self):
        ...
    def _updateOptional(self):
        ...
    def _updateData(self, *_):
        ...
    def _rawUpdate(self):
        ...
    def _updateViewModel(self):
        ...
    def _preInitModel(self):
        ...
    def _fillViewModel(self, tx):
        ...
    def _fillModel(self, tx, chapterID, points, limit, level, rewardsHash):
        ...
    def _fillLastSeen(self, tx, chapterID, points, level, rewards, rewardsHash):
        ...
    def _getTimeLeft(self, chapterID, widgetState):
        ...
    def _needToShowExtraIntro(self, isBattlePassExtraChapterSeen):
        ...
    def _needToRemindExtraChapter(self):
        ...
    def _getAppearAnimationState(self):
        ...
    def _getWidgetState(self, isBattlePassExtraChapterSeen, isBattlePassHolidayChapterSeen):
        ...
    def _hasExtraChapter(self):
        ...
    def _getUncompletedExtraChapterID(self):
        ...
    def _savePresenterLastState(self, rewards=None, rewardsHash=None):
        ...
