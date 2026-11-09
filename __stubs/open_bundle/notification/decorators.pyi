# wot-extractor: STUB (.pyi) gerado a partir de sources/res/open_bundle/scripts/client/open_bundle/notification/decorators.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.shared.notifications import NotificationGroup as NotificationGroup, NotificationGuiSettings as NotificationGuiSettings
from helpers import dependency as dependency
from messenger import g_settings as g_settings
from notification.decorators import MessageDecorator as MessageDecorator
from notification.settings import NOTIFICATION_BUTTON_STATE as NOTIFICATION_BUTTON_STATE, NOTIFICATION_TYPE as NOTIFICATION_TYPE
from open_bundle.gui.constants import GFNotificationTemplates as GFNotificationTemplates
from open_bundle.skeletons.open_bundle_controller import IOpenBundleController as IOpenBundleController

class OpenBundleStartDecorator(MessageDecorator):
    def __init__(self, entityID, model=None, data=None):
        ...
    def getGroup(self):
        ...
    def getType(self):
        ...
    @staticmethod
    def __makeEntity(data):
        ...
    @staticmethod
    def __makeSettings():
        ...

class OpenBundleReminderDecorator(MessageDecorator):
    __openBundle: Any
    __ENTITY_ID = 0
    def __init__(self, message, savedData, model):
        ...
    def getSavedData(self):
        ...
    def _getEvents(self):
        ...
    def _make(self, entity=None, settings=None):
        ...
    def __makeEntity(self, message, savedData):
        ...
    def __makeSettings(self):
        ...
    def __updateEntityButtons(self):
        ...
    def __update(self, *_):
        ...
