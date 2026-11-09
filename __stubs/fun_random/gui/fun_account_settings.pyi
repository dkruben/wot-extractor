# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/fun_account_settings.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import copy as copy
from typing import TYPE_CHECKING as TYPE_CHECKING
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import KEY_SETTINGS as KEY_SETTINGS
from fun_random.gui.fun_gui_constants import AccountSettingsConstants as AccountSettingsConstants, ACCOUNT_SUBMODE_DEFAULT_SETTINGS as ACCOUNT_SUBMODE_DEFAULT_SETTINGS
from typing import Any as Any

class FunAccountSettings(object):
    @staticmethod
    def _getSettings():
        ...
    @staticmethod
    def _setSettings(settings):
        ...
    @classmethod
    def getIsTriggerCompletionSeen(cls, triggerID):
        ...
    @classmethod
    def setIsTriggerCompletionSeen(cls, triggerID, isSeen):
        ...

class FunSubModeAccountSettings(object):
    subModeKey: _Any
    def __init__(self, subModeKey):
        ...
    def getSettings(self, name):
        ...
    def setSettings(self, name, value):
        ...
    def isInfoPageShown(self):
        ...
    def setInfoPageShown(self, status):
        ...

def setSubModeDefaultSettings(subModeKey):
    ...
