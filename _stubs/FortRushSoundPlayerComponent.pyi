# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/FortRushSoundPlayerComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from helpers.events_handler import EventsHandler as EventsHandler
from typing import Dict as Dict, Union as Union, Tuple as Tuple
from PlayerEvents import g_playerEvents as g_playerEvents
from constants import ARENA_PERIOD as ARENA_PERIOD, FINISH_REASON as FINISH_REASON
from fort_rush.gui.shared.events import CaptureInvaderEvent as CaptureInvaderEvent, CapturePointEvent as CapturePointEvent
from fort_rush.gui.sounds import play2DSound as play2DSound, get2DSound as get2DSound
from fort_rush.gui.sounds.sound_constants import CAPTURE_STATE_START_TO_SOUND as CAPTURE_STATE_START_TO_SOUND, CAPTURE_STATE_STOP_TO_SOUND as CAPTURE_STATE_STOP_TO_SOUND, CapturePointSounds as CapturePointSounds, RTPC_VALUE_THRESHOLD as RTPC_VALUE_THRESHOLD, SoundStates as SoundStates, WIN_POINTS_CAP_STINGER as WIN_POINTS_CAP_STINGER
from fort_rush_common.fort_rush_constants import CAPTURE_POINT_INVADER_COMPONENT as CAPTURE_POINT_INVADER_COMPONENT, CAPTURE_POINT_NO_TEAM as CAPTURE_POINT_NO_TEAM, CaptureStates as CaptureStates
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, EventPriority as EventPriority
from script_component.DynamicScriptComponent import DynamicScriptComponent as DynamicScriptComponent
_NORMALIZED_MAX_VALUE = 1.0

class FortRushSoundPlayerComponent(DynamicScriptComponent, EventsHandler):
    _pointStates: Any
    _pointInvadingTeams: Any
    _pointOwnerTeams: Any
    _sound: Any
    def __init__(self):
        ...
    def _onAvatarReady(self):
        ...
    def onDestroy(self):
        ...
    def _getEvents(self):
        ...
    def _getListeners(self):
        ...
    def _onCapturePointUpdate(self, event):
        ...
    def _setRTPCValue(self, event, resolvedState):
        ...
    def _onInvaderAdded(self, event):
        ...
    def _onInvaderRemoved(self, event):
        ...
    def _playCollectionSound(self, collection, state):
        ...
    def _handleDecreasingStateAsInvader(self, collection, baseName):
        ...
    def _onVehicleHealthChanged(self, vehicleID, newHealth, oldHealth):
        ...
    def _onArenaPeriodChange(self, period, _, __, periodAdditionalInfo):
        ...
