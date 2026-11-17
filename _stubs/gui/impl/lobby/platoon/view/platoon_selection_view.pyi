# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/platoon/view/platoon_selection_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from helpers import dependency as dependency
from frameworks.wulf import WindowFlags as WindowFlags, WindowLayer as WindowLayer, ViewFlags as ViewFlags
from gui.impl.gen import R as R
from gui.impl.gen.view_models.windows.pop_over_window_model import PopOverWindowModel as PopOverWindowModel
from gui.impl.pub import WindowView as WindowView
from gui.shared.events import PlatoonDropdownEvent as PlatoonDropdownEvent
from gui.shared import g_eventBus as g_eventBus
from gui.impl.lobby.platoon.platoon_helpers import PreloadableWindow as PreloadableWindow
from gui.impl.lobby.platoon.view.platoon_welcome_view import WelcomeView as WelcomeView
from skeletons.gui.game_control import IPlatoonController as IPlatoonController
_logger: Any
strButtons = R.strings.platoon.buttons

class SelectionWindow(PreloadableWindow):
    __platoonCtrl: Any
    @property
    def popOverModel(self):
        ...
    @property
    def preBattleView(self):
        ...
    def __init__(self):
        ...
    def show(self, focus=True):
        ...
    def hide(self, destroy=False):
        ...
    def _onContentReady(self):
        ...
    def _finalize(self):
        ...
