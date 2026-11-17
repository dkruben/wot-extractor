# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/battle_control/controllers/hit_direction_ctrl/ls_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.battle_control.controllers.hit_direction_ctrl.ctrl import HitDirectionController as HitDirectionController
from gui.battle_control.controllers.hit_direction_ctrl.hit_data import HitData as HitData
from gui.battle_control.controllers.hit_direction_ctrl.base import HitType as HitType
from last_stand.gui.ls_vehicle_role_helper import getVehicleRole as getVehicleRole
from last_stand_common.last_stand_constants import LS_ROLE_PREFIX as LS_ROLE_PREFIX

class LSHitDirectionController(HitDirectionController):
    def addHit(self, hitDirYaw, attackerID, damage, isBlocked, critFlags, isHighExplosive, damagedID, attackReasonID):
        ...

class LSHitDirectionControllerPlayer(LSHitDirectionController):
    def stopControl(self):
        ...
