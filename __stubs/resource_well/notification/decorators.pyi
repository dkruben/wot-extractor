# wot-extractor: STUB (.pyi) gerado a partir de sources/res/resource_well/scripts/client/resource_well/notification/decorators.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.shared.notifications import NotificationGuiSettings as NotificationGuiSettings, NotificationPriorityLevel as NotificationPriorityLevel
from helpers import dependency as dependency
from messenger import g_settings as g_settings
from notification.decorators import MessageDecorator as MessageDecorator
from notification.settings import NOTIFICATION_TYPE as NOTIFICATION_TYPE, NOTIFICATION_BUTTON_STATE as NOTIFICATION_BUTTON_STATE
from skeletons.gui.resource_well import IResourceWellController as IResourceWellController

class ResourceWellLockButtonDecorator(MessageDecorator):
    __resourceWell: Any
    def __init__(self, entityID, entity=None, settings=None, model=None):
        ...
    def clear(self):
        ...
    def _make(self, entity=None, settings=None):
        ...
    def __updateEntityButtons(self):
        ...
    def __update(self, *_):
        ...

class ResourceWellStartDecorator(ResourceWellLockButtonDecorator):
    def __init__(self, entityID, message, model):
        ...
    def getType(self):
        ...
    def __makeEntity(self, message):
        ...
    def __makeSettings(self):
        ...
