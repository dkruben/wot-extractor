# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/user_missions/hangar_widget/plugins/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from helpers import dependency as dependency
from gui.impl.lobby.user_missions.hangar_widget.services import IMissionsContainerService as IMissionsContainerService

class IUserMissionPlugin(object):
    _missionsContainerService: Any
    _PLUGIN_DESTROY_DELAY = 0
    _pendingDestroyCallbackId = None
    @classmethod
    def getPathToResource(cls):
        ...
    @classmethod
    def getDependencies(cls):
        ...
    @classmethod
    def getViewAlias(cls):
        ...
    @classmethod
    def isPluginEnabled(cls):
        ...
    @classmethod
    def startListening(cls):
        ...
    @classmethod
    def stopListening(cls):
        ...
    @classmethod
    def cancelPendingUpdates(cls):
        ...
    @classmethod
    def _onUpdate(cls, *args, **kwargs):
        ...
    @classmethod
    def _performUpdate(cls, *args, **kwargs):
        ...
