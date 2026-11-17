# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/mapbox/mapbox_prime_time_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.daapi.view.lobby.prime_time_view_base import ServerListItemPresenter as ServerListItemPresenter
from gui.Scaleform.daapi.view.meta.RankedPrimeTimeMeta import RankedPrimeTimeMeta as RankedPrimeTimeMeta
from helpers import dependency as dependency, time_utils as time_utils
from skeletons.gui.game_control import IMapboxController as IMapboxController
from gui.prb_control.settings import PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME
from gui.periodic_battles.models import PrimeTimeStatus as PrimeTimeStatus
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import text_styles as text_styles, time_formatters as time_formatters

class MapboxServerPresenter(ServerListItemPresenter):
    def isEnabled(self):
        ...
    def _buildTooltip(self, peripheryID):
        ...

class MapboxPrimeTimeView(RankedPrimeTimeMeta):
    _serverPresenterClass = MapboxServerPresenter
    __mapboxCtrl: Any
    def _getController(self):
        ...
    def _populate(self):
        ...
    def _prepareData(self, serverList, serverInfo):
        ...
    def _getActualServers(self):
        ...
    def _getServerText(self, serverList, serverInfo, isServerNameShort=False):
        ...
    def _setHeaderData(self):
        ...
    def _setBackground(self):
        ...
    def _getPrbActionName(self):
        ...
    def _getPrbForcedActionName(self):
        ...
    def __getStatusTitle(self):
        ...
    def __getTimeText(self, serverInfo):
        ...
