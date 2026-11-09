# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/notification/actions_handlers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from adisp import adisp_process as adisp_process
from fun_random.gui.feature.util.fun_mixins import FunSubModesWatcher as FunSubModesWatcher, FunProgressionWatcher as FunProgressionWatcher
from fun_random.gui.feature.util.fun_wrappers import hasMultipleSubModes as hasMultipleSubModes
from helpers import dependency as dependency
from notification.actions_handlers import NavigationDisabledActionHandler as NavigationDisabledActionHandler
from notification.settings import NOTIFICATION_TYPE as NOTIFICATION_TYPE
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext

class SelectFunRandomMode(NavigationDisabledActionHandler, FunSubModesWatcher):
    __lobbyContext: Any
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    # decorador original: @hasMultipleSubModes(...)
    def checkHeaderNavigation(self):
        ...
    # decorador original: @adisp_process
    def doAction(self, model, entityID, action):
        ...

class ShowFunRandomProgression(NavigationDisabledActionHandler, FunProgressionWatcher):
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def doAction(self, model, entityID, action):
        ...
