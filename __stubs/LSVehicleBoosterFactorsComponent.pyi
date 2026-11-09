# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/LSVehicleBoosterFactorsComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from helpers import dependency as dependency
from last_stand.gui.ls_gui_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from last_stand_common.ls_utils.boosters import applyBoosterFactors as applyBoosterFactors, getFactorsDiff as getFactorsDiff
from script_component.DynamicScriptComponent import DynamicScriptComponent as DynamicScriptComponent
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider

class LSVehicleBoosterFactorsComponent(DynamicScriptComponent):
    guiSessionProvider: Any
    @property
    def lsBattleGuiCtrl(self):
        ...
    def set_factors(self, prev):
        ...
    def applyFactors(self, value, factorName):
        ...
    def _onAvatarReady(self):
        ...
