# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/helpers/__init__.py (BYTECODE: a descompilacao falhou; sem bases, decoradores nem valores por omissao).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import os as os
import enum as enum
from past.builtins import unicode as unicode
from future.utils import viewitems as viewitems
import BigWorld as BigWorld
import ResMgr as ResMgr
import constants as constants
from aih_constants import CTRL_MODE_NAME as CTRL_MODE_NAME, CTRL_MODES as CTRL_MODES
from debug_utils import LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION
from helpers import i18n as i18n
from math_common import round_py2_style_int as round_py2_style_int
from soft_exception import SoftException as SoftException
from external_strings_utils import unicode_from_utf8 as unicode_from_utf8
absolute_import: Any
VERSION_FILE_PATH: Any
_CLIENT_VERSION: Any
LOC_VERSION_FILE_PATH: Any
_g_alphabetOrderExcept: Any

# gerado do bytecode: classes base desconhecidas
class ReferralButtonHandler:
    def invoke(cls, **kwargs):
        ...

# gerado do bytecode: classes base desconhecidas
class ClanQuestButtonHandler:
    def invoke(cls, **kwargs):
        ...

# gerado do bytecode: classes base desconhecidas
class ClanSupplyQuestButtonHandler:
    def invoke(cls, **kwargs):
        ...

# gerado do bytecode: classes base desconhecidas
class ExitCode:
    SUCCESS: Any
    FAILED: Any

def gEffectsDisabled():
    ...
def isPlayerAccount():
    ...
def isPlayerAvatar():
    ...
def isPlayerExist():
    ...
def getLanguageCode():
    ...
def getClientLanguage():
    ...
def getClientOverride():
    ...
def getLocalizedData(dataDict, key, defVal=...):
    ...
def int2roman(number):
    ...
def getClientVersion(force=...):
    ...
def getShortClientVersion():
    ...
def getFullClientVersion():
    ...
def newFakeModel():
    ...
def _getSymOrderIdx(symbol):
    ...
def strcmp(word1, word2):
    ...
def setHangarVisibility(isVisible):
    ...
def getHelperServicesConfig(manager):
    ...
def isShowingKillCam():
    ...
def getVisibilityControllerMask(controlModes):
    ...
def unicodeToStr(data):
    ...
def getPreferencesDirPath():
    ...

def __getattr__(name: str) -> Any: ...  # stub incompleto (gerado do bytecode)
