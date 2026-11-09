# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/arena_components/ls_advanced_chat_component.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from functools import partial as partial
import BigWorld as BigWorld
from future.utils import viewitems as viewitems
from arena_components.advanced_chat_component import AdvancedChatComponent as AdvancedChatComponent, EMPTY_CHAT_CMD_FLAG as EMPTY_CHAT_CMD_FLAG, ChatCommandChange as ChatCommandChange, EMPTY_STATE as EMPTY_STATE
from battleground.location_point_manager import g_locationPointManager as g_locationPointManager
from gui.battle_control import avatar_getter as avatar_getter
from chat_commands_consts import BATTLE_CHAT_COMMAND_NAMES as BATTLE_CHAT_COMMAND_NAMES, MarkerType as MarkerType
from helpers import dependency as dependency
from last_stand.gui.ls_gui_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from last_stand_common.last_stand_constants import LSMarkerComponentNames as LSMarkerComponentNames, LS_BATTLE_CHAT_COMMANDS as LS_BATTLE_CHAT_COMMANDS, LS_OBELISK_ACTIVE_TIME as LS_OBELISK_ACTIVE_TIME
from messenger_common_chat2 import MESSENGER_ACTION_IDS as _ACTIONS
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
_actionMarkerByComponents: dict

class LSAdvancedChatComponent(AdvancedChatComponent):
    guiSessionProvider: Any
    _obeliskCommandCallbacks: Any
    def __init__(self, componentSystem):
        ...
    @property
    def lsBattleGuiCtrl(self):
        ...
    def _removeEventListenersAndClear(self):
        ...
    def cleanup(self):
        ...
    def _getActionMarker(self, cmdID, cmdTargetID):
        ...
    def _handleRegularCommand(self, cmd):
        ...
    def _chatCommandsUpdated(self, cmdMarkerType, cmdTargetID, cmdID, senderVehID, typeOfUpdate):
        ...
    def _cleanObeliskCommandVehicle(self, senderID):
        ...
    def _cleanObeliskCommands(self):
        ...
