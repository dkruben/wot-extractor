# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/platoon/view/platoon_search_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import time as time
from gui.impl.gen.view_models.windows.pop_over_window_model import PopOverWindowModel as PopOverWindowModel
from gui.prb_control import prb_getters as prb_getters
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from skeletons.gui.game_control import IPlatoonController as IPlatoonController
from helpers import dependency as dependency
from gui.impl.gen.view_models.views.lobby.platoon.searching_dropdown_model import SearchingDropdownModel as SearchingDropdownModel
from gui.impl.lobby.platoon.view.subview.platoon_tiers_limit_subview import TiersLimitSubview as TiersLimitSubview
from gui.impl.pub import ViewImpl as ViewImpl, WindowView as WindowView
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags
from gui.impl.gen import R as R
from gui.impl import backport as backport
from gui.shared import g_eventBus as g_eventBus
from gui.shared.events import PlatoonDropdownEvent as PlatoonDropdownEvent
from gui.impl.lobby.premacc.squad_bonus_tooltip_content import SquadBonusTooltipContent as SquadBonusTooltipContent
from gui.impl.lobby.platoon.platoon_helpers import formatSearchEstimatedTime as formatSearchEstimatedTime, getQueueInfoByQueueType as getQueueInfoByQueueType, Position as Position, getPlatoonBonusState as getPlatoonBonusState, BonusState as BonusState
from PlayerEvents import g_playerEvents as g_playerEvents
from UnitBase import UNDEFINED_ESTIMATED_TIME as UNDEFINED_ESTIMATED_TIME
from frameworks.wulf.gui_constants import ViewStatus as ViewStatus, WindowLayer as WindowLayer, ViewFlags as ViewFlags
from gui.impl.lobby.platoon.platoon_helpers import PreloadableWindow as PreloadableWindow
from constants import QUEUE_TYPE as QUEUE_TYPE
_logger: Any

class SearchView(ViewImpl, CallbackDelayer):
    __platoonCtrl: Any
    _layoutID: Any
    QUEUE_INFO_UPDATE_TIME = 5
    searchTimestamp = 0
    __tiersLimitSubview: Any
    __prbEntityType: Any
    def __init__(self):
        ...
    def getPrbEntityType(self):
        ...
    @staticmethod
    def resetState():
        ...
    def _finalize(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    @property
    def _viewModelClass(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def __addListeners(self):
        ...
    def __removeListeners(self):
        ...
    def __onOutsideClick(self):
        ...
    def __initButtons(self):
        ...
    def __askForPlayerQueueInfo(self):
        ...
    def __cancelSearch(self):
        ...
    def __onQueueInfoReceived(self, queueInfo):
        ...
    def __updateEstimatedTime(self):
        ...
    def _setBackgroundImage(self):
        ...

class SearchWindow(PreloadableWindow):
    __platoonCtrl: Any
    def __init__(self):
        ...
    @property
    def preBattleView(self):
        ...
    @property
    def popOverModel(self):
        ...
    def _finalize(self):
        ...
    def _onContentReady(self):
        ...
    def show(self, focus=True):
        ...
    def hide(self, destroy=False):
        ...
