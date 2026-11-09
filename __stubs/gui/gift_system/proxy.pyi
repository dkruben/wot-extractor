# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/gift_system/proxy.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from gifts.gifts_common import GiftEventID as GiftEventID
from gui.gift_system.wrappers import IncomeSysMessage as IncomeSysMessage
from helpers import dependency as dependency
from messenger.formatters.service_channel import ServiceChannelFormatter as ServiceChannelFormatter
from shared_utils import makeTupleByDict as makeTupleByDict
from skeletons.gui.game_control import IGiftSystemController as IGiftSystemController
_logger: Any

class GiftSystemMessagesProxy(ServiceChannelFormatter):
    __giftSystemCtrl: Any
    def format(self, message, *args):
        ...
