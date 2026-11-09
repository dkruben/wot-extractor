# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/cgf_components/soul_collector_components.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import CGF as CGF
import GenericComponents as GenericComponents
from cgf_script.registration import ComponentProperty as ComponentProperty, registerComponent as registerComponent

# decorador original: @registerComponent
class SoulCollectorProgressComponent(object):
    category = 'Halloween'
    editorTitle = 'Soul Collector Progress Component'
    progressSectors: Any
    sectorOffsetY: Any
    progressSequence: Any

# decorador original: @registerComponent
class SoulCollectorComponent(object):
    category = 'Halloween'
    editorTitle = 'SoulCollectorComponent'
    loadProgressGO: Any
    energyGlowAnimator: Any
    auraAnimator: Any
    drainerAnimator: Any
