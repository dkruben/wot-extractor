# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/cgf_demo_client/test_physical_debris_spawner.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import functools as functools
import CGF as CGF
import Triggers as Triggers
import Physics as Physics
from cgf_demo.demo_category import DEMO_CATEGORY as DEMO_CATEGORY
from cgf_script.registration import ComponentProperty as ComponentProperty, registerComponent as registerComponent

# decorador original: @registerComponent
class TestEntranceSpawner(object):
    group = DEMO_CATEGORY
    editorTitle = 'Test Entrance Spawner'
    domain = CGF.Domain.Client
    trigger: Any
    debrisSpawner: Any

class EntranceSpawnerSystem(CGF.System):
    EntranceSpawnerActivated: Any
    AreaTriggerAccess: Any
    DebrisSpawnerAccess: Any
    Reactions: Any
    def update(self):
        ...
    def _onEntranceAdded(self, entrance, triggerAccess):
        ...
    def __onEnter(self, debrisSpawnerUuid, who, where):
        ...
    def __onExit(self, debrisSpawnerUuid, who, where):
        ...
