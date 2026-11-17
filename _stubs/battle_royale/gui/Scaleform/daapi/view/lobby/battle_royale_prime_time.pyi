# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/Scaleform/daapi/view/lobby/battle_royale_prime_time.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import Configs as Configs
from gui.Scaleform.daapi.view.lobby.epicBattle.epic_prime_time import EpicBattlesPrimeTimeView as EpicBattlesPrimeTimeView
from gui.Scaleform.daapi.view.lobby.epicBattle.epic_prime_time import EpicBattleServerPresenter as EpicBattleServerPresenter
from gui.shared.event_dispatcher import showHangar as showHangar
from helpers import dependency as dependency
from skeletons.gui.game_control import IBattleRoyaleController as IBattleRoyaleController
from gui.prb_control.settings import PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME
from gui.impl import backport as backport
from gui.impl.gen import R as R

class BattleRoyaleServerPresenter(EpicBattleServerPresenter):
    def _getEndOfCycleTooltipText(self):
        ...

class BattleRoyalePrimeTimeView(EpicBattlesPrimeTimeView):
    _serverPresenterClass = BattleRoyaleServerPresenter
    __battleRoyale: Any
    def _getController(self):
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
    def _getTimeText(self, serverInfo):
        ...
    def _getCycleFinishedOnThisServerText(self, cycleNumber, serverName):
        ...
    def _getPrbActionName(self):
        ...
    def _getPrbForcedActionName(self):
        ...
    def _onServerSettingsChange(self, diff):
        ...
