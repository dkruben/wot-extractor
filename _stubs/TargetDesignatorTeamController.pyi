# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/TargetDesignatorTeamController.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from Math import Vector3 as Vector3
from chat_commands_consts import LocationMarkerSubType as LocationMarkerSubType
from helpers import dependency as dependency
from script_component.DynamicScriptComponent import DynamicScriptComponent as DynamicScriptComponent
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from typing import Set as Set, Optional as Optional, Tuple as Tuple
from gui.battle_control.controllers.feedback_adaptor import BattleFeedbackAdaptor as BattleFeedbackAdaptor
ClientMarkers: Any
_debug: Any
_UNSPOTTED_MARKER_HIT = LocationMarkerSubType.TARGET_DESIGNATOR_UNSPOTTED_MARKER_HIT

class TargetDesignatorTeamController(DynamicScriptComponent):
    session: Any
    __markers: Any
    def __init__(self):
        ...
    def onDestroy(self):
        ...
    def set_unspottedMarkers(self, oldMarkers):
        ...
    def __updateMarkers(self, oldMarkers, newMarkers):
        ...
