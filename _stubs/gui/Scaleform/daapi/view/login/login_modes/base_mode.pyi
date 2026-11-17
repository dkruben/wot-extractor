# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/login/login_modes/base_mode.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
from helpers import dependency as dependency
from skeletons.gui.login_manager import ILoginManager as ILoginManager

class INVALID_FIELDS(object):
    ALL_VALID = 0
    LOGIN_INVALID = 1
    PWD_INVALID = 2
    SERVER_INVALID = 4
    LOGIN_PWD_INVALID: Any

class BaseMode(object):
    _loginManager: Any
    _view: Any
    _fallbackMode: Any
    def __init__(self, view, fallbackMode=None):
        ...
    def onPopulate(self):
        ...
    def destroy(self):
        ...
    @property
    def login(self):
        ...
    def doLogin(self, *args):
        ...
    def updateForm(self):
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
    @property
    def showRememberServerWarning(self):
        ...
    def setRememberPassword(self, *args):
        ...
    def isToken2(self):
        ...
    def resetToken(self):
        ...
    def doSocialLogin(self, *args):
        ...
    def changeAccount(self):
        ...
    def skipRejectionError(self, *args):
        ...
