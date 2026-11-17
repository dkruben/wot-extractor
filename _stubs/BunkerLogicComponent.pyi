# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/BunkerLogicComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import CGF as CGF
from story_mode_common.cgf_components_common.bunkers import BunkerLogicComponentDescriptor as BunkerLogicComponentDescriptor
from constants import IS_CGF_DUMP as IS_CGF_DUMP, IS_EDITOR as IS_EDITOR
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from cgf_script.registration import registerReplicableComponent as registerReplicableComponent
from gui.battle_control.battle_constants import FEEDBACK_EVENT_ID as FEEDBACK_EVENT_ID, ENTITY_IN_FOCUS_TYPE as ENTITY_IN_FOCUS_TYPE

class DynamicScriptComponent(object):
    ...

# decorador original: @registerReplicableComponent
class BunkerLogicComponent(DynamicScriptComponent, BunkerLogicComponentDescriptor):
    sessionProvider: Any
    _spaceID: Any
    def __init__(self):
        ...
    def bunkerDestroyed(self):
        ...
    def startLogic(self, spaceID):
        ...
    def stopLogic(self):
        ...
    def _onVehicleFeedbackReceived(self, eventID, entityID, entityInFocusData):
        ...
    def highlightBunker(self, isInFocus):
        ...
    def _onBunkerDestroyed(self):
        ...
    def _activateGameObject(self, gameObjectID, queue):
        ...
