# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/AvatarInputHandler/commands/vehicle_upgrade_control.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import CommandMapping as CommandMapping
from AvatarInputHandler.commands.input_handler_command import InputHandlerCommand as InputHandlerCommand
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from gui.battle_control import event_dispatcher as event_dispatcher

class VehicleUpdateControl(InputHandlerCommand):
    __guiSessionProvider: Any
    def handleKeyEvent(self, isDown, key, mods, event=None):
        ...

class VehicleUpgradePanelControl(InputHandlerCommand):
    __guiSessionProvider: Any
    def handleKeyEvent(self, isDown, key, mods, event=None):
        ...
