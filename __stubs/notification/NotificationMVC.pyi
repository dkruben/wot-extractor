# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/notification/NotificationMVC.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from notification.AlertController import AlertController as AlertController
from notification.NotificationsCounter import NotificationsCounter as NotificationsCounter
from notification.NotificationsModel import NotificationsModel as NotificationsModel
from notification.actions_handlers import NotificationsActionsHandlers as NotificationsActionsHandlers
g_instance: Any

class _NotificationMVC(object):
    __model: Any
    __alertsController: Any
    __actionsHandlers: Any
    __unreadMessagesCounter: Any
    __firstEntry: Any
    def __init__(self):
        ...
    def initialize(self):
        ...
    def getModel(self):
        ...
    def getAlertController(self):
        ...
    def handleAction(self, typeID, entityID, action):
        ...
    def cleanUp(self, resetCounter=False):
        ...
