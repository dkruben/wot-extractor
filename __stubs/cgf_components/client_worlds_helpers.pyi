# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/cgf_components/client_worlds_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import enum as enum
import BattleReplay as BattleReplay
from constants import IS_UE_EDITOR as IS_UE_EDITOR
from helpers import isPlayerAccount as isPlayerAccount, isPlayerAvatar as isPlayerAvatar

class ClientWorld(enum.IntEnum):
    NONE = 0
    BATTLE = 1
    HANGAR = 2
    EDITOR = 4
    AllWorlds: Any

def getClientWorld():
    ...
def clientWorldsPredicate(clientWorlds):
    ...
