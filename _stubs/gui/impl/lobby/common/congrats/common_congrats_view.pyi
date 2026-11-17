# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/common/congrats/common_congrats_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags
from gui.impl.gen.resources import R as R
from gui.impl.gen.view_models.views.lobby.common.congrats.common_congrats_view_model import CommonCongratsViewModel as CommonCongratsViewModel
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.lobby_window import LobbyWindow as LobbyWindow
from gui.shared.view_helpers.blur_manager import CachedBlur as CachedBlur
_logger: Any

class _CommonCongratsView(ViewImpl):
    __ctx: Any
    _blur: Any
    def __init__(self, context):
        ...
    @property
    def viewModel(self):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def __updateVM(self):
        ...
    def __addListeners(self):
        ...
    def __removeListeners(self):
        ...
    def __onConfirm(self):
        ...
    def __onBack(self):
        ...
    def __onClose(self):
        ...
    def __destroyWindow(self):
        ...

class CongratsWindow(LobbyWindow):
    __slots__: tuple
    def __init__(self, context):
        ...
