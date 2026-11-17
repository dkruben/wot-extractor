# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/rankedBattles/ranked_battles_prime_time_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from past.builtins import cmp as cmp
from helpers import dependency as dependency
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.prb_control.settings import PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME
from gui.ranked_battles.ranked_helpers.sound_manager import RANKED_SUBVIEW_SOUND_SPACE as RANKED_SUBVIEW_SOUND_SPACE
from gui.Scaleform.daapi.view.lobby.prime_time_view_base import ServerListItemPresenter as ServerListItemPresenter
from gui.Scaleform.daapi.view.meta.RankedPrimeTimeMeta import RankedPrimeTimeMeta as RankedPrimeTimeMeta
from skeletons.connection_mgr import IConnectionManager as IConnectionManager
from skeletons.gui.game_control import IRankedBattlesController as IRankedBattlesController

class RankedServerPresenter(ServerListItemPresenter):
    _RES_ROOT = R.strings.ranked_battles.primeTimes.serverTooltip
    _connectionMgr: Any
    def _compare(self, other):
        ...

class RankedBattlesPrimeTimeView(RankedPrimeTimeMeta):
    _COMMON_SOUND_SPACE = RANKED_SUBVIEW_SOUND_SPACE
    _RES_ROOT = R.strings.ranked_battles.primeTimes
    _serverPresenterClass = RankedServerPresenter
    __rankedController: Any
    def _getController(self):
        ...
    def _populate(self):
        ...
    def _isAlertBGVisible(self):
        ...
    def _getPrbActionName(self):
        ...
    def _getPrbForcedActionName(self):
        ...
