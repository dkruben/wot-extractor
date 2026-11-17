# wot-extractor: STUB (.pyi) gerado a partir de sources/res/event_platform/scripts/common/event_platform_common/respawns/respawn_components.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import CGF as CGF
from cgf_script.registration import registerComponent as registerComponent

# decorador original: @registerComponent
class RespawnBlockComponent(object):
    category = 'Respawns'
    editorTitle = 'RespawnBlockComponent'
    domain = CGF.Domain.All
    blockers: Any
    def __init__(self, initBlock):
        ...

# decorador original: @registerComponent
class PerformRespawnComponent(object):
    category = 'Respawns'
    editorTitle = 'PerformRespawnComponent'
    domain = CGF.Domain.All
