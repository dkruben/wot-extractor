# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/avatar_helpers/AvatarSyncData.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import AccountCommands as AccountCommands

class AvatarSyncData(object):
    __isSynchronized: Any
    __subscribers: Any
    __avatar: Any
    def __init__(self):
        ...
    def setAvatar(self, avatar):
        ...
    def onAvatarBecomePlayer(self):
        ...
    def onAvatarBecomeNonPlayer(self):
        ...
    def waitForSync(self, callback):
        ...
    def __onSyncResponse(self, syncID, resultID, ext=None):
        ...
