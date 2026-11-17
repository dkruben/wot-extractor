# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/AvatarInputHandler/commands/prebattle_highlights_control.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import CommandMapping as CommandMapping
import BattleReplay as BattleReplay
import Keys as Keys
import VOIP as VOIP
from AvatarInputHandler.commands.input_handler_command import InputHandlerCommand as InputHandlerCommand
from helpers import dependency as dependency
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as _CAPS
from gui.battle_control import event_dispatcher as gui_event_dispatcher, avatar_getter as avatar_getter
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider

class PrebattleHighlightsCommandsSetup(InputHandlerCommand):
    guiSessionProvider: Any
    def handleKeyEvent(self, isDown, key, mods, event=None):
        ...
