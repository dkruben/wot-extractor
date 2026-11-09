# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/epicBattle/epic_prime_time.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import Configs as Configs
from gui.Scaleform.daapi.view.lobby.prime_time_view_base import ServerListItemPresenter as ServerListItemPresenter
from gui.Scaleform.daapi.view.meta.EpicPrimeTimeMeta import EpicPrimeTimeMeta as EpicPrimeTimeMeta
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.prb_control.settings import PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME
from gui.shared.event_dispatcher import showHangar as showHangar
from gui.shared.formatters import text_styles as text_styles, time_formatters as time_formatters
from helpers import dependency as dependency
from helpers import time_utils as time_utils
from skeletons.gui.game_control import IEpicBattleMetaGameController as IEpicBattleMetaGameController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext

class EpicBattleServerPresenter(ServerListItemPresenter):
    def _buildTooltip(self, peripheryID):
        ...
    def _getEndOfCycleTooltipText(self):
        ...

class EpicBattlesPrimeTimeView(EpicPrimeTimeMeta):
    _serverPresenterClass = EpicBattleServerPresenter
    __epicController: Any
    __lobbyContext: Any
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _isAlertBGVisible(self):
        ...
    def _getController(self):
        ...
    def _getPrbActionName(self):
        ...
    def _getPrbForcedActionName(self):
        ...
    def _getStatusText(self):
        ...
    def _getTimeText(self, serverInfo):
        ...
    def _getCycleFinishedOnThisServerText(self, cycleNumber, serverName):
        ...
    def _onServerSettingsChange(self, diff):
        ...
    def _setHeaderText(self):
        ...
    def _setBackground(self):
        ...
    def _setFullscreenModeSupported(self):
        ...
    def _setCloseBtnVisibility(self):
        ...
    def _setShadowVisibility(self):
        ...
