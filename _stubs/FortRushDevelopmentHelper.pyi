# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/FortRushDevelopmentHelper.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import BigWorld as BigWorld
from script_component.DynamicScriptComponent import DynamicScriptComponent as DynamicScriptComponent
from debug_utils import LOG_WARNING as LOG_WARNING
from fort_rush_common.component_helpers import getInvaderComponent as getInvaderComponent
from fort_rush_common.fort_rush_constants import FORT_RUSH_DEVELOPMENT_HELPER as FORT_RUSH_DEVELOPMENT_HELPER
from gui.battle_control import avatar_getter as avatar_getter

class FortRushDevelopmentHelper(DynamicScriptComponent):
    def progressZone(self, zoneName):
        ...
    def progressCapturingZone(self):
        ...
    def captureZone(self, zoneName):
        ...
    def captureZoneEnemy(self, zoneName):
        ...
    def neutralizeZone(self, zoneName):
        ...
    def captureCurrentZone(self):
        ...
