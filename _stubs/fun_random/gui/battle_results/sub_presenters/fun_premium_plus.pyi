# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/battle_results/sub_presenters/fun_premium_plus.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from constants import PremiumConfigs as PremiumConfigs
from fun_random.gui.battle_results.packers.fun_packers import FunRandomPremiumPlus as FunRandomPremiumPlus
from gui.battle_results.presenters.battle_results_sub_presenter import BattleResultsSubPresenter as BattleResultsSubPresenter
from gui.impl.gui_decorators import args2params as args2params
from gui.impl.gen.view_models.views.lobby.battle_results.premium_plus_model import PremiumPlusModel as PremiumPlusModel
from gui.shared import events as events
from helpers import dependency as dependency, server_settings as server_settings
from skeletons.gui.game_control import IGameSessionController as IGameSessionController, IWotPlusController as IWotPlusController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from frameworks.wulf import ViewModel as ViewModel
from gui.battle_results.stats_ctrl import BattleResults as BattleResults

class FunPremiumPlusSubPresenter(BattleResultsSubPresenter):
    __gameSession: Any
    __lobbyContext: Any
    __wotPlusController: Any
    @classmethod
    def getViewModelType(cls):
        ...
    def packBattleResults(self, battleResults):
        ...
    def _getEvents(self):
        ...
    def _getListeners(self):
        ...
    def _getCallbacks(self):
        ...
    # decorador original: @args2params(...)
    def __onNextBonusTimeUpdate(self, isUpdate):
        ...
    def __onPremiumStatusChanged(self, _=None):
        ...
    # decorador original: @server_settings.serverSettingsChangeListener(...)
    def __onServerSettingsChanged(self, _):
        ...
    def __onXpBonusApplied(self):
        ...
    def __onXpBonusApplyStatusChanged(self, event):
        ...
    def __onXpBonusChanged(self, _=None):
        ...
    def __onWotPlusChanged(self, data):
        ...
