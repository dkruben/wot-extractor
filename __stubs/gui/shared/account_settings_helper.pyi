# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/account_settings_helper.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import GUI_START_BEHAVIOR as GUI_START_BEHAVIOR
from helpers import dependency as dependency
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore

class WelcomeScreen(CONST_CONTAINER):
    CREW_NPS_WELCOME = 'crewNpsWelcome'

class AccountSettingsHelper(object):
    settingsCore: Any
    @classmethod
    def welcomeScreenShown(cls, screen):
        ...
    @classmethod
    def isWelcomeScreenShown(cls, screen):
        ...
