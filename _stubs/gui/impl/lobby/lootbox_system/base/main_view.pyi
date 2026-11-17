# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/lootbox_system/base/main_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
from collections import deque as deque
from typing import TYPE_CHECKING as TYPE_CHECKING
from account_helpers.AccountSettings import LOOT_BOXES_INTRO_VIDEO_SHOWN as LOOT_BOXES_INTRO_VIDEO_SHOWN
from frameworks.wulf import WindowFlags as WindowFlags
from gui.Scaleform.Waiting import Waiting as Waiting
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.lootbox_system.main_view_model import MainViewModel as MainViewModel, SubViewID as SubViewID
from gui.impl.lobby.lootbox_system.base.common import MainViewImpl as MainViewImpl, PresentersMap as PresentersMap
from gui.impl.pub import WindowImpl as WindowImpl
from gui.lootbox_system.base.common import ViewID as ViewID, Views as Views
from gui.lootbox_system.base.sound import enterLootBoxesSoundState as enterLootBoxesSoundState, exitLootBoxesSoundState as exitLootBoxesSoundState
from helpers import dependency as dependency
from skeletons.gui.game_control import ILootBoxSystemController as ILootBoxSystemController
from typing import Any as Any, Dict as Dict, Deque as Deque, Optional as Optional, Tuple as Tuple

class MainViewPresenters(PresentersMap):
    def _makeLoadersMap(self):
        ...
    def _loadHome(self):
        ...
    def _loadSingleBoxRewards(self):
        ...
    def _loadMultipleBoxesRewards(self):
        ...

class MainView(MainViewImpl):
    __lootBoxes: _Any
    __subviews: _Any
    __subviewID: _Any
    __pendingSubviews: _Any
    __eventName: _Any
    def __init__(self, ctx=None, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    @property
    def currentSubview(self):
        ...
    def createToolTip(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def switchToSubView(self, subViewID=None, isBackground=False, *args, **kwargs):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _onLoaded(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    def _getPresentersMap(self):
        ...
    def _getDefaultSubViewID(self):
        ...
    def __onResourcesLoadCompleted(self):
        ...
    def __addSubview(self, subViewID=None, *args, **kwargs):
        ...
    def __loadPendingSubviews(self):
        ...
    def __showIntroIfNeeded(self):
        ...

class MainWindow(WindowImpl):
    def __init__(self, layer, ctx=None, *args, **kwargs):
        ...
