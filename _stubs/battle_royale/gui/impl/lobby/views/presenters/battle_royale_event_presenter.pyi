# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/views/presenters/battle_royale_event_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from battle_royale.gui.impl.gen.view_models.views.lobby.views.battle_royale_event_model import BattleRoyaleEventModel as BattleRoyaleEventModel
from battle_royale.gui.impl.lobby.br_helpers.utils import setEventInfo as setEventInfo
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from helpers import dependency as dependency
from skeletons.gui.game_control import IBattleRoyaleController as IBattleRoyaleController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext

# base nao representavel no stub: ViewComponent[...]
class BattleRoyaleEventPresenter(IGlobalListener):
    __battleRoyaleController: Any
    __lobbyContext: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def onPrbEntitySwitched(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def __update(self, *_):
        ...
