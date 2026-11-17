# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/cgf_components_common/vehicle_mechanics/stationary_reload_sequence_params_component.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import CGF as CGF
from cgf_script.registration import ComponentProperty as ComponentProperty, registerComponent as registerComponent

# decorador original: @registerComponent
class StationaryReloadSequenceParamsComponent(object):
    category = 'Sequence'
    editorTitle = 'Stationary reload sequence params'
    domain = CGF.Domain.All
    sequencePreparingLayer: Any
    sequenceFinishingLayer: Any
