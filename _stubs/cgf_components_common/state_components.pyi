# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/cgf_components_common/state_components.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import CGF as CGF
from cgf_script.registration import ComponentProperty as ComponentProperty, registerComponent as registerComponent
from GenericComponents import StateSwitcherComponent as StateSwitcherComponent
_DEFAULT_HEALTH = 300

class DEATH_REASON(object):
    UNKNOWN = 0
    DESTROYED = 1

class DeathComponentDescriptor(object):
    category = 'Common'
    editorTitle = 'Death Component'

class HealthComponentDescriptor(object):
    category = 'Common'
    editorTitle = 'Health Component'
    maxHealth: Any
    health: Any

# decorador original: @registerComponent
class RemoveOnDeathComponent(object):
    category = 'Death'
    editorTitle = 'Remove On Death Component'
    domain = CGF.Domain.All
    delay: Any

# decorador original: @registerComponent
class SpawnOnDeathComponent(object):
    category = 'Death'
    editorTitle = 'Spawn On Death Component'
    domain = CGF.Domain.All
    prefabPath: Any
    delay: Any
    attachToGO: Any

# decorador original: @registerComponent
class VehicleHealthObserverComponent(object):
    category = 'Common'
    editorTitle = 'Vehicle Health Observer Component'
    domain = CGF.Domain.All
    state: Any
