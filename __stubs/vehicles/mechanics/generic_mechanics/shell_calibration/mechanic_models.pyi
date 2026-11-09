# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/mechanics/generic_mechanics/shell_calibration/mechanic_models.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.battle_control.components_states.ammo import DefaultComponentAmmoState as DefaultComponentAmmoState
from gui.battle_control.components_states.ammo.constants import ShellMode as ShellMode
from gui.battle_control.components_states.ammo.shells import DefaultAmmoMode as DefaultAmmoMode

class ShellCalibrationAmmoMode(DefaultAmmoMode):
    __calibrationShells: Any
    def __init__(self, calibrationShells):
        ...
    def getShellMode(self, shellIntCD):
        ...

class ShellCalibrationAmmoState(DefaultComponentAmmoState):
    __ammoMode: Any
    def __init__(self, calibrationShells):
        ...
    def getAmmoMode(self):
        ...
