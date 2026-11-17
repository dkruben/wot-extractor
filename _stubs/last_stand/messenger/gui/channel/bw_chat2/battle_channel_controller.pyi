# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/messenger/gui/channel/bw_chat2/battle_channel_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import types as types
import BigWorld as BigWorld
from future.utils import viewitems as viewitems
from chat_commands_consts import BATTLE_CHAT_COMMAND_NAMES as BATTLE_CHAT_COMMAND_NAMES
from last_stand_common.last_stand_constants import LSMarkersType as LSMarkersType, LSMarkerComponentNames as LSMarkerComponentNames
from messenger.gui.Scaleform.channels.bw_chat2.battle_controllers import TeamChannelController as TeamChannelController
from messenger.m_constants import MESSENGER_COMMAND_TYPE as MESSENGER_COMMAND_TYPE
from messenger_common_chat2 import MESSENGER_ACTION_IDS as MESSENGER_ACTION_IDS
from gui.impl import backport as backport
from gui.impl.gen import R as R
from messenger import g_settings as g_settings

class LSTeamChannelController(TeamChannelController):
    _BASE_RELATED_COMMANDS_NAME: tuple
    def _formatCommand(self, command):
        ...
