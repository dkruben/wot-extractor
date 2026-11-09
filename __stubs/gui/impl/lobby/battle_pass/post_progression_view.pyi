# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/battle_pass/post_progression_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import IntEnum as IntEnum, unique as unique
from future.utils import viewitems as viewitems
from PlayerEvents import g_playerEvents as g_playerEvents
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import IS_BATTLE_PASS_COLLECTION_SEEN as IS_BATTLE_PASS_COLLECTION_SEEN, LAST_BATTLE_PASS_CYCLES_SEEN as LAST_BATTLE_PASS_CYCLES_SEEN, LAST_BATTLE_PASS_POINTS_SEEN as LAST_BATTLE_PASS_POINTS_SEEN
from battle_pass_common import BATTLE_PASS_TICKETS_EVENT as BATTLE_PASS_TICKETS_EVENT, BattlePassConsts as BattlePassConsts, CurrencyBP as CurrencyBP
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.store.browser.shop_helpers import getBattlePassCoinProductsUrl as getBattlePassCoinProductsUrl, getBattlePassTalerProductsUrl as getBattlePassTalerProductsUrl
from gui.battle_pass.battle_pass_bonuses_packers import packBonusModelAndTooltipData as packBonusModelAndTooltipData
from gui.battle_pass.battle_pass_constants import ChapterState as ChapterState
from gui.battle_pass.battle_pass_helpers import getInfoPageURL as getInfoPageURL
from gui.collection.collections_helpers import loadCollectionsFromBattlePass as loadCollectionsFromBattlePass
from gui.impl.auxiliary.collections_helper import fillCollectionModel as fillCollectionModel
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.battle_pass.chapter_simple_model import ChapterSimpleModel as ChapterSimpleModel, ChapterStatus as ChapterStatus
from gui.impl.gen.view_models.views.lobby.battle_pass.level_model import LevelModel as LevelModel
from gui.impl.gen.view_models.views.lobby.battle_pass.post_progression_view_model import PostProgressionStatus as PostProgressionStatus, PostProgressionViewModel as PostProgressionViewModel
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel as replaceNoneKwargsModel
from gui.lootbox_system.base.common import ViewID as ViewID, Views as Views
from gui.shared.event_dispatcher import showBattlePassHowToEarnPointsView as showBattlePassHowToEarnPointsView, showBattlePassTankmenVoiceover as showBattlePassTankmenVoiceover, showBrowserOverlayView as showBrowserOverlayView, showShop as showShop
from helpers import dependency as dependency, time_utils as time_utils
from shared_utils import first as first
from skeletons.gui.game_control import IBattlePassController as IBattlePassController, ICollectionsSystemController as ICollectionsSystemController, ILootBoxSystemController as ILootBoxSystemController
from skeletons.gui.shared import IItemsCache as IItemsCache
_CHAPTER_STATUSES: dict

# decorador original: @unique
class _AnimationState(IntEnum):
    NORMAL_STATE = 0
    NEW_PROGRESS_STATE = 1
    NEW_CYCLE_STATE = 2

# base nao representavel no stub: ViewComponent[...]
class PostProgressionPresenter:
    __battlePass: Any
    __collectionsSystem: Any
    __itemsCache: Any
    __lootBoxes: Any
    __chapterID: Any
    __tankmenScreen: Any
    __tooltipItems: Any
    __animationState: Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def getTooltipData(self, event):
        ...
    def activate(self):
        ...
    def deactivate(self):
        ...
    def updateInitialData(self, **kwargs):
        ...
    def onExtraChapterExpired(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    def _getCallbacks(self):
        ...
    def __fillModel(self):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __updatePostProgressionData(self, model=None):
        ...
    def __updateChapters(self, chapters):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __updateBalance(self, value=None, model=None):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __updateRewardChoice(self, model=None):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __updateTicketInfo(self, model=None):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __updateCollections(self, model=None):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __updateProgression(self, model=None):
        ...
    def __getLevelModel(self, level):
        ...
    def __onPointsUpdated(self, *_):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __onBattlePassBought(self, model=None):
        ...
    def __onBPTalerUpdated(self, *data):
        ...
    def __getPostProgressionStatus(self):
        ...
    def __getChapterStatus(self, chapterID):
        ...
    def __getTankmenScreenID(self):
        ...
    def __checkBattlePassState(self, *_):
        ...
    @staticmethod
    def __showInfoPage():
        ...
    def __showPointsInfo(self):
        ...
    @staticmethod
    def __showCoinsShop():
        ...
    def __showTickets(self):
        ...
    def __showTankmen(self):
        ...
    def __claimRewards(self):
        ...
    def __openCollection(self):
        ...
    @staticmethod
    def __showTalers():
        ...
    def __onProgressAchieved(self):
        ...
    def __onCycleCompleted(self):
        ...
    def __saveLastProgress(self):
        ...
    def __saveLastCycle(self):
        ...
