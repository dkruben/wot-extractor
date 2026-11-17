# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/cgf/show_event_component.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import CGF as CGF
from cgf_components.hover_component import SelectionComponent as SelectionComponent
from cgf_script.registration import registerComponent as registerComponent, registerModule as registerModule
from fort_rush.gui.sounds import play2DSound as play2DSound
from fort_rush.gui.sounds.sound_constants import HangarSounds as HangarSounds
from fort_rush.skeletons.battle_controller import IFortRushBattleController as IFortRushBattleController
from fort_rush_common.configs.fort_rush_battles_config import fortRushBattlesConfigGameParamsSchema as fortRushBattlesConfigGameParamsSchema
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from helpers import dependency as dependency
from PlayerEvents import g_playerEvents as g_playerEvents

# decorador original: @registerComponent
class FortRushShowEventComponent(object):
    domain = CGF.Domain.Client
    editorTitle = 'Fort Rush Show Event Component'
    group = 'Fort Rush'
    _fortRushCtrl: Any
    def showEvent(self):
        ...

class FortRushShowEventSystem(CGF.System, IGlobalListener):
    _fortRushCtrl: Any
    ShowEventActivated: Any
    SelectionActivated: Any
    SelectionDeactivated: Any
    ShowEventIterate: Any
    SelectionAccess: Any
    Reactions: Any
    _allGOs: Any
    def __init__(self):
        ...
    def update(self):
        ...
    def onMappingLoaded(self):
        ...
    def onMappingUnloaded(self):
        ...
    def onShowEventAdded(self, gameObject, queue, selectionAccess):
        ...
    def onSelectionAdded(self, showEventComponent, selectionComponent):
        ...
    def onSelectionRemoved(self, showEventComponent, selectionComponent):
        ...
    def onPrbEntitySwitched(self):
        ...
    def __onConfigModelUpdated(self, gpKey):
        ...
    def _updateVisibility(self):
        ...
    def _updateGameObjectComponent(self, eventGameObject, queue, selectionAccess):
        ...

# decorador original: @registerModule
class FortRushShowEventModule(object):
    domain = CGF.Domain.Client
    editorTitle = 'Fort Rush Show Event Module'
    group = 'Fort Rush Hangar'
    systems: list
    components: list
