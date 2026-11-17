# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/gui/Scaleform/view/lobby/antispam_message.py (BYTECODE: a descompilacao falhou; sem bases, decoradores nem valores por omissao).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import IS_CHINA as IS_CHINA
from account_helpers.settings_core.ServerSettingsManager import SETTINGS_SECTIONS as SETTINGS_SECTIONS
from account_helpers.settings_core.settings_constants import CONTACTS as CONTACTS
from helpers import dependency as dependency
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
absolute_import: Any
MAX_ANTISPAM_MESSAGES: Any
_isClosed: Any

def isShown():
    ...
def close():
    ...
def reset():
    ...
def _getCounter(settingsCore=...):
    ...
def _setCounter(counter, settingsCore=...):
    ...

def __getattr__(name: str) -> Any: ...  # stub incompleto (gerado do bytecode)
