# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/gui/Scaleform/channels/bw/factories.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from messenger.gui.Scaleform.channels.bw import lobby_controllers as lobby_controllers
from messenger.gui.interfaces import IControllerFactory as IControllerFactory
from messenger.m_constants import LAZY_CHANNEL as LAZY_CHANNEL
from messenger.proto.bw import find_criteria as find_criteria
from messenger.storage import MessengerStorageDescriptor as MessengerStorageDescriptor, ChannelsStorage as ChannelsStorage

class LobbyControllersFactory(IControllerFactory):
    channelsStorage: Any
    def init(self):
        ...
    def factory(self, channel):
        ...
