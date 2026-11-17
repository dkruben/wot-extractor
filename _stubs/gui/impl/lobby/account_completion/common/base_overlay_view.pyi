# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/account_completion/common/base_overlay_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from PlayerEvents import g_playerEvents as g_playerEvents
from gui.impl.lobby.account_completion.curtain.curtain_base_sub_view import CurtainBaseSubView as CurtainBaseSubView
from gui.impl.lobby.account_completion.curtain.curtain_view import CurtainWindow as CurtainWindow
from gui.impl.lobby.account_completion.utils.common import openMenu as openMenu
from gui.impl.gen.view_models.views.lobby.account_completion.common.base_overlay_view_model import BaseOverlayViewModel as BaseOverlayViewModel

class BaseOverlayView(CurtainBaseSubView):
    __slots__: tuple
    _IS_CLOSE_BUTTON_VISIBLE = True
    _onClose: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def activate(self, onClose=None, *args, **kwargs):
        ...
    def deactivate(self):
        ...
    def hide(self):
        ...
    def reveal(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _onAccountBecomeNonPlayer(self):
        ...
    def _escapePressHandler(self):
        ...
    def _closeClickedHandler(self):
        ...
