# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/login/Preferences.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import json as json
import BigWorld as BigWorld
import Settings as Settings
import constants as constants
from predefined_hosts import AUTO_LOGIN_QUERY_URL as AUTO_LOGIN_QUERY_URL
from debug_utils import LOG_DEBUG as LOG_DEBUG, LOG_WARNING as LOG_WARNING
from gui import GUI_SETTINGS as GUI_SETTINGS

class Preferences(dict):
    __oldFormat: Any
    def __init__(self):
        ...
    def writeLoginInfo(self):
        ...
    def __invalidateSettingsSanity(self):
        ...
    def __readOldPreferencesFormat(self, loginInfo):
        ...
    def __getitem__(self, key):
        ...
    def __repr__(self):
        ...

def _crypt(data):
    ...
def _decrypt(data):
    ...
def _LOG_PERSONAL_DATA(msg, *kargs, **kwargs):
    ...
