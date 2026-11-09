# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/login/login_modes/social_mode.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from connection_mgr import LOGIN_STATUS as LOGIN_STATUS
from constants import IS_CHINA as IS_CHINA
from gui import makeHtmlString as makeHtmlString
from gui.Scaleform.daapi.view.login.login_modes.base_mode import BaseMode as BaseMode, INVALID_FIELDS as INVALID_FIELDS
from gui.Scaleform.Waiting import Waiting as Waiting
from gui.login.social_networks import SOCIAL_NETWORKS as SOCIAL_NETWORKS
from helpers import dependency as dependency
from helpers.i18n import makeString as _ms
from skeletons.connection_mgr import IConnectionManager as IConnectionManager
SOCIAL_NETWORK_TO_DOMAIN_MAPPING: dict

class SocialMode(BaseMode):
    _connectionMgr: Any
    @property
    def login(self):
        ...
    @property
    def rememberUser(self):
        ...
    @property
    def password(self):
        ...
    @property
    def rememberPassVisible(self):
        ...
    def onPopulate(self):
        ...
    def destroy(self):
        ...
    def isToken2(self):
        ...
    def resetToken(self):
        ...
    def setRememberPassword(self, *args):
        ...
    def doLogin(self, *args):
        ...
    def doSocialLogin(self, socialNetworkName, serverName, isRegistration):
        ...
    def updateForm(self):
        ...
    def changeAccount(self):
        ...
    def __onLoginRejected(self, loginStatus, _):
        ...
    def __setSocialDataList(self, socialList):
        ...
    def __getLogoutWarning(self, socialNetworkName):
        ...
    @staticmethod
    def __getTooltipHeader(socialNetworkName):
        ...
    @staticmethod
    def __getTooltipBody(socialNetworkName):
        ...
