# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/cgf_components_common/vehicle_mechanics/custom_rotation_point.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import CGF as CGF
from cgf_script.registration import ComponentProperty as ComponentProperty, registerComponent as registerComponent

# decorador original: @registerComponent
class CustomRotationPointComponent(object):
    category = 'Vehicle Mechanics'
    editorTitle = 'Custom Rotation Point Component'
    domain = CGF.Domain.All
    minSpeed: Any
    minPoints: Any
    maxSpeed: Any
    maxPoints: Any
    changeRailDirection: Any
    physicsRef: Any
    originGimletCOMOffset: Any
    originRailCOMOffset: Any
    def __init__(self):
        ...
