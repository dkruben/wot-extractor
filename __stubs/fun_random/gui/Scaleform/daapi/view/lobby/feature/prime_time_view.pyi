# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/Scaleform/daapi/view/lobby/feature/prime_time_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from past.builtins import cmp as cmp
from fun_random.gui.feature.util.fun_mixins import FunAssetPacksMixin as FunAssetPacksMixin, FunSubModeHolder as FunSubModeHolder
from fun_random.gui.feature.util.fun_wrappers import hasHoldingSubMode as hasHoldingSubMode, filterHoldingSubModeUpdates as filterHoldingSubModeUpdates
from fun_random.gui.fun_gui_constants import PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME
from gui.Scaleform.daapi.view.lobby.prime_time_view_base import ServerListItemPresenter as ServerListItemPresenter, makeServerString as makeServerString
from gui.Scaleform.daapi.view.meta.RankedPrimeTimeMeta import RankedPrimeTimeMeta as RankedPrimeTimeMeta
from gui.impl import backport as backport
from gui.impl.gen import R as R
from helpers import dependency as dependency
from skeletons.connection_mgr import IConnectionManager as IConnectionManager

class FunRandomServerPresenter(ServerListItemPresenter):
    _RES_ROOT = R.strings.fun_random.primeTimes.serverTooltip
    _connectionMgr: Any
    def _compare(self, other):
        ...

class FunRandomPrimeTimeView(RankedPrimeTimeMeta, FunAssetPacksMixin, FunSubModeHolder):
    _RES_ROOT = R.strings.fun_random.primeTimes
    _serverPresenterClass = FunRandomServerPresenter
    def __init__(self, ctx, **kwargs):
        ...
    def _dispose(self):
        ...
    # decorador original: @hasHoldingSubMode(...)
    def _initView(self):
        ...
    # decorador original: @hasHoldingSubMode(...)
    def _clearView(self):
        ...
    def _isAlertBGVisible(self):
        ...
    def _getController(self):
        ...
    def _getPrbActionName(self):
        ...
    def _getPrbForcedActionName(self):
        ...
    def _getServerText(self, serverList, serverInfo, isServerNameShort=False):
        ...
    # decorador original: @filterHoldingSubModeUpdates
    def _onControllerUpdated(self, *args):
        ...
    def _startControllerListening(self):
        ...
    def _stopControllerListening(self):
        ...
