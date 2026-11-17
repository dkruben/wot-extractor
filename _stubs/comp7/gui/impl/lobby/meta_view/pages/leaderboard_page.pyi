# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/meta_view/pages/leaderboard_page.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import BigWorld as BigWorld
import adisp as adisp
import typing as typing
from comp7.gui.impl.gen.view_models.views.lobby.enums import MetaRootViews as MetaRootViews, Rank as Rank
from comp7.gui.impl.gen.view_models.views.lobby.meta_view.pages.leaderboard_model import LeaderboardModel as LeaderboardModel, State as State
from comp7.gui.impl.gen.view_models.views.lobby.meta_view.pages.table_record_model import TableRecordModel as TableRecordModel
from comp7.gui.impl.lobby.meta_view.pages import PageSubModelPresenter as PageSubModelPresenter
from comp7.gui.impl.lobby.tooltips.fifth_rank_tooltip import FifthRankTooltip as FifthRankTooltip
from comp7.gui.impl.lobby.tooltips.last_update_tooltip import LastUpdateTooltip as LastUpdateTooltip
from comp7.gui.impl.lobby.tooltips.sixth_rank_tooltip import SixthRankTooltip as SixthRankTooltip
from gui.Scaleform.genConsts.CONTEXT_MENU_HANDLER_TYPE import CONTEXT_MENU_HANDLER_TYPE as CONTEXT_MENU_HANDLER_TYPE
from gui.impl.backport import BackportContextMenuWindow as BackportContextMenuWindow, createContextMenuData as createContextMenuData
from gui.impl.gen import R as R
from gui.impl.gui_decorators import args2params as args2params
from helpers import dependency as dependency
from skeletons.connection_mgr import IConnectionManager as IConnectionManager
from skeletons.gui.game_control import IComp7Controller as IComp7Controller
from gui.event_boards.event_boards_items import ExcelItem as ExcelItem
_logger: Any

class LeaderboardPage(PageSubModelPresenter):
    __slots__: tuple
    __comp7Controller: Any
    __connectionMgr: Any
    __elitePosition: Any
    __loadingStateManager: Any
    __requestedPageData: Any
    __lastUpdateTime: Any
    def __init__(self, viewModel, parentView):
        ...
    @property
    def pageId(self):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def createContextMenu(self, event):
        ...
    def initialize(self, **params):
        ...
    def finalize(self):
        ...
    def _getEvents(self):
        ...
    def __onRefresh(self, *_):
        ...
    def __onRanksConfigChanged(self):
        ...
    # decorador original: @args2params(...)
    def __getTableRecords(self, limit, offset):
        ...
    def __updateData(self):
        ...
    # decorador original: @adisp.adisp_process
    def __requestRecords(self, limit, offset, loadingChainMark):
        ...
    def __updateRecords(self, records):
        ...
    # decorador original: @adisp.adisp_process
    def __updateCommonRemoteData(self, loadingChainMark):
        ...
    # decorador original: @adisp.adisp_process
    def __updatePersonalData(self, loadingChainMark):
        ...
    def __isResultExpected(self, generation):
        ...
    def __getRecordModel(self, record):
        ...

class _LoadingStateManager(object):
    __REQUESTS_COUNT_KEY = 'requestsCount'
    __ERRORS_KEY = 'errors'
    __generation = 0
    __viewModel: Any
    __registeredChains: Any
    def __init__(self, viewModel):
        ...
    def startRequest(self, chainMark):
        ...
    def isValidGeneration(self, generation):
        ...
    def finishRequest(self, chainMark, isSuccessfull):
        ...
    @classmethod
    def __makeNewChainBlock(cls):
        ...

def _getBackportContextMenuData(event):
    ...
