# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/account_completion/steam_confirm_email_overlay_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.impl.backport import text as loc
from gui.impl.gen import R as R
from gui.impl.lobby.account_completion.common import errors as errors
from gui.impl.lobby.account_completion.common.base_confirm_credentials_overlay_view import BaseConfirmCredentialsOverlayView as BaseConfirmCredentialsOverlayView
from gui.impl.lobby.account_completion.utils.common import showAccountAlreadyHasEmail as showAccountAlreadyHasEmail
from gui.shared.event_dispatcher import showSteamAddEmailOverlay as showSteamAddEmailOverlay
from helpers import dependency as dependency
from skeletons.gui.game_control import ISteamCompletionController as ISteamCompletionController
from skeletons.gui.platform.wgnp_controllers import IWGNPSteamAccRequestController as IWGNPSteamAccRequestController
from wg_async import _Future as _Future
from gui.platform.wgnp.steam_account.request import ConfirmEmailParams as WGNPSAConfirmEmailParams
res = R.strings.dialogs.accountCompletion

class SteamConfirmEmailOverlayView(BaseConfirmCredentialsOverlayView):
    __slots__: tuple
    _wgnpSteamAccCtrl: Any
    __accountCompletionCtrl: Any
    def _getEmailAddedTime(self):
        ...
    def _doRequest(self):
        ...
    def _handleError(self, response):
        ...
    def _onResend(self):
        ...
    def _closeClickedHandler(self):
        ...
