# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/gift_system/hubs/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from gifts.gifts_common import GiftEventID as GiftEventID
from gui.gift_system.hubs.base.hub_core import GiftEventBaseHub as GiftEventBaseHub
from gui.gift_system.hubs.dev.hub_core import GiftEventDevHub as GiftEventDevHub
from gui.gift_system.hubs.base.hub_core import IGiftEventHub as IGiftEventHub
from helpers.server_settings import GiftEventConfig as GiftEventConfig
_HUB_BY_EVENT_ID: dict

def createGiftEventHub(eventID, eventSettings, isMessagesAllowed):
    ...
