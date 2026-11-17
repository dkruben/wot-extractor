# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_core/scripts/client/comp7_core/gui/Scaleform/daapi/view/lobby/comp7_core_prime_time_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from comp7_core.gui.impl.lobby.comp7_core_helpers import comp7_core_model_helpers as comp7_core_model_helpers
from gui.Scaleform.daapi.view.lobby.prime_time_view_base import ServerListItemPresenter as ServerListItemPresenter, PrimeTimeViewBase as PrimeTimeViewBase
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.periodic_battles.models import PrimeTimeStatus as PrimeTimeStatus
from gui.shared.formatters import text_styles as text_styles, time_formatters as time_formatters
from gui.shared.view_helpers.blur_manager import CachedBlur as CachedBlur
from helpers import time_utils as time_utils

class Comp7CoreServerPresenter(ServerListItemPresenter):
    def isEnabled(self):
        ...
    def _buildTooltip(self, peripheryID):
        ...

class Comp7CorePrimeTimeView(PrimeTimeViewBase):
    _RES_STATUS_ROOT = None
    _serverPresenterClass = Comp7CoreServerPresenter
    __BLUR_INTENSITY = 0.5
    __blur: Any
    def __init__(self, **kwargs):
        ...
    @property
    def _seasonNameClazz(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _startControllerListening(self):
        ...
    def _stopControllerListening(self):
        ...
    def _prepareData(self, serverList, serverInfo):
        ...
    def _getActualServers(self):
        ...
    def __getStatusTitle(self):
        ...
    def __getTimeText(self, serverInfo):
        ...
