# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/account_completion/steam_add_email_overlay_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.impl.backport import text as loc
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.account_completion.tooltips.tooltip_constants import TooltipConstants as TooltipConstants
from gui.impl.lobby.account_completion.common import errors as errors
from gui.impl.lobby.account_completion.common.base_credentials_overlay_view import BaseCredentialsOverlayView as BaseCredentialsOverlayView
from gui.impl.lobby.account_completion.utils.common import showAccountAlreadyHasEmail as showAccountAlreadyHasEmail, RESTRICTED_REQUEST_MIN_TIME as RESTRICTED_REQUEST_MIN_TIME
from gui.impl.pub.tooltip_window import SimpleTooltipContent as SimpleTooltipContent
from gui.shared.event_dispatcher import showSteamConfirmEmailOverlay as showSteamConfirmEmailOverlay
from helpers import dependency as dependency
from helpers.time_utils import getTimeDeltaFromNow as getTimeDeltaFromNow
from skeletons.gui.game_control import ISteamCompletionController as ISteamCompletionController
from skeletons.gui.platform.wgnp_controllers import IWGNPSteamAccRequestController as IWGNPSteamAccRequestController
from wg_async import _Future as _Future
from gui.platform.wgnp.steam_account.request import AddEmailParams as WGNPSAAddEmailParams
from gui.impl.gen.view_models.views.lobby.account_completion.add_credentials_model import AddCredentialsModel as AddCredentialsModel
rAccCompletion = R.strings.dialogs.accountCompletion

class SteamAddEmailOverlayView(BaseCredentialsOverlayView):
    __slots__: tuple
    _TITLE: Any
    _SUBTITLE: Any
    _REWARDS_TITLE: Any
    __wgnpSteamAccCtrl: Any
    __accountCompletionCtrl: Any
    def createToolTipContent(self, event, contentID):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _validateInput(self):
        ...
    def _doRequest(self):
        ...
    def _handleSuccess(self, *_):
        ...
    def _handleError(self, response):
        ...
    def _getEmailErrorMessage(self, response):
        ...
