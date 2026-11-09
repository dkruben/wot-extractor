# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/login/login_modes/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from gui import GUI_SETTINGS as GUI_SETTINGS
from gui.Scaleform.daapi.view.login.login_modes.wgc_mode import WgcMode as WgcMode
from gui.Scaleform.daapi.view.login.login_modes.steam_mode import SteamMode as SteamMode
from gui.Scaleform.daapi.view.login.login_modes.credentials_mode import CredentialsMode as CredentialsMode
from gui.Scaleform.daapi.view.login.login_modes.social_mode import SocialMode as SocialMode
from helpers import dependency as dependency
from skeletons.gui.login_manager import ILoginManager as ILoginManager
from gui.Scaleform.daapi.view.login.login_modes.base_mode import BaseMode as BaseMode

# decorador original: @dependency.replace_none_kwargs(...)
def createLoginMode(view, loginManager=None):
    ...
