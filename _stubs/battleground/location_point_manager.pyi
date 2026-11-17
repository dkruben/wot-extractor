# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/battleground/location_point_manager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from builtins import range as range
from collections import namedtuple as namedtuple
from future.utils import viewitems as viewitems, viewvalues as viewvalues
import BigWorld as BigWorld
import Math as Math
import ResMgr as ResMgr
from avatar_components.CombatEquipmentManager import CombatEquipmentManager as CombatEquipmentManager
from chat_commands_consts import BATTLE_CHAT_COMMAND_NAMES as BATTLE_CHAT_COMMAND_NAMES, MarkerType as MarkerType, LocationMarkerSubType as LocationMarkerSubType, _DEFAULT_ACTIVE_COMMAND_TIME as _DEFAULT_ACTIVE_COMMAND_TIME
from gui.battle_control import avatar_getter as avatar_getter
from helpers import dependency as dependency
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from messenger_common_chat2 import MESSENGER_ACTION_IDS as _ACTIONS
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from vehicle_systems.stricted_loading import makeCallbackWeak as makeCallbackWeak
_logger: Any
_EquipmentAdapter: Any
_DYNAMIC_OBJECTS_CONFIG_FILE = 'scripts/dynamic_objects.xml'
_AREA_VISUAL_SECTION: dict
_DIR_UP: Any
_STUN_AREA_DEFAULTS: dict
_CHECK_DISTANCE_CALLBACK_TIME = 1.5
_DISTANCE_FOR_MARKER_REMOVAL = 15.0
COMMAND_NAME_TO_LOCATION_MARKER_SUBTYPE: dict
g_locationPointManager: Any

class LocationPointData(object):
    creatorID: Any
    position: Any
    targetID: Any
    commandID: Any
    replyCount: Any
    markerText: Any
    markerSubType: Any
    areas: Any
    def __init__(self, creatorID, position, targetID, commandID, replyCount, markerText, markerSubType):
        ...

class LocationPointManager(CallbackDelayer):
    sessionProvider: Any
    __markedAreas: Any
    __activeLocationMarkerID: Any
    __resources: Any
    __visualisationData: Any
    def __init__(self):
        ...
    def activate(self):
        ...
    def deactivate(self):
        ...
    def loadPrerequisites(self):
        ...
    def addLocationPoint(self, position, targetID, creatorID, cmdID=None, activeTime=..., markerText='', numberOfReplies=0, isTargetForPlayer=False):
        ...
    def getLocationPointData(self, targetID):
        ...
    def setGUIVisible(self, visible):
        ...
    def getRepliablePoints(self, currPlayerID):
        ...
    def __onPrereqsLoaded(self, resourceRefs):
        ...
    def __removeMarkedArea(self, targetID):
        ...
    def __onReplyFeedbackReceived(self, targetID, replierID, markerType, oldReplyCount, newReplyCount):
        ...
    def __checkDistanceForRepliersCB(self):
        ...
    def __onRemoveCommandReceived(self, removeID, markerType):
        ...
    def __addVisualisationArea(self, targetID, position, visualisationParams, showArea=True):
        ...
    def __createArea(self, position, visualisationParams, areaIndex):
        ...
    @staticmethod
    def __getAreaParamsConfig(section):
        ...
    @property
    def markedAreas(self):
        ...
