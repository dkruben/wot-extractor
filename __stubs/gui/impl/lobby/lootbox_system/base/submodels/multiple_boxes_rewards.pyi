# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/lootbox_system/base/submodels/multiple_boxes_rewards.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from typing import TYPE_CHECKING as TYPE_CHECKING
import SoundGroups as SoundGroups
import Windowing as Windowing
from frameworks.wulf import Array as Array
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from gui.impl.gen.view_models.views.lobby.lootbox_system.main_view_model import SubViewID as SubViewID
from gui.impl.gen.view_models.views.lobby.lootbox_system.submodels.multiple_boxes_rewards_view_model import MultipleBoxesRewardsViewModel as MultipleBoxesRewardsViewModel
from gui.impl.lobby.lootbox_system.base.common import SubViewImpl as SubViewImpl
from gui.impl.lobby.lootbox_system.base.submodels.common import updateAnimationState as updateAnimationState
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel as replaceNoneKwargsModel
from gui.lootbox_system.base.bonuses_packers import packBonusModelAndTooltipData as packBonusModelAndTooltipData
from gui.lootbox_system.base.common import ViewID as ViewID, Views as Views
from gui.lootbox_system.base.decorators import createBackportTooltipDecorator as createBackportTooltipDecorator, createTooltipContentDecorator as createTooltipContentDecorator
from gui.lootbox_system.base.sound import enterLootBoxesMultipleRewardState as enterLootBoxesMultipleRewardState, exitLootBoxesMultipleRewardState as exitLootBoxesMultipleRewardState, playVideoPauseSound as playVideoPauseSound, playVideoResumeSound as playVideoResumeSound
from gui.lootbox_system.base.utils import isShopVisible as isShopVisible, openBoxes as openBoxes
from gui.lootbox_system.base.views_loaders import showItemPreview as showItemPreview
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, events as events
from gui.shared.system_factory import collectLootBoxMainView as collectLootBoxMainView
from gui.sounds.filters import StatesGroup as StatesGroup, States as States
from helpers import dependency as dependency
from skeletons.gui.game_control import ILootBoxSystemController as ILootBoxSystemController
from typing import Dict as Dict, List as List, Optional as Optional
from gui.server_events.bonuses import SimpleBonus as SimpleBonus

class MultipleBoxesRewards(SubViewImpl):
    __lootBoxes: Any
    __isReopen: Any
    __category: Any
    __openCount: Any
    __bonuses: Any
    __tooltipItems: Any
    __isVideoPlaying: Any
    __eventName: Any
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
    def _getEvents(self):
        ...
    def _getListeners(self):
        ...
    def __setVideoPlaying(self, ctx=None):
        ...
    def _getBonusPacker(self):
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
    def __updateBonuses(self, model=None):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __updateAnimationState(self, ctx=None, model=None):
        ...
    def __openNext(self, ctx=None):
        ...
    def __goBack(self):
        ...
    def __onErrorBack(self, *_):
        ...
    def __showPreview(self, ctx):
        ...
    def __openShop(self):
        ...
    def __updateStateContext(self, bonuses):
        ...
