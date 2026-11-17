# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/views/presenters/battle_type_selector_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from battle_royale.gui.constants import BattleRoyaleSubMode as BattleRoyaleSubMode
from battle_royale.gui.impl.gen.view_models.views.lobby.views.battle_type_selector_view_model import BattleTypeSelectorViewModel as BattleTypeSelectorViewModel, BattleType as BattleType
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.impl.gui_decorators import args2params as args2params
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from helpers import dependency as dependency
from skeletons.gui.game_control import IBattleRoyaleController as IBattleRoyaleController
SubModeIdToBattleType: dict
BattleTypeToSubMode: dict

# base nao representavel no stub: ViewComponent[...]
class BattleTypeSelectorPresenter(IGlobalListener):
    __battleRoyaleController: Any
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
    def __addListeners(self):
        ...
    def __removeListeners(self):
        ...
    # decorador original: @args2params(...)
    def __onSelectTab(self, tabId):
        ...
    def __update(self, *_):
        ...
    def __onSubModeUpdated(self, *args):
        ...
