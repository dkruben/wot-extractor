# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/turret_gun_angles.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.ClientHangarSpace import hangarCFG as hangarCFG
from skeletons.gui.turret_gun_angles import ITurretAndGunAngles as ITurretAndGunAngles

class TurretAndGunAngles(ITurretAndGunAngles):
    __gunPitch: Any
    __turretYaw: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def reset(self):
        ...
    def destroy(self):
        ...
    def set(self, gunPitch=0.0, turretYaw=0.0):
        ...
    def getTurretYaw(self):
        ...
    def getGunPitch(self):
        ...
