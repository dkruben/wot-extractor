# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/cgf_components/hover_group_components.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import CGF as CGF
import SoundGroups as SoundGroups
from cgf_script.registration import ComponentProperty as ComponentProperty, registerComponent as registerComponent
from cgf_components.hover_component import IsHoveredComponent as IsHoveredComponent, HoverGroupTrackerComponent as HoverGroupTrackerComponent

# decorador original: @registerComponent
class HoverableComponent(object):
    domain = CGF.Domain.ClientEditor
    editorTitle = 'Hoverable'
    group = 'Common'
    groupTracker: Any

# decorador original: @registerComponent
class HoverSoundComponent(object):
    domain = CGF.Domain.ClientEditor
    editorTitle = 'Hover group sound'
    group = 'Common'
    hoverAddingSound: Any
    hoverRemovingSound: Any

class HoverGroupSystem(CGF.System):
    HoverableActivated: Any
    HoverableDeactivated: Any
    HoverSoundActivated: Any
    HoverSoundDeactivated: Any
    HoverGroupTrackerAccess: Any
    Reactions: Any
    def update(self):
        ...
    def onHoverAdded(self, hoverableComponent, gameObject, hoverGroupTrackerAccess):
        ...
    def onHoverRemoved(self, hoverableComponent, gameObject, hoverGroupTrackerAccess):
        ...
    def onHoverSoundAdded(self, hoverSound):
        ...
    def onHoverSoundRemoved(self, hoverSound):
        ...
