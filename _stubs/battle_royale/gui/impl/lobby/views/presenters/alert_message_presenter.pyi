# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/views/presenters/alert_message_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import json as json
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from helpers import dependency as dependency
from helpers import time_utils as time_utils
from skeletons.gui.game_control import IBattleRoyaleController as IBattleRoyaleController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from battle_royale.gui.constants import BattleRoyaleModeState as BattleRoyaleModeState
from battle_royale.gui.impl.gen.view_models.views.lobby.views.alert_message_model import AlertMessageModel as AlertMessageModel, AlertType as AlertType
from battle_royale.gui.shared.event_dispatcher import showBattleRoyalePrimeTime as showBattleRoyalePrimeTime
_BATTLE_ROYALE_MODE_STATE_TO_ALERT_TYPE: dict

# base nao representavel no stub: ViewComponent[...]
class AlertMessagePresenter(IGlobalListener):
    __battleRoyaleController: Any
    __lobbyContext: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def _getEvents(self):
        ...
    def onPrbEntitySwitched(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def __update(self, *_):
        ...
    def __updateBattleSchedule(self, model):
        ...
    @staticmethod
    def __onChangeServer():
        ...
