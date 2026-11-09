# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/account_completion/common/base_confirm_credentials_overlay_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import time as time
from abc import abstractmethod as abstractmethod
import typing as typing
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.account_completion.confirm_credentials_model import ConfirmCredentialsModel as ConfirmCredentialsModel
from gui.impl.lobby.account_completion.common.base_wgnp_overlay_view import BaseWGNPOverlayView as BaseWGNPOverlayView
from gui.impl.lobby.account_completion.common.field_presenters import CodePresenter as CodePresenter
from gui.impl.lobby.account_completion.utils.common import DISABLE_BUTTON_TIME as DISABLE_BUTTON_TIME
from typing import Optional as Optional
res = R.strings.dialogs.accountCompletion

class BaseConfirmCredentialsOverlayView(BaseWGNPOverlayView):
    __slots__: tuple
    _TITLE: Any
    _LAYOUT_DYN_ACCESSOR = R.views.lobby.account_completion.ConfirmCredentialsView
    _VIEW_MODEL_CLASS = ConfirmCredentialsModel
    _code: Any
    _email: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def activate(self, email='', *args, **kwargs):
        ...
    def deactivate(self):
        ...
    def _doFinalize(self):
        ...
    def _updateConfirmButtonAvailability(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _cleanNoTimerWarning(self):
        ...
    @abstractmethod
    def _getEmailAddedTime(self):
        ...
    def _validateInput(self):
        ...
    def _updateErrorModel(self, errorMessage, buttonTimer=None, isButtonVisible=True, isButtonEnabled=True, resendButtonLabelResID=...):
        ...
    @abstractmethod
    def _onResend(self):
        ...
