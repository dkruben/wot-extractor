# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/cgf_components/show_event_component.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import CGF as CGF
from cgf_components.hover_component import SelectionComponent as SelectionComponent
from cgf_script.registration import registerComponent as registerComponent, registerModule as registerModule
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from halloween.skeletons.halloween_controller import IHalloweenController as IHalloweenController
from halloween.skeletons.halloween_sound_controller import IHalloweenSoundController as IHalloweenSoundController
from halloween.uilogging.logging_constants import HWLogKeys as HWLogKeys
from helpers import dependency as dependency

# decorador original: @registerComponent
class HWShowEventComponent(object):
    domain = CGF.Domain.Client
    editorTitle = 'HW Show Event Component'
    group = 'Halloween'
    halloweenCtrl: Any
    hwSoundCtrl: Any
    def showEvent(self):
        ...

class HWShowEventSystem(CGF.System, IGlobalListener):
    halloweenCtrl: Any
    ShowEventActivated: Any
    SelectionActivated: Any
    ShowEventDeactivated: Any
    SelectionDeactivated: Any
    ShowEventIterate: Any
    SelectionAccess: Any
    Reactions: Any
    def update(self):
        ...
    def onShowEventAdded(self, gameObject, queue, selectionAccess):
        ...
    def onShowEventRemoved(self, showEventIterate):
        ...
    def onSelectionAdded(self, showEventComponent, selectionComponent):
        ...
    def onSelectionRemoved(self, showEventComponent, selectionComponent):
        ...
    def onPrbEntitySwitched(self):
        ...
    def _updateGameObjectComponent(self, eventGameObject, queue, selectionAccess):
        ...

# decorador original: @registerModule
class HWShowEventModule(object):
    domain = CGF.Domain.Client
    editorTitle = 'HW Show Event Module'
    group = 'Halloween'
    systems: list
    components: list
