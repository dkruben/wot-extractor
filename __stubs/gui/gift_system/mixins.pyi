# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/gift_system/mixins.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gifts.gifts_common import GiftEventID as GiftEventID, GiftEventState as GiftEventState
from gui.gift_system.constants import HubUpdateReason as HubUpdateReason
from gui.gift_system.hubs.base.hub_core import IGiftEventHub as IGiftEventHub
from gui.gift_system.wrappers import filterGiftHubsAction as filterGiftHubsAction
from helpers import dependency as dependency
from skeletons.gui.game_control import IGiftSystemController as IGiftSystemController

class GiftEventHubWatcher(object):
    _GIFT_EVENT_ID = GiftEventID.UNKNOWN
    __giftsController: Any
    _eventHub: Any
    def __init__(self, *args, **kwargs):
        ...
    def isGiftEventDisabled(self, isCached=True):
        ...
    def isGiftEventEnabled(self, isCached=True):
        ...
    def isGiftEventSuspended(self, isCached=True):
        ...
    def getGiftEventState(self, isCached=True):
        ...
    def getGiftEventHub(self, isCached=True):
        ...
    def catchGiftEventHub(self, autoSub=True):
        ...
    def releaseGiftEventHub(self, autoUnsub=True):
        ...
    def _onGiftHubUpdate(self, reason, extra=None):
        ...
    # decorador original: @filterGiftHubsAction(...)
    def __onHubsCreation(self, *_):
        ...
    # decorador original: @filterGiftHubsAction(...)
    def __onHubsDestruction(self, *_):
        ...
    def __subToGiftEventHub(self):
        ...
    def __unsubFromGiftEventHub(self):
        ...
