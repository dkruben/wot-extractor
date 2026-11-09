# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/cgf_components_common/cgf_common_module.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import CGF as CGF
from cgf_components_common.managers.state_managers import StateSwitcherSystem as StateSwitcherSystem
from cgf_components_common.vehicle_components import VehicleDestroyingComponent as VehicleDestroyingComponent, VehicleDamageLoggerComponent as VehicleDamageLoggerComponent, VehicleSequenceParamsAttachedComponent as VehicleSequenceParamsAttachedComponent
from cgf_components_common.material_component import MaterialComponent as MaterialComponent
from cgf_components_common.state_components import RemoveOnDeathComponent as RemoveOnDeathComponent, SpawnOnDeathComponent as SpawnOnDeathComponent, VehicleHealthObserverComponent as VehicleHealthObserverComponent
from cgf_components_common.vehicle_mechanics import StationaryReloadSequenceParamsComponent as StationaryReloadSequenceParamsComponent, CrestMovingSequenceParamsComponent as CrestMovingSequenceParamsComponent
from cgf_script.registration import registerModule as registerModule

# decorador original: @registerModule
class CommonScriptsModule(object):
    name = 'Common Module'
    desc = 'Client Server Common Components'
    group = 'Common'
    systems: list
    components: list
