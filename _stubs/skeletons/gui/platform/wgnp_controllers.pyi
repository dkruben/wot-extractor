# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/skeletons/gui/platform/wgnp_controllers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
import wg_async as wg_async
from gui.platform.base.statuses.constants import DEFAULT_CONTEXT as DEFAULT_CONTEXT
from skeletons.gui.platform.controller import IPlatformRequestController as IPlatformRequestController
from helpers.server_settings import _Wgnp as _Wgnp
from gui.platform.base.statuses.events_mgr import StatusEventsManager as StatusEventsManager
from gui.platform.wgnp.steam_account.statuses import SteamAccEmailStatus as SteamAccEmailStatus
from gui.platform.wgnp.steam_account.request import AddEmailParams as AddEmailParams, ConfirmEmailParams as ConfirmEmailParams
from gui.platform.wgnp.demo_account.statuses import DemoAccCredentialsStatus as DemoAccCredentialsStatus, DemoAccNicknameStatus as DemoAccNicknameStatus
from gui.platform.wgnp.demo_account.request import AddCredentialsParams as AddCredentialsParams, ConfirmCredentialsParams as ConfirmCredentialsParams, ChangeNicknameParams as ChangeNicknameParams, ValidateNicknameParams as ValidateNicknameParams
from gui.platform.wgnp.general.statuses import GeneralAccountCountryStatus as GeneralAccountCountryStatus
from gui.platform.base.statuses.constants import StatusTypes as StatusTypes

class IWGNPRequestController(IPlatformRequestController):
    @property
    def settings(self):
        ...

class IWGNPSteamAccRequestController(IWGNPRequestController):
    # decorador original: @wg_async.wg_async
    def addEmail(self, email, waitingID=None):
        ...
    # decorador original: @wg_async.wg_async
    def getEmailStatus(self, waitingID=None):
        ...
    # decorador original: @wg_async.wg_async
    def confirmEmail(self, code, waitingID=None):
        ...
    @property
    def emailAddedTime(self):
        ...
    @property
    def statusEvents(self):
        ...

class IWGNPDemoAccRequestController(IWGNPRequestController):
    # decorador original: @wg_async.wg_async
    def getCredentialsStatus(self, waitingID=None):
        ...
    # decorador original: @wg_async.wg_async
    def addCredentials(self, login, password, waitingID=None):
        ...
    # decorador original: @wg_async.wg_async
    def confirmCredentials(self, code, waitingID=None):
        ...
    @property
    def credentialsAddedTime(self):
        ...
    @property
    def statusEvents(self):
        ...
    def getCurrentStatus(self, context=...):
        ...
    # decorador original: @wg_async.wg_async
    def getNicknameStatus(self, waitingID=None):
        ...
    # decorador original: @wg_async.wg_async
    def validateNickname(self, nickname, waitingID=None):
        ...
    # decorador original: @wg_async.wg_async
    def changeNickname(self, nickname, cost, waitingID=None):
        ...

class IWGNPGeneralRequestController(IWGNPRequestController):
    # decorador original: @wg_async.wg_async
    def getAccountCountry(self, waitingID=None):
        ...
