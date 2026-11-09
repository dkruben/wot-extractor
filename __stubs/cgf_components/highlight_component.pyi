# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/cgf_components/highlight_component.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import CGF as CGF
from cgf_script.registration import ComponentProperty as ComponentProperty, registerComponent as registerComponent
from GenericComponents import DynamicModelComponent as DynamicModelComponent
from cgf_components.hover_component import IsHoveredComponent as IsHoveredComponent, SelectionComponent as SelectionComponent

# decorador original: @registerComponent
class IsHighlighted(object):
    editorTitle = 'Is Highlighted'
    domain = CGF.Domain.ClientEditor

# decorador original: @registerComponent
class HighlightComponent(object):
    domain = CGF.Domain.ClientEditor
    editorTitle = 'Highlight'
    group = 'Common'
    color: Any
    groupName: Any
    drawerMode: Any
    colorIndex: Any
    overridenHighlightModel: Any
    callbackID: Any
    def __init__(self):
        ...

class HighlightSystem(CGF.System):
    HoverActivated: Any
    HoverDeactivated: Any
    DynamicModelHighlightActivated: Any
    DynamicModelHighlightDeactivated: Any
    HighlightComponentDeactivated: Any
    HighlightModelIterate: Any
    DynamicModelAccess: Any
    Reactions: Any
    def update(self):
        ...
    def onHoverAdded(self, selection, gameObject, queue):
        ...
    def onHoverRemoved(self, selection, gameObject, queue):
        ...
    def onDynamicModelHighlightAdded(self, highlightComponent, dynamicModelComponent, dynamicModelAccess, highlightModelIterate):
        ...
    def onDynamicModelHighlightRemoved(self, highlightComponent, dynamicModelComponent, dynamicModelAccess, highlightModelIterate):
        ...
    def onHighlightComponentRemoved(self, highlightComponent, dynamicModelComponent, dynamicModelAccess):
        ...
    def __edgeDetectDynamicModel(self, enable, highlightComponent, dynamicModelComponent, dynamicModelAccess):
        ...
    def __enableGroupDraw(self, enable, groupName, highlightModelIterate, dynamicModelAccess):
        ...
