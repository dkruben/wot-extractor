# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/gui/Scaleform/channels/bw_chat2/factories.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import PREBATTLE_TYPE as PREBATTLE_TYPE, ARENA_GUI_TYPE as ARENA_GUI_TYPE
from messenger.gui.gameface.channels.GFChannelController import GFChannelController as GFChannelController
from messenger.gui.Scaleform.channels.bw_chat2 import battle_controllers as battle_controllers
from messenger.gui.Scaleform.channels.bw_chat2 import lobby_controllers as lobby_controllers
from messenger.gui.interfaces import IControllerFactory as IControllerFactory
from messenger.m_constants import BATTLE_CHANNEL as BATTLE_CHANNEL
from messenger.proto.bw_chat2 import find_criteria as find_criteria
from messenger.proto.bw_chat2.wrappers import CHAT_TYPE as CHAT_TYPE
from messenger.storage import MessengerStorageDescriptor as MessengerStorageDescriptor, ChannelsStorage as ChannelsStorage
from gui.shared.system_factory import registerBattleChanelController as registerBattleChanelController, collectBattleChanelController as collectBattleChanelController
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider

class LobbyControllersFactory(IControllerFactory):
    channelsStorage: Any
    def init(self):
        ...
    def factory(self, channel):
        ...

class BattleControllersFactory(IControllerFactory):
    channelsStorage: Any
    def init(self):
        ...
    def factory(self, channel):
        ...
