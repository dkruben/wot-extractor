# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/cgf_demo/test_edge_drawer.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import CGF as CGF
import Triggers as Triggers
from cgf_demo.demo_category import DEMO_CATEGORY as DEMO_CATEGORY
from cgf_script.registration import registerComponent as registerComponent
from EdgeDrawer import EdgeHighlightComponent as EdgeHighlightComponent

class _Stage(object):
    Empty = 0
    Ally = 1
    Enemy = 2

# decorador original: @registerComponent
class TestEdgeDrawerComponent(object):
    group = DEMO_CATEGORY
    editorTitle = 'Test Edge Drawer'
    domain = CGF.Domain.ClientEditor
    callbackID: Any
    def __init__(self):
        ...

class TestEdgeDrawerComponentSystem(CGF.System):
    _ALLY_COLOR = 2
    _ENEMY_COLOR = 1
    EdgeDrawerActivated: Any
    EdgeDrawerDeactivated: Any
    EdgeHighlightAccess: Any
    Reactions: Any
    def update(self):
        ...
    def __triggerReaction(self, gameObject):
        ...
    def __switchStage(self, prevStage, gameObject):
        ...
