# wot-extractor: STUB (.pyi) gerado a partir de sources/res/advent_calendar/scripts/client/advent_calendar/notification/decorators.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.shared.notifications import NotificationGroup as NotificationGroup, NotificationGuiSettings as NotificationGuiSettings
from messenger import g_settings as g_settings
from notification.decorators import MessageDecorator as MessageDecorator
from notification.settings import NOTIFICATION_TYPE as NOTIFICATION_TYPE

class DoorsAvailableDecorator(MessageDecorator):
    __notificationName: Any
    def __init__(self, entityID, model, notificationData, notificationName):
        ...
    def getGroup(self):
        ...
    def getType(self):
        ...
    def __makeEntity(self, linkageData):
        ...
    @staticmethod
    def __makeSettings(priority):
        ...
