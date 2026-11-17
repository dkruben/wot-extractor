# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_core/scripts/client/comp7_core/gui/Scaleform/daapi/view/battle/messages/player_messages.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from comp7_core_constants import ROLE_EQUIPMENT_TAG as ROLE_EQUIPMENT_TAG
from constants import EQUIPMENT_STAGES as EQUIPMENT_STAGES
from gui.Scaleform.daapi.view.battle.shared.messages import PlayerMessages as PlayerMessages
from points_of_interest_shared import ENEMY_VEHICLE_ID as ENEMY_VEHICLE_ID
from comp7_core.gui.battle_control.controllers.consumables.comp7_equipment_ctrl import Comp7EquipmentController as Comp7EquipmentController
_ROLE_EQUIPMENT_READY = 'ROLE_EQUIPMENT_READY'
_POI_EQUIPMENT_USED = 'POI_EQUIPMENT_USED'
_POI_EQUIPMENT_USED_BY_ENEMY = 'POI_EQUIPMENT_USED_BY_ENEMY'
_POI_EQUIPMENT_USED_BY_ALLY = 'POI_EQUIPMENT_USED_BY_ALLY'
_ROLE_EQUIPMENT_APPLIED = 'ROLE_EQUIPMENT_APPLIED'
_ROLE_EQUIPMENT_PROMOTED = 'ROLE_EQUIPMENT_PROMOTED'

class Comp7CorePlayerMessages(PlayerMessages):
    @property
    def _modeController(self):
        ...
    def _addGameListeners(self):
        ...
    def _removeGameListeners(self):
        ...
    def __onEquipmentUpdated(self, _, item):
        ...
    def __onPoiEquipmentUsed(self, equipment, vehicleID):
        ...
    def __onRoleEquipmentStateChanged(self, state, previousState=None):
        ...
