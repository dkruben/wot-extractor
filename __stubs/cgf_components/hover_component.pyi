# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/cgf_components/hover_component.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import CGF as CGF
import GUI as GUI
import Event as Event
from GenericComponents import VSEComponent as VSEComponent
from Physics import CameraCollideComponent as CameraCollideComponent
from cgf_script.registration import ComponentProperty as ComponentProperty, registerComponent as registerComponent
from constants import IS_CLIENT as IS_CLIENT, CollisionFlags as CollisionFlags
from vehicle_systems.tankStructure import ColliderTypes as ColliderTypes
from helpers import dependency as dependency
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
from AvatarInputHandler import cameras as cameras

# decorador original: @registerComponent
class SelectionComponent(object):
    group = 'Common'
    editorTitle = 'Selection'
    domain = CGF.Domain.ClientEditor
    highlight: Any
    onClickAction: Any
    def __init__(self):
        ...

# decorador original: @registerComponent
class IsHoveredComponent(object):
    editorTitle = 'Is Hovered'
    domain = CGF.Domain.Client

# decorador original: @registerComponent
class HoverGroupTrackerComponent(object):
    group = 'Common'
    editorTitle = 'Hover group tracker'
    domain = CGF.Domain.ClientEditor
    __hoveredGOs: Any
    def __init__(self):
        ...
    def addHoveredGO(self, gameObject):
        ...
    def removeHoveredGO(self, gameObject):
        ...

class HoverSystem(CGF.System):
    _hangarSpace: Any
    HoveredActivated: Any
    HoveredDeactivated: Any
    SelectionDeactivated: Any
    HoverIterate: Any
    HoverAccess: Any
    SelectionAccess: Any
    CameraCollideAccess: Any
    Reactions: Any
    _MAX_PICK_RAY_LEN = 1500.0
    __lastCursorPos: Any
    __lastCursorActive: Any
    def __init__(self):
        ...
    def update(self):
        ...
    def onIsHoveredAdded(self, vseComponent):
        ...
    def onIsHoveredRemoved(self, vseComponent):
        ...
    def onIsSelectableRemoved(self, gameObject, hoverAccess, queue):
        ...
    def tick(self, queue, hoverAccess, hoverStateChanged):
        ...
    def __getGameObjectUnderCursor(self):
        ...
