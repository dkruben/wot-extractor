# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/abilities/self_buff.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import CGF as CGF
from typing import List as List
from cgf_script.registration import ComponentProperty as ComponentProperty, registerComponent as registerComponent
from constants import IS_CLIENT as IS_CLIENT
from helpers import dependency as dependency
import GenericComponents as GenericComponents
from items import vehicles as vehicles
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from vehicle_systems.model_assembler import loadAppearancePrefab as loadAppearancePrefab
from battle_royale.abilities.common import getEffectSuffixForGunLength as getEffectSuffixForGunLength
_GUN_LENGTH_RANGES: dict

class VehicleSelfBuffComponent(object):
    ...

class UpgradeInProgressComponent(object):
    ...

# decorador original: @registerComponent
class SelfBuffComponent(object):
    editorTitle = 'Self Buff Component'
    group = 'Abilities'
    domain = CGF.Domain.Client
    gunNode: Any

# decorador original: @registerComponent
class SelfBuffNodeComponent(object):
    editorTitle = 'Self Buff Node Component'
    group = 'Abilities'
    domain = CGF.Domain.Client
    effectPathTemplate: Any

class SelfBuffSystem(CGF.System):
    __guiSessionProvider: Any
    VehicleSelfBuffActivated: Any
    UpgradeDeactivated: Any
    SelfBuffNodeAccess: Any
    Reactions: Any
    def update(self):
        ...
    def visualizeSelfBuff(self, vehicleSelfBuffComponent):
        ...
    def __launch(self, vehicleSelfBuffComponent):
        ...
    def __setupVFX(self, nodeGO, appearance, queue):
        ...
    def inBattleUpgradeCompleted(self, vehicleSelfBuffComponent):
        ...
