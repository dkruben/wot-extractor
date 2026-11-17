# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/battle_control/controllers/hit_direction_ctrl/hw_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.battle_control.controllers.hit_direction_ctrl.ctrl import HitDirectionController as HitDirectionController
from gui.battle_control.controllers.hit_direction_ctrl.hit_data import HitData as HitData
from gui.battle_control.controllers.hit_direction_ctrl.base import HitType as HitType
from halloween.gui.hw_vehicle_role_helper import getVehicleRole as getVehicleRole

class HWHitDirectionController(HitDirectionController):
    def addHit(self, hitDirYaw, attackerID, damage, isBlocked, critFlags, isHighExplosive, damagedID, attackReasonID):
        ...

class HWHitDirectionControllerPlayer(HWHitDirectionController):
    def stopControl(self):
        ...
