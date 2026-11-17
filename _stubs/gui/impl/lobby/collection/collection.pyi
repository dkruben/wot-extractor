# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/collection/collection.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from frameworks.wulf import ViewStatus as ViewStatus, WindowFlags as WindowFlags
from gui.Scaleform.Waiting import Waiting as Waiting
from gui.Scaleform.daapi.view.lobby.profile.sound_constants import ACHIEVEMENTS_SOUND_SPACE as ACHIEVEMENTS_SOUND_SPACE
from gui.collection.account_settings import getShownNewItemsCount as getShownNewItemsCount, isItemNew as isItemNew, isRewardNew as isRewardNew, isTutorialCompleted as isTutorialCompleted, setCollectionRenewSeen as setCollectionRenewSeen, setCollectionTutorialCompleted as setCollectionTutorialCompleted, setItemShown as setItemShown, setRewardShown as setRewardShown, setShownNewItemsCount as setShownNewItemsCount
from gui.collection.collections_helpers import composeBonuses as composeBonuses, getItemResKey as getItemResKey
from gui.collection.resources.cdn.models import Group as Group, Sub as Sub, makeImageID as makeImageID
from gui.impl.auxiliary.collections_helper import getCollectionsBonusPacker as getCollectionsBonusPacker
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.collection.collection_view_model import CollectionViewModel as CollectionViewModel
from gui.impl.gen.view_models.views.lobby.collection.item_model import ItemModel as ItemModel, ItemState as ItemState
from gui.impl.gen.view_models.views.lobby.collection.page_backgrounds_model import PageBackgroundsModel as PageBackgroundsModel
from gui.impl.gen.view_models.views.lobby.collection.reward_info_model import RewardInfoModel as RewardInfoModel, RewardState as RewardState
from gui.impl.gen.view_models.views.lobby.collection.tab_model import TabModel as TabModel
from gui.impl.lobby.battle_pass.tooltips.battle_pass_coin_tooltip_view import BattlePassCoinTooltipView as BattlePassCoinTooltipView
from gui.impl.lobby.collection.tooltips.collection_item_tooltip_view import CollectionItemTooltipView as CollectionItemTooltipView
from gui.impl.lobby.common.view_helpers import packBonusModelAndTooltipData as packBonusModelAndTooltipData
from gui.impl.lobby.common.view_wrappers import createBackportTooltipDecorator as createBackportTooltipDecorator
from gui.impl.pub import WindowImpl as WindowImpl
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel as replaceNoneKwargsModel
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, events as events, g_eventBus as g_eventBus
from gui.shared.event_dispatcher import showCollectionItemPreviewWindow as showCollectionItemPreviewWindow, showHangar as showHangar
from helpers import dependency as dependency
from skeletons.gui.game_control import ICollectionsSystemController as ICollectionsSystemController
from typing import Dict as Dict
_logger: Any
_INITIAL_PAGE = -1

class CollectionView(ViewComponent):
    _COMMON_SOUND_SPACE = ACHIEVEMENTS_SOUND_SPACE
    __collectionsSystem: Any
    __collectionId: Any
    __collection: Any
    __rewardTooltips: Any
    __page: Any
    __pagesCount: Any
    __content: Any
    __waitingCount: Any
    def __init__(self, ctx=None):
        ...
    @property
    def viewModel(self):
        ...
    # decorador original: @createBackportTooltipDecorator(...)
    def createToolTip(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def getTooltipData(self, event):
        ...
    def getContext(self):
        ...
    def _onLoaded(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    def __onViewLoaded(self, args):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __fillTabData(self, model=None):
        ...
    def __fillTabs(self, model=None):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __fillItems(self, model=None):
        ...
    def __fillItemModel(self, item, itemModel):
        ...
    def __fillTabModel(self, collectionId, tabModel):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __fillPagesBackgrounds(self, model=None):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __clearContent(self, model=None):
        ...
    def __updateContentData(self):
        ...
    def __generateContentData(self):
        ...
    def __onContentUpdated(self, isOk, data):
        ...
    def __showWaiting(self):
        ...
    def __hideWaiting(self):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __updateCurrentNewItems(self, model=None):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __fillProgression(self, model=None):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __fillProgressInfo(self, model=None):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __fillRewardsInfo(self, model=None):
        ...
    def __getRewardState(self, requiredCount):
        ...
    def __getItemState(self, itemId):
        ...
    def __onSetItemReceived(self, args):
        ...
    def __onSetRewardReceived(self, args):
        ...
    def __onSetProgressItemsReceived(self):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __onFinishTutorial(self, model=None):
        ...
    def __onOpenItemPreview(self, args):
        ...
    def __onTabSelected(self, args):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __onBalanceUpdated(self, model=None):
        ...
    def __onSettingsChanged(self):
        ...
    def __onClose(self):
        ...
    def __getContent(self, group, sub, name):
        ...

class CollectionWindow(WindowImpl):
    def __init__(self, layer, ctx, **kwargs):
        ...
