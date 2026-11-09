# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/account_completion/common/base_wgnp_overlay_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from abc import ABCMeta as ABCMeta, abstractmethod as abstractmethod
import typing as typing
import wg_async as wg_async
from gui.impl.gen import R as R
from gui.impl.lobby.account_completion.common.base_overlay_view import BaseOverlayView as BaseOverlayView
from gui.impl.lobby.account_completion.curtain.curtain_view import CurtainWindow as CurtainWindow
from wg_async import _Future as _Future
from gui.impl.gen.view_models.views.lobby.account_completion.common.base_wgnp_overlay_view_model import BaseWgnpOverlayViewModel as BaseWgnpOverlayViewModel

class BaseWGNPOverlayView(BaseOverlayView, metaclass=ABCMeta):
    __slots__: tuple
    _TITLE: Any
    _SUBTITLE: Any
    @property
    def viewModel(self):
        ...
    def activate(self, *args, **kwargs):
        ...
    def deactivate(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    # decorador original: @wg_async.wg_async
    def _confirmClickedHandler(self):
        ...
    def _warningTimerHandler(self):
        ...
    @abstractmethod
    def _updateConfirmButtonAvailability(self):
        ...
    @abstractmethod
    def _validateInput(self):
        ...
    @abstractmethod
    def _doRequest(self):
        ...
    def _handleSuccess(self, response):
        ...
    @abstractmethod
    def _handleError(self, response):
        ...
    def _setWarning(self, text='', countDown=0):
        ...
