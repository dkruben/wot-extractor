# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/login/login_modes/base_wgc_mode.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import WGC as WGC
from account_helpers.settings_core.settings_constants import GAME as GAME
from gui.Scaleform.daapi.view.login.login_modes.base_mode import BaseMode as BaseMode
_g_firstEntry = True

class BaseWgcMode(BaseMode):
    @property
    def login(self):
        ...
    @property
    def showRememberServerWarning(self):
        ...
    def onPopulate(self):
        ...
    def doLogin(self, userName, password, serverName, isSocialToken2Login):
        ...
    def skipRejectionError(self, loginStatus):
        ...
    def updateForm(self):
        ...
    def destroy(self):
        ...
    def _onWgcError(self):
        ...
