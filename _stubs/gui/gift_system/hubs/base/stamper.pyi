# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/gift_system/hubs/base/stamper.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.gift_system.hubs.subsystems import BaseHubSubsystem as BaseHubSubsystem
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
from helpers.server_settings import GiftEventConfig as GiftEventConfig

class IGiftEventStamper(BaseHubSubsystem):
    def isBalanceAvailable(self):
        ...
    def wasBalanceAvailable(self):
        ...
    def getStampCount(self, stampName):
        ...

class GiftEventBaseStamper(IGiftEventStamper):
    __slots__: tuple
    _STAMPS: Any
    __itemsCache: Any
    __updateCallback: Any
    __isBalanceAvailable: Any
    __wasBalanceAvailable: Any
    def __init__(self, eventSettings, updateCallback):
        ...
    def destroy(self):
        ...
    def isBalanceAvailable(self):
        ...
    def wasBalanceAvailable(self):
        ...
    def getStampCount(self, stampName):
        ...
    def _isNotificationsEnabled(self):
        ...
    def __initBalanceWatchers(self):
        ...
    def __onItemsSyncCompleted(self, *_):
        ...
    def __notifyGiftEventHub(self):
        ...
    def __updateBalanceAvailability(self, isAvailable):
        ...
    def __updateBalanceContent(self, entitlementsData):
        ...
