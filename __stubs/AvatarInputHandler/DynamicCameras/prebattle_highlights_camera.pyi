# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/AvatarInputHandler/DynamicCameras/prebattle_highlights_camera.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import math as math
import logging as logging
from functools import partial as partial
import BigWorld as BigWorld
import CGF as CGF
from AvatarInputHandler.cameras import FovExtended as FovExtended
from CameraComponents import CameraComponent as CameraComponent, ActiveCameraComponent as ActiveCameraComponent, FovComponent as FovComponent, DofComponent as DofComponent
from GenericComponents import getGlobalTagStorage as getGlobalTagStorage
from cgf_modules.sequence_events import sequenceSubscribe as sequenceSubscribe
from constants import PREBATTLE_SEQUENCE_EVENT_NAMES as PREBATTLE_SEQUENCE_EVENT_NAMES
from gui.battle_control.avatar_getter import getSpaceID as getSpaceID
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from gui.battle_control.controllers.prebattle_highlights.pbh_constants import TANK_CAMERA_TEMPLATE as TANK_CAMERA_TEMPLATE
_logger: Any
PBH_CAMERA_EVENTS: tuple
INITIAL_CAMERA_INDEX = 0

class PrebattleHighlightsCamera(object):
    __sessionProvider: Any
    __cameraGo: Any
    __pbhSize: Any
    __customizationHelper: Any
    def __init__(self, _):
        ...
    @property
    def aimingSystem(self):
        ...
    def enable(self):
        ...
    def disable(self):
        ...
    def __getPBHCameraGo(self, size, index=0):
        ...
    def __subscribeOnSeqEvents(self):
        ...
    def __tryToChangeCamera(self, index):
        ...
    def __applyCameraSettings(self, go):
        ...
