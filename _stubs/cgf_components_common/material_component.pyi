# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/cgf_components_common/material_component.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import CGF as CGF
from cgf_script.registration import ComponentProperty as ComponentProperty, registerComponent as registerComponent
from material_kinds import EFFECT_MATERIALS as EFFECT_MATERIALS

# decorador original: @registerComponent
class MaterialComponent(object):
    category = 'Material'
    editorTitle = 'Material'
    domain = CGF.Domain.All
    materials: dict
    kind: Any
