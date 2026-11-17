# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/battle_pass/battle_pass_buy_levels_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import SoundGroups as SoundGroups
from frameworks.wulf import ViewStatus as ViewStatus, WindowLayer as WindowLayer
from gui.battle_pass.battle_pass_bonuses_packers import packBonusModelAndTooltipData as packBonusModelAndTooltipData
from gui.battle_pass.battle_pass_buyer import BattlePassBuyer as BattlePassBuyer
from gui.battle_pass.battle_pass_constants import ChapterState as ChapterState
from gui.battle_pass.battle_pass_package import PackageAnyLevels as PackageAnyLevels
from gui.battle_pass.sounds import BattlePassSounds as BattlePassSounds
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.battle_pass.battle_pass_buy_level_view_model import BattlePassBuyLevelViewModel as BattlePassBuyLevelViewModel
from gui.impl.gui_decorators import args2params as args2params
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel as replaceNoneKwargsModel
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, events as events, g_eventBus as g_eventBus
from gui.shared.event_dispatcher import showBattlePass as showBattlePass
from gui.sounds.filters import switchHangarOverlaySoundFilter as switchHangarOverlaySoundFilter
from helpers import dependency as dependency
from skeletons.gui.game_control import IBattlePassController as IBattlePassController, IWalletController as IWalletController
from skeletons.gui.shared import IItemsCache as IItemsCache
_logger: Any

# base nao representavel no stub: ViewComponent[...]
class BuyLevelsPresenter:
    __battlePass: Any
    __wallet: Any
    __itemsCache: Any
    __tooltipItems: Any
    __chapterID: Any
    __package: Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def getTooltipData(self, event):
        ...
    def updateInitialData(self, **kwargs):
        ...
    def activate(self):
        ...
    def deactivate(self):
        ...
    def onExtraChapterExpired(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _getListeners(self):
        ...
    def _getEvents(self):
        ...
    def __clearTooltips(self):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __fillModel(self, model=None):
        ...
    def __onBuying(self, _):
        ...
    def __onAwardViewClose(self, _):
        ...
    def __onLevelUp(self):
        ...
    def __onSettingsChanged(self, *_):
        ...
    def __onWalletChanged(self, _):
        ...
    def __updateState(self):
        ...
    def __onPurchase(self):
        ...
    # decorador original: @args2params(...)
    def __onChangeSelectedLevels(self, count):
        ...
    def __notifyPurchaseAborted(self):
        ...
    def __onBuyLevelsCallback(self, result):
        ...
