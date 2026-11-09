# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/notification/decorators.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from comp7.gui.impl.lobby.comp7_helpers.comp7_quest_helpers import hasAvailableOfferTokens as hasAvailableOfferTokens
from gui.shared.notifications import NotificationGroup as NotificationGroup, NotificationGuiSettings as NotificationGuiSettings
from helpers import dependency as dependency
from messenger import g_settings as g_settings
from notification.decorators import MessageDecorator as MessageDecorator
from notification.settings import NOTIFICATION_BUTTON_STATE as NOTIFICATION_BUTTON_STATE
from skeletons.gui.game_control import IComp7Controller as IComp7Controller
from skeletons.gui.shared import IItemsCache as IItemsCache

class Comp7BondEquipmentDecorator(MessageDecorator):
    __itemsCache: Any
    __comp7Controller: Any
    __notificationType: Any
    __useCounterOnce: Any
    def __init__(self, entityID, notificationType, savedData, model, template, priority, useCounterOnce=True, isNotify=True):
        ...
    def getType(self):
        ...
    def getGroup(self):
        ...
    def getSavedData(self):
        ...
    def isShouldCountOnlyOnce(self):
        ...
    @staticmethod
    def isPinned():
        ...
    def clear(self):
        ...
    def _make(self, entity=None, settings=None):
        ...
    def __onItemsSyncCompleted(self, *_):
        ...
    def __updateEntityButtons(self):
        ...
    def __getButtonState(self):
        ...
