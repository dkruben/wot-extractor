# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/cgf_components/show_event_component.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import CGF as CGF
from cgf_components.hover_component import SelectionComponent as SelectionComponent
from cgf_script.registration import registerComponent as registerComponent
from GenericComponents import DynamicModelComponent as DynamicModelComponent
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from helpers import dependency as dependency
from skeletons.gui.game_control import IHangarLoadingController as IHangarLoadingController
from last_stand.skeletons.ls_controller import ILSController as ILSController
from last_stand.skeletons.ls_sound_controller import ILSSoundController as ILSSoundController

# decorador original: @registerComponent
class LSShowEventComponent(object):
    domain = CGF.Domain.Client
    editorTitle = 'LS Show Event Component'
    group = 'Last Stand'
    lsCtrl: Any
    lsSoundCtrl: Any
    def showEvent(self):
        ...

# decorador original: @registerComponent
class LSShowEventRewardComponent(object):
    domain = CGF.Domain.Client
    editorTitle = 'LS Show Event Reward Component'
    group = 'Last Stand'

class LSShowEventSystem(CGF.System, IGlobalListener):
    lsCtrl: Any
    hangarLoadingController: Any
    ShowEventModelsActivated: Any
    ShowEventActivated: Any
    ShowEventRewardActivated: Any
    SelectionActivated: Any
    SelectionDeactivated: Any
    ShowEventIterate: Any
    SelectionAccess: Any
    Reactions: Any
    _is3dPointVisible: Any
    _is3dPointRewardVisible: Any
    _allGOs: Any
    _rewardGoIDs: Any
    def __init__(self):
        ...
    def update(self):
        ...
    def onShowEventAdded(self, go, q, selectionAccess):
        ...
    def onSelectionAdded(self, showEventComponent, selectionComponent):
        ...
    def onAddedRewardComponent(self, go):
        ...
    def onSelectionRemoved(self, showEventComponent, selectionComponent):
        ...
    def onMappingLoaded(self):
        ...
    def onMappingUnloaded(self):
        ...
    def onPrbEntitySwitched(self):
        ...
    def _updateGameObjectComponent(self, eventGameObject, queue, selectionAccess):
        ...
    def _onSettingsUpdate(self):
        ...
    def _updateVisibility(self):
        ...
