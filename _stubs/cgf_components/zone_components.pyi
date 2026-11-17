# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/cgf_components/zone_components.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import functools as functools
import logging as logging
import BigWorld as BigWorld
import CGF as CGF
import Triggers as Triggers
import UIComponents as UIComponents
from cgf_script.registration import ComponentProperty as CompProp, registerComponent as registerComponent
from constants import IS_CLIENT as IS_CLIENT, IS_CGF_DUMP as IS_CGF_DUMP, IS_EDITOR as IS_EDITOR
from helpers import dependency as dependency
from hints.battle import manager as battleHintsModelsMgr
from PlayerEvents import g_playerEvents as g_playerEvents
from helpers import isPlayerAvatar as isPlayerAvatar
from GenericComponents import TimedActivatedComponent as TimedActivatedComponent
from typing import TYPE_CHECKING as TYPE_CHECKING
from typing import Optional as Optional
avatar_getter = None
_logger: Any

class IBattleSessionProvider(object):
    ...

class Vehicle(object):
    ...

class RandomEventZoneUINotificationType(object):
    DANGER_ZONE = 'dangerZone'
    WARNING_ZONE = 'warningZone'
    MAP_DEATH_ZONE = 'mapDeathZone'

class WeatherZoneUINotificationType(object):
    BLIZZARD_ZONE = 'blizzardZone'
    FIRE_ZONE = 'fireZone'
    FOG_ZONE = 'fogZone'
    RAIN_ZONE = 'rainZone'
    SANDSTORM_ZONE = 'sandstormZone'
    SMOKE_ZONE = 'smokeZone'
    TORNADO_ZONE = 'tornadoZone'

# decorador original: @registerComponent
class ZoneMarker(object):
    category = 'UI'
    editorTitle = 'Zone Marker'
    domain = CGF.Domain.ClientEditor
    isVisibleOnMinimap: Any
    isVisibleOn3DScene: Any
    reduceDuration: Any
    id: Any
    startTime: Any
    finishTime: Any
    def __init__(self):
        ...
    @property
    def duration(self):
        ...
    @property
    def markerProgress(self):
        ...
    def isActive(self):
        ...

# decorador original: @registerComponent
class WeatherZoneUINotification(object):
    category = 'UI'
    editorTitle = 'Zone with weather UI Notification'
    domain = CGF.Domain.ClientEditor
    trigger: Any
    zoneType: Any
    id: Any
    enterReactionID: Any
    exitReactionID: Any
    inZoneVehicles: Any
    def __init__(self):
        ...

# decorador original: @registerComponent
class ZoneHint(object):
    category = 'UI'
    editorTitle = 'Zone hint'
    domain = CGF.Domain.ClientEditor
    trigger: Any
    hintUniqName: Any
    id: Any
    enterReactionID: Any
    exitReactionID: Any
    inZoneVehicles: Any
    def __init__(self):
        ...

# decorador original: @registerComponent
class RandomEventZoneUINotification(object):
    category = 'UI'
    editorTitle = 'Zone with timer UI Notification'
    domain = CGF.Domain.ClientEditor
    trigger: Any
    zoneType: Any
    id: Any
    startTime: Any
    finishTime: Any
    enterReactionID: Any
    exitReactionID: Any
    inZoneVehicles: Any
    def __init__(self):
        ...
    def isActive(self):
        ...

class MapZoneSystem(CGF.System):
    __guiSessionProvider: Any
    RandomEventUINotificationsActivated: Any
    RandomEventUINotificationsDeactivated: Any
    RandomEventUINotificationsIterate: Any
    RandomEventUIAndTimerActivated: Any
    RandomEventUINotificationsAccess: Any
    WeatherUINotificationsActivated: Any
    WeatherUINotificationsDeactivated: Any
    WeatherUINotificationsIterate: Any
    WeatherUINotificationsAccess: Any
    ZoneHintsIterate: Any
    ZoneHintsActivated: Any
    ZoneHintsDeactivated: Any
    ZoneHintsAccess: Any
    ZoneMarkerActivated: Any
    ZoneMarkerDeactivated: Any
    ZoneMarkerIterate: Any
    ZoneMarkerAndTimerActivated: Any
    ZoneMarkerAccess: Any
    MinimapChangerActivated: Any
    MinimapChangerDeactivated: Any
    MinimapChangerAccess: Any
    VehicleAccess: Any
    AreaTriggerAccess: Any
    Reactions: Any
    __subscriptionsCount: Any
    def __init__(self):
        ...
    def onMappingLoaded(self):
        ...
    def onMappingUnloaded(self):
        ...
    def commonUpdate(self):
        ...
    def periodUpdate(self):
        ...
    def __subscribeTrigger(self, go, zone, zoneAccessType, triggerAccess, enterCallback, exitCallback):
        ...
    def __unsubscribeTrigger(self, zone, triggerAccess):
        ...
    def __onEnterZone(self, go, enterCallback, zoneAccessType, who, _):
        ...
    def __onExitZone(self, go, exitCallback, zoneAccessType, who, _):
        ...
    def __onEnterRandomEventZone(self, zoneNotification):
        ...
    def __onExitRandomEventZone(self, zoneNotification):
        ...
    def __onEnterWeatherZone(self, zoneNotification):
        ...
    def __onExitWeatherZone(self, zoneNotification):
        ...
    def __onEnterZoneHint(self, zoneHint):
        ...
    def __onExitZoneHint(self, zoneHint):
        ...
    def __subscribeVehicleChanges(self):
        ...
    def __unsubscribeVehicleChanges(self):
        ...
    def __onVehicleChanged(self, *args, **kwargs):
        ...
    def __onAvatarReady(self):
        ...
    def __onVehicleLeaveWorld(self, vehicle):
        ...

def _isAvatarReady():
    ...
def getHints():
    ...
