# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/cgf_demo_client/demo_module.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import CGF as CGF
from cgf_demo.demo_category import DEMO_CATEGORY as DEMO_CATEGORY
from cgf_demo_client.test_gun_effects_controller import EntranceSingleShotSystem as EntranceSingleShotSystem, EntranceContinuousBurstSystem as EntranceContinuousBurstSystem
from cgf_script.registration import registerModule as registerModule
from cgf_demo_client.test_hierarchy_modificator import HierarchyModifier as HierarchyModifier, HierarchyModifier2 as HierarchyModifier2, ModelSwapperSystem as ModelSwapperSystem, TestHierarchyModifierSystem as TestHierarchyModifierSystem, TestMaterialManipulatorSystem as TestMaterialManipulatorSystem, TestMaterialParamManipulator as TestMaterialParamManipulator, TestModelSwapper as TestModelSwapper
from cgf_demo_client.test_state_machine_trigger import StateMachineActivatorSystem as StateMachineActivatorSystem, TestStateMachineStatesActivator as TestStateMachineStatesActivator
from cgf_demo_client.test_triggers import EntranceModifierSystem as EntranceModifierSystem, ShowHealthInfoComponent as ShowHealthInfoComponent, TestEntranceNotifier as TestEntranceNotifier, TestHealthMonitoringSystem as TestHealthMonitoringSystem
from cgf_demo_client.test_physical_debris_spawner import EntranceSpawnerSystem as EntranceSpawnerSystem, TestEntranceSpawner as TestEntranceSpawner
from cgf_demo_client.test_death_triggers import TestAddDeathByTrigger as TestAddDeathByTrigger, TestDeathByTriggerSystem as TestDeathByTriggerSystem, TestRemoveDeathByTrigger as TestRemoveDeathByTrigger
from cgf_demo_client.test_client_component import ClientTestSystem as ClientTestSystem, ClientTestComponent as ClientTestComponent
from constants import IS_CLIENT as IS_CLIENT

class DisplayReplicableValuesSystem(object):
    Reactions: Any

# decorador original: @registerModule
class TestClientDemoModule(object):
    name = 'Test Client Demo Module'
    group = DEMO_CATEGORY
    systems: list
    components: list
