# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/platform/wgnp/steam_account/controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import time as time
import wg_async as wg_async
from BWUtil import AsyncReturn as AsyncReturn
from constants import EMAIL_CONFIRMATION_TOKEN_NAME as EMAIL_CONFIRMATION_TOKEN_NAME
from gui.platform.base.statuses.controller_mixin import StatusesMixin as StatusesMixin
from gui.platform.base.statuses.constants import StatusTypes as StatusTypes, DEFAULT_CONTEXT as DEFAULT_CONTEXT
from gui.platform.wgnp.base.controller import WGNPRequestController as WGNPRequestController
from gui.platform.wgnp.steam_account.request import EmailStatusParams as EmailStatusParams, AddEmailParams as AddEmailParams, ConfirmEmailParams as ConfirmEmailParams
from gui.platform.wgnp.steam_account.statuses import SteamAccEmailStatus as SteamAccEmailStatus, createEmailStatusFromResponse as createEmailStatusFromResponse
from skeletons.gui.platform.wgnp_controllers import IWGNPSteamAccRequestController as IWGNPSteamAccRequestController

class WGNPSteamAccRequestController(StatusesMixin, WGNPRequestController, IWGNPSteamAccRequestController):
    _emailAddedTime: Any
    def __init__(self):
        ...
    @property
    def emailAddedTime(self):
        ...
    # decorador original: @wg_async.wg_async
    def getEmailStatus(self, waitingID=None):
        ...
    # decorador original: @wg_async.wg_async
    def addEmail(self, email, waitingID=None):
        ...
    # decorador original: @wg_async.wg_async
    def confirmEmail(self, code, waitingID=None):
        ...
    def _getStatusTokensSettings(self):
        ...
