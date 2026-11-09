# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/cgf_components_common/vehicle_components.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import CGF as CGF
import Triggers as Triggers
from cgf_script.registration import ComponentProperty as ComponentProperty, registerComponent as registerComponent

# decorador original: @registerComponent
class VehicleDestroyingComponent(object):
    category = 'Vehicle'
    editorTitle = 'Vehicle Destroying Component'
    domain = CGF.Domain.ServerEditor
    trigger: Any
    reactionID: Any
    def __init__(self):
        ...

# decorador original: @registerComponent
class VehicleDamageLoggerComponent(object):
    category = 'Loggers'
    editorTitle = 'Vehicle Damage Logger Component'
    domain = CGF.Domain.ServerEditor
    topMostParentName: Any
    def __init__(self):
        ...

# decorador original: @registerComponent
class VehicleSequenceParamsAttachedComponent(object):
    category = 'Vehicle'
    editorTitle = 'Vehicle Sequence Params Attached Component'
    domain = CGF.Domain.All
