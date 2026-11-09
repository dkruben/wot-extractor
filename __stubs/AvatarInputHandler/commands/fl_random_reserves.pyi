# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/AvatarInputHandler/commands/fl_random_reserves.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import CommandMapping as CommandMapping
from AvatarInputHandler.commands.input_handler_command import InputHandlerCommand as InputHandlerCommand
from ReservesEvents import randomReservesEvents as randomReservesEvents
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider

class FLRandomReserves(InputHandlerCommand):
    __guiSessionProvider: Any
    __FIRST_RESERVE_INDEX = 0
    __SECOND_RESERVE_INDEX = 1
    def handleKeyEvent(self, isDown, key, mods, event=None):
        ...
