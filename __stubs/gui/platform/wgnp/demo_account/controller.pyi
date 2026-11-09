# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/platform/wgnp/demo_account/controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import time as time
import wg_async as wg_async
from BWUtil import AsyncReturn as AsyncReturn
from constants import EMAIL_CONFIRMATION_TOKEN_NAME as EMAIL_CONFIRMATION_TOKEN_NAME
from gui.platform.base.statuses.controller_mixin import StatusesMixin as StatusesMixin
from gui.platform.base.statuses.constants import DEFAULT_CONTEXT as DEFAULT_CONTEXT, StatusTypes as StatusTypes
from gui.platform.wgnp.base.controller import WGNPRequestController as WGNPRequestController
from gui.platform.wgnp.demo_account.request import CredentialsStatusParams as CredentialsStatusParams, AddCredentialsParams as AddCredentialsParams, ConfirmCredentialsParams as ConfirmCredentialsParams, NicknameStatusParams as NicknameStatusParams, ChangeNicknameParams as ChangeNicknameParams, ValidateNicknameParams as ValidateNicknameParams
from gui.platform.wgnp.demo_account.statuses import DemoAccCredentialsStatus as DemoAccCredentialsStatus, createCredentialsConfirmationStatus as createCredentialsConfirmationStatus, createCredentialStatusFromResponse as createCredentialStatusFromResponse, DemoAccNicknameStatus as DemoAccNicknameStatus, createNicknameStatusFromResponse as createNicknameStatusFromResponse
from skeletons.gui.platform.wgnp_controllers import IWGNPDemoAccRequestController as IWGNPDemoAccRequestController
NICKNAME_CONTEXT = '<nickname>'

class WGNPDemoAccRequestController(StatusesMixin, WGNPRequestController, IWGNPDemoAccRequestController):
    _credentialsAddedTime: Any
    def __init__(self):
        ...
    @property
    def credentialsAddedTime(self):
        ...
    # decorador original: @wg_async.wg_async
    def getCredentialsStatus(self, waitingID=None):
        ...
    # decorador original: @wg_async.wg_async
    def addCredentials(self, login, password, waitingID=None):
        ...
    # decorador original: @wg_async.wg_async
    def confirmCredentials(self, code, waitingID=None):
        ...
    # decorador original: @wg_async.wg_async
    def getNicknameStatus(self, waitingID=None, force=False):
        ...
    # decorador original: @wg_async.wg_async
    def validateNickname(self, nickname, waitingID=None):
        ...
    # decorador original: @wg_async.wg_async
    def changeNickname(self, nickname, cost, waitingID=None):
        ...
    # decorador original: @wg_async.wg_async
    def _renameRequest(self, params, waitingID=None):
        ...
    def _checkIsEnabled(self, diff):
        ...
    def _getStatusTokensSettings(self):
        ...
