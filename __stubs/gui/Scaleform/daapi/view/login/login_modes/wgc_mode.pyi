# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/login/login_modes/wgc_mode.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import WGC as WGC
from constants import IS_CHINA as IS_CHINA
from gui.Scaleform.daapi.view.login.login_modes.base_wgc_mode import BaseWgcMode as BaseWgcMode
from gui.Scaleform.locale.MENU import MENU as MENU
from gui.impl import backport as backport
from gui.impl.gen import R as R
from helpers.i18n import makeString as _ms
from predefined_hosts import g_preDefinedHosts as g_preDefinedHosts

class WgcMode(BaseWgcMode):
    __wgcStoredUserSelected: Any
    def __init__(self, *args):
        ...
    @property
    def login(self):
        ...
    def onPopulate(self):
        ...
    def destroy(self):
        ...
    def updateForm(self):
        ...
    def changeAccount(self):
        ...
    def doLogin(self, userName, password, serverName, isSocialToken2Login):
        ...
    def doSocialLogin(self, *args):
        ...
    def skipRejectionError(self, loginStatus):
        ...
    def _onWgcError(self):
        ...
    def __stop(self):
        ...
