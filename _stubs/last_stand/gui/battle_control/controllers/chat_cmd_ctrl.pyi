# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/battle_control/controllers/chat_cmd_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import CommandMapping as CommandMapping
from gui.battle_control.controllers.chat_cmd_ctrl import ChatCommandsController as ChatCommandsController
from helpers import dependency as dependency
from last_stand.skeletons.ls_controller import ILSController as ILSController
from last_stand_common.last_stand_constants import LS_BATTLE_CHAT_COMMANDS as LS_BATTLE_CHAT_COMMANDS

class LSChatCommandsController(ChatCommandsController):
    _lsCtrl: Any
    def handleContexChatCommand(self, key):
        ...
