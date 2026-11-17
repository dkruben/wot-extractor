# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/messages/player_messages.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from typing import TYPE_CHECKING as TYPE_CHECKING
from constants import EQUIPMENT_STAGES as EQUIPMENT_STAGES, ARENA_GUI_TYPE as ARENA_GUI_TYPE
from battle_royale.gui.constants import BR_EQUIPMENTS_WITH_MESSAGES as BR_EQUIPMENTS_WITH_MESSAGES
from gui.Scaleform.daapi.view.battle.shared.messages import fading_messages as fading_messages
from items import vehicles as vehicles
from items.artefacts import Equipment as Equipment
_logger: Any

class PlayerMessages(fading_messages.FadingMessages):
    def __init__(self):
        ...
    def __del__(self):
        ...
    def _addGameListeners(self):
        ...
    def _removeGameListeners(self):
        ...
    def __onShowDestructibleEntityMessageByCode(self, code, entityID, attackerID):
        ...
    def _onShowPlayerMessageByCode(self, code, postfix, targetID, attackerID, equipmentID, ignoreMessages):
        ...
    def __onShowPlayerMessageByKey(self, key, args=None, extra=None):
        ...
    def __onCombatEquipmentUpdated(self, _, item):
        ...
    def _onCombatEquipmentUsed(self, shooterID, eqID):
        ...
    @staticmethod
    def _getPostfixFromEquipment(equipment):
        ...
