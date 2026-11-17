# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/cgf_components/sequence_components.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import CGF as CGF
from cgf_script.registration import ComponentProperty as ComponentProperty, registerComponent as registerComponent
from typing import TYPE_CHECKING as TYPE_CHECKING
from typing import List as List

# decorador original: @registerComponent
class OnDisappearPrefabSpawnComponent(object):
    category = 'Sequence'
    editorTitle = 'On Disappear Prefab Spawner'
    domain = CGF.Domain.ClientEditor
    prefab: Any

# decorador original: @registerComponent
class OnAppearPrefabSpawnComponent(object):
    category = 'Sequence'
    editorTitle = 'On Appear Prefab Spawner'
    domain = CGF.Domain.ClientEditor
    prefab: Any

# decorador original: @registerComponent
class SequenceSnapshotComponent(object):
    editorTitle = 'Sequence Snapshot'
    domain = CGF.Domain.Client

# decorador original: @registerComponent
class SequencePauseComponent(object):
    editorTitle = 'Sequence Pause'
    domain = CGF.Domain.Client

class PrefabSpawnerSystem(CGF.System):
    SpawnerActivated: Any
    SpawnerDeactivated: Any
    Reactions: Any
    def update(self):
        ...
    @staticmethod
    def _onLoaded(objects, queue):
        ...
