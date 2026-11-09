# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/Scaleform/daapi/view/battle/shared/messages/player_messages.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from gui.Scaleform.daapi.view.battle.shared.messages import player_messages as player_messages
from items import vehicles as vehicles
_logger: Any

class SHPlayerMessages(player_messages.PlayerMessages):
    def _onShowPlayerMessageByCode(self, code, postfix, targetID, attackerID, equipmentID, ignoreMessages):
        ...
    def _getFullName(self, vehicleID):
        ...
    def __isVehicleBot(self, vehicleID):
        ...
