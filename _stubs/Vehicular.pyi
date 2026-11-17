# wot-extractor: STUB do modulo 'Vehicular', SEM CODIGO no cliente (nativo do motor, em C++, ou ausente).
# So lista os membros que o codigo Python usa (24 ficheiro(s)); assinaturas e tipos sao
# desconhecidos (*args/**kwargs e Any). Os comentarios dizem como cada membro e usado.

from typing import Any

BurnoutProcessor: Any  # usado sem chamada 2x
C11nComponent: Any  # usado sem chamada 3x
C11nEditComponent: Any  # usado sem chamada 2x
CollisionObstaclesCollector: Any  # usado sem chamada 7x
CompositeTrack: Any  # usado sem chamada 3x
def ContinuousBurstEvent(*args: Any, **kwargs: Any) -> Any: ...  # chamado 1x com 0 argumento(s) posicional(is); keywords: active, entityID, slotName
DetailedEngineState: Any  # usado sem chamada 7x
DetailedGunState: Any  # usado sem chamada 3x; importado com 'from Vehicular import' em 1 ficheiro(s)
DirtComponent: Any  # usado sem chamada 10x
def FireRateChangedEvent(*args: Any, **kwargs: Any) -> Any: ...  # chamado 1x com 0 argumento(s) posicional(is); keywords: entityID, shotsPerSec, slotName
FlagComponent: Any  # usado sem chamada 5x
FlyingInfoProvider: Any  # usado sem chamada 6x
FrictionAudition: Any  # usado sem chamada 5x
GearBox: Any  # usado sem chamada 5x
GeneralWheelsAnimator: Any  # usado sem chamada 11x
def GeneralWheelsAnimatorConfig(*args: Any, **kwargs: Any) -> Any: ...  # chamado 1x com 1 argumento(s) posicional(is); importado com 'from Vehicular import' em 1 ficheiro(s)
GeneralWheelsAnimatorSystem: Any  # usado sem chamada 1x
GunAudition: Any  # importado com 'from Vehicular import' em 1 ficheiro(s)
GunInstallationComponent: Any  # usado sem chamada 2x
GunRotatorAudition: Any  # usado sem chamada 2x
HaxapodMovementLegComponent: Any  # importado com 'from Vehicular import' em 1 ficheiro(s)
LeveredSuspension: Any  # usado sem chamada 5x
LinkedNodesPitchAnimator: Any  # usado sem chamada 2x
LodCalculator: Any  # usado sem chamada 10x
def MultiShotEvent(*args: Any, **kwargs: Any) -> Any: ...  # chamado 1x com 0 argumento(s) posicional(is); keywords: entityID, gunIDs, slotName
OnPlayerInZoneComponent: Any  # importado com 'from Vehicular import' em 1 ficheiro(s)
def PhysicalDestroyedTrackConfig(*args: Any, **kwargs: Any) -> Any: ...  # chamado 1x com 1 argumento(s) posicional(is)
PhysicalTrackBuilder: Any  # usado sem chamada 2x
def PhysicalTrackCreationData(*args: Any, **kwargs: Any) -> Any: ...  # chamado 1x com 7 argumento(s) posicional(is)
RecoilComponent: Any  # usado sem chamada 4x
RemainingAmmoClipPercentGetter: Any  # importado com 'from Vehicular import' em 1 ficheiro(s)
SiegeState: Any  # usado sem chamada 3x
def SimpleTrackCreationData(*args: Any, **kwargs: Any) -> Any: ...  # chamado 2x com 6 argumento(s) posicional(is)
def SingleShotEvent(*args: Any, **kwargs: Any) -> Any: ...  # chamado 1x com 0 argumento(s) posicional(is); keywords: entityID, gunID, slotName
def SplineTrackCreationData(*args: Any, **kwargs: Any) -> Any: ...  # chamado 2x com 3 argumento(s) posicional(is)
Suspension: Any  # usado sem chamada 7x
SuspensionSound: Any  # usado sem chamada 5x
SwingingAnimator: Any  # usado sem chamada 3x
TankWheelsAnimator: Any  # usado sem chamada 9x
TerrainMatKindSensor: Any  # usado sem chamada 6x
TerrainMatKindSensorSystem: Any  # usado sem chamada 1x
TessellationCollisionSensor: Any  # usado sem chamada 7x
TrackNodesAnimator: Any  # usado sem chamada 6x
def VariablesChangedEvent(*args: Any, **kwargs: Any) -> Any: ...  # chamado 2x com 0 argumento(s) posicional(is); keywords: entityID, slotName, varValueMap
VehicleAudition: Any  # usado sem chamada 7x; importado com 'from Vehicular import' em 1 ficheiro(s)
VehicleAuditionSystem: Any  # usado sem chamada 1x
VehicleSoundTriggerTarget: Any  # usado sem chamada 3x
VehicleTraces: Any  # usado sem chamada 7x
VehicleTracks: Any  # usado sem chamada 9x
def VehicleTracksCreationContext(*args: Any, **kwargs: Any) -> Any: ...  # chamado 1x com 6 argumento(s) posicional(is)
WaterSensor: Any  # usado sem chamada 8x
def getDummyLodLink(*args: Any, **kwargs: Any) -> Any: ...  # chamado 1x com 0 argumento(s) posicional(is)

def __getattr__(name: str) -> Any: ...  # outros membros nao observados
