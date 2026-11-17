# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/account_helpers/gameplay_ctx.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import ArenaType as ArenaType
import constants as constants
from debug_utils import LOG_DEBUG as LOG_DEBUG, LOG_ERROR as LOG_ERROR, LOG_WARNING as LOG_WARNING
from helpers import dependency as dependency
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
_ASSAULT2_GP_NAME: Any
ENABLED_ARENA_GAMEPLAY_NAMES: Any
ENABLED_ARENA_EPIC_NAMES: tuple

def getDefaultMask():
    ...
def getMask():
    ...
def setMaskByNames(names):
    ...
def isCreationEnabled(gameplayName, isEpic):
    ...
def _setMask(gameplayMask):
    ...
