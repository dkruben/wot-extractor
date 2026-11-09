# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/cgf_demo_client/test_gun_effects_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import CGF as CGF
import Triggers as Triggers
import Vehicular as Vehicular
from cgf_demo.demo_category import DEMO_CATEGORY as DEMO_CATEGORY
from cgf_script.registration import ComponentProperty as ComponentProperty, registerComponent as registerComponent
from cgf_events import gun_events as gun_events
from constants import UNKNOWN_GUN_INDEX as UNKNOWN_GUN_INDEX

# decorador original: @registerComponent
class TestEntranceSingleShot(object):
    category = DEMO_CATEGORY
    editorTitle = 'Test Entrance Single Shot'
    domain = CGF.Domain.Client
    trigger: Any
    gun: Any

class EntranceSingleShotSystem(CGF.System):
    EntranceActivated: Any
    TriggerAccess: Any
    EntranceAccess: Any
    Reactions: Any
    def update(self):
        ...
    def __onEnter(self, _, where):
        ...

# decorador original: @registerComponent
class TestEntranceContinuousBurst(object):
    category = DEMO_CATEGORY
    editorTitle = 'Test Entrance Continuous Burst'
    domain = CGF.Domain.Client
    trigger: Any
    gun: Any

class EntranceContinuousBurstSystem(CGF.System):
    EntranceActivated: Any
    TriggerAccess: Any
    EntranceAccess: Any
    Reactions: Any
    def update(self):
        ...
    def __onEnter(self, _, where):
        ...
    def __onExit(self, _, where):
        ...
