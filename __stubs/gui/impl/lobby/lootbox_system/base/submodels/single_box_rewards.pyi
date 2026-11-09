# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/lootbox_system/base/submodels/single_box_rewards.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from typing import TYPE_CHECKING as TYPE_CHECKING
import SoundGroups as SoundGroups
import Windowing as Windowing
from adisp import adisp_async as adisp_async, adisp_process as adisp_process
from frameworks.wulf import WindowLayer as WindowLayer
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from gui.impl.gen.view_models.views.lobby.lootbox_system.main_view_model import SubViewID as SubViewID
from gui.impl.gen.view_models.views.lobby.lootbox_system.submodels.single_box_rewards_view_model import SingleBoxRewardsViewModel as SingleBoxRewardsViewModel
from gui.impl.lobby.lootbox_system.base.common import SubViewImpl as SubViewImpl
from gui.impl.lobby.lootbox_system.base.submodels.common import updateAnimationState as updateAnimationState
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel as replaceNoneKwargsModel
from gui.lootbox_system.base.bonuses_packers import packBonusModelAndTooltipData as packBonusModelAndTooltipData, splitBonusesToExtra as splitBonusesToExtra
from gui.lootbox_system.base.common import ViewID as ViewID, Views as Views
from gui.lootbox_system.base.decorators import createBackportTooltipDecorator as createBackportTooltipDecorator, createTooltipContentDecorator as createTooltipContentDecorator
from gui.lootbox_system.base.sound import playVideoPauseSound as playVideoPauseSound, playVideoResumeSound as playVideoResumeSound
from gui.lootbox_system.base.utils import acceptRerollableBoxRewards as acceptRerollableBoxRewards, hasStopRerollToken as hasStopRerollToken, isShopVisible as isShopVisible, openBoxes as openBoxes
from gui.lootbox_system.base.views_loaders import showItemPreview as showItemPreview
from gui.server_events.bonuses import SimpleBonus as SimpleBonus
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, events as events
from gui.shared.system_factory import collectLootBoxMainView as collectLootBoxMainView
from gui.shared.view_helpers.blur_manager import CachedBlur as CachedBlur
from gui.shop import showBuyGoldForLootboxReroll as showBuyGoldForLootboxReroll
from gui.sounds.filters import StatesGroup as StatesGroup, States as States
from gui.shared.event_dispatcher import showRerollBoxDialog as showRerollBoxDialog, showExchangeGoldWindow as showExchangeGoldWindow
from gui.shared.money import Currency as Currency
from helpers import dependency as dependency
from shared_utils import first as first
from skeletons.gui.game_control import ILootBoxSystemController as ILootBoxSystemController
from wg_async import wg_async as wg_async, wg_await as wg_await
from typing import Dict as Dict, List as List
_logger: Any

class SingleBoxRewards(SubViewImpl):
    __lootBoxes: Any
    __isReopen: Any
    __category: Any
    __openCount: Any
    __bonuses: Any
    __extraBonuses: Any
    __hasStopRerollToken: Any
    __tooltipItems: Any
    __isVideoPlaying: Any
    __eventName: Any
    __blur: Any
    def __init__(self, viewModel, parentView):
        ...
    @property
    def viewModel(self):
        ...
    # decorador original: @createBackportTooltipDecorator(...)
    def createToolTip(self, event):
        ...
    # decorador original: @createTooltipContentDecorator(...)
    def createToolTipContent(self, event, contentID):
        ...
    def getTooltipData(self, event):
        ...
    def initialize(self, *args, **kwargs):
        ...
    def finalize(self):
        ...
    def _getCallbacks(self):
        ...
    def _getEvents(self):
        ...
    def _getListeners(self):
        ...
    def _getBonusPacker(self):
        ...
    def __setVideoPlaying(self, ctx=None):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __setWindowAccessible(self, model=None):
        ...
    def __onWindowAccessibilityChanged(self, _):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __updateData(self, model=None):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __updateCounters(self, model=None):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __updateBoxReroll(self, model=None):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __updateBonuses(self, model=None):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __updateAnimationState(self, ctx=None, model=None):
        ...
    def __processOpenBoxResult(self, bonuses):
        ...
    def __isRerollDialogRequired(self):
        ...
    # decorador original: @wg_async
    def __showExchange(self, currencyValue, currencyName):
        ...
    # decorador original: @wg_async
    def __rerollDialogOpen(self):
        ...
    def __openNext(self, ctx=None):
        ...
    # decorador original: @wg_async
    def __rerollBox(self, ctx=None):
        ...
    # decorador original: @adisp_process
    def __goBack(self):
        ...
    def __onErrorBack(self, *_):
        ...
    def __showPreview(self, ctx):
        ...
    # decorador original: @adisp_process
    def __openShop(self):
        ...
    def __updateBonusesData(self, bonuses):
        ...
    def __updateStateContext(self, **kwargs):
        ...
    def __onMoneyUpdated(self, _):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def __ensureRerollRewardsAccepted(self, callback):
        ...
