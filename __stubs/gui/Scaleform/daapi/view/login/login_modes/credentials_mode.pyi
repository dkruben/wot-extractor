# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/login/login_modes/credentials_mode.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
import WWISE as WWISE
import constants as constants
from external_strings_utils import _LOGIN_NAME_MIN_LENGTH as _LOGIN_NAME_MIN_LENGTH
from external_strings_utils import isAccountLoginValid as isAccountLoginValid
from gui import GUI_SETTINGS as GUI_SETTINGS
from gui.Scaleform.daapi.view.login.login_modes.base_mode import BaseMode as BaseMode, INVALID_FIELDS as INVALID_FIELDS
from gui.Scaleform.Waiting import Waiting as Waiting
from gui.Scaleform.locale.MENU import MENU as MENU
from gui.impl import backport as backport
from gui.impl.gen import R as R
from helpers.i18n import makeString as _ms
_ValidateCredentialsResult: Any

class CredentialsMode(BaseMode):
    firstRun = True
    _rememberUser: Any
    def __init__(self, *args):
        ...
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
    def setRememberPassword(self, rememberUser):
        ...
    def isToken2(self):
        ...
    def resetToken(self):
        ...
    def doLogin(self, userName, password, serverName, isSocialToken2Login):
        ...
    def updateForm(self):
        ...
    @staticmethod
    def __validateCredentials(userName, password, isToken2Login):
        ...
