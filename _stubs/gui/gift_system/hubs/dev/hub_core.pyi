# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/gift_system/hubs/dev/hub_core.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from gui.gift_system.hubs.base.hub_core import GiftEventBaseHub as GiftEventBaseHub
from gui.gift_system.hubs.dev import IDevMessagesPusher as IDevMessagesPusher
from gui.gift_system.hubs.dev.stamper import GiftEventDevStamper as GiftEventDevStamper
from gui.gift_system.hubs.dev.gifter import GiftEventDevGifter as GiftEventDevGifter
from gui.gift_system.hubs.dev.messenger import GiftEventDevMessenger as GiftEventDevMessenger
from gui.gift_system.hubs.dev.relations_keeper import GiftEventDevKeeper as GiftEventDevKeeper
from gui.gift_system.hubs.base.stamper import IGiftEventStamper as IGiftEventStamper
from gui.gift_system.hubs.base.gifter import IGiftEventGifter as IGiftEventGifter
from gui.gift_system.hubs.base.messenger import IGiftEventMessenger as IGiftEventMessenger
from gui.gift_system.hubs.base.relations_keeper import IGiftEventKeeper as IGiftEventKeeper
from gui.gift_system.wrappers import SendGiftResponse as SendGiftResponse
from helpers.server_settings import GiftEventConfig as GiftEventConfig
_logger: Any

class GiftEventDevHub(GiftEventBaseHub, IDevMessagesPusher):
    __slots__: tuple
    def __init__(self, eventSettings, isMessagesAllowed):
        ...
    def __repr__(self):
        ...
    def destroy(self):
        ...
    def reset(self):
        ...
    def _createGifter(self, eventSettings):
        ...
    def _createKeeper(self, eventSettings):
        ...
    def _createMessenger(self, eventSetting, isMessagesAllowed):
        ...
    def _createStamper(self, eventSettings):
        ...
    def _onGifterResponse(self, responseData):
        ...
    def _onKeeperCleared(self):
        ...
    def _onStamperUpdate(self):
        ...
    def _updateSettings(self, eventSettings):
        ...
