# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/winback/winback_umg_intro_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import WindowFlags as WindowFlags
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.winback.winback_umg_intro_view_model import WinbackUmgIntroViewModel as WinbackUmgIntroViewModel
from gui.impl.pub.lobby_window import LobbyWindow as LobbyWindow
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.shared.system_factory import collectDynamicUmgWinbackPresenters as collectDynamicUmgWinbackPresenters
from helpers import dependency as dependency
from skeletons.gui.game_control import IBattlePassController as IBattlePassController

# base nao representavel no stub: ViewComponent[...]
class WinbackUmgIntroView:
    __battlePass: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def _getChildComponents(self):
        ...
    def __update(self, *_):
        ...
    def __onClose(self):
        ...

class WinbackUmgIntroWindow(LobbyWindow):
    def __init__(self, parent=None):
        ...
