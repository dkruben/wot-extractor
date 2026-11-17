# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/AvatarInputHandler/commands/mechanic_controls/auto_shoot_gun_control.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import Keys as Keys
from AvatarInputHandler.commands.input_handler_command import InputHandlerCommand as InputHandlerCommand
from gui.battle_control.controllers.auto_shoot_guns.auto_shoot_helpers import AUTO_SHOOT_DEV_KEYS as AUTO_SHOOT_DEV_KEYS, AutoShootDevCommand as AutoShootDevCommand
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider

class DevAutoShootGunControl(InputHandlerCommand):
    __sessionProvider: Any
    _KEY_TO_COMMAND_MAP: dict
    def handleKeyEvent(self, isDown, key, mods, event=None):
        ...
    def __handleDevKeyEvent(self, isDown, key):
        ...

def createAutoShootGunControl(*_, **__):
    ...
