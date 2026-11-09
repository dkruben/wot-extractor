# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/EntityMarkerComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from future.utils import viewvalues as viewvalues
from chat_commands_consts import MarkerType as MarkerType, INVALID_TARGET_ID as INVALID_TARGET_ID
from script_component.DynamicScriptComponent import DynamicScriptComponent as DynamicScriptComponent
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from gui.battle_control.controllers.area_marker_ctrl import AreaMarkersController as AreaMarkersController

class EntityMarkerComponent(DynamicScriptComponent):
    sessionProvider: Any
    _isReconnect: Any
    markerID: Any
    def __init__(self):
        ...
    def set_visible(self, oldValue):
        ...
    def onDestroy(self):
        ...
    def _onAvatarReady(self):
        ...
    def __createMarker(self, isReconnect=False):
        ...
    def __clearBattleCommunication(self):
        ...
    def __removeMarker(self):
        ...
