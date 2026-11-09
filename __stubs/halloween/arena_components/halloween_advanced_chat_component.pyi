# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/arena_components/halloween_advanced_chat_component.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import BigWorld as BigWorld
from arena_components.advanced_chat_component import AdvancedChatComponent as AdvancedChatComponent
from battleground.location_point_manager import g_locationPointManager as g_locationPointManager
from gui.battle_control import avatar_getter as avatar_getter
from chat_commands_consts import BATTLE_CHAT_COMMAND_NAMES as BATTLE_CHAT_COMMAND_NAMES, MarkerType as MarkerType
from halloween_common.halloween_constants import HalloweenMarkerComponentNames as HalloweenMarkerComponentNames
from messenger_common_chat2 import MESSENGER_ACTION_IDS as _ACTIONS

class HWAdvancedChatComponent(AdvancedChatComponent):
    def cleanupBCMarkers(self):
        ...
    def _getActionMarker(self, cmdID, cmdTargetID):
        ...
