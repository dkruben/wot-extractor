# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/SequenceNetworkSync.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import BigWorld as BigWorld
import CGF as CGF
from constants import HAS_DEV_RESOURCES as HAS_DEV_RESOURCES
from cgf_client_common.entity_dyn_components import ReplicableDynamicScriptComponent as ReplicableDynamicScriptComponent
from cgf_components.sequence_components import SequencePauseComponent as SequencePauseComponent, SequenceSnapshotComponent as SequenceSnapshotComponent
from cgf_script.registration import registerReplicableComponent as registerReplicableComponent, ComponentProperty as ComponentProperty
from GenericComponents import Sequence as Sequence
_logger: Any
_STATE_STOPPED = Sequence.State.Stopped
_STATE_PAUSED = Sequence.State.Paused
_STATE_RUNNING = Sequence.State.Running
_INT_STATE_STOPPED: Any
_INT_STATE_PAUSED: Any
_INT_STATE_RUNNING: Any

# decorador original: @registerReplicableComponent
class SequenceNetworkSync(ReplicableDynamicScriptComponent):
    editorTitle = 'Sequence Network Sync'
    timeCorrection: Any
    expired: Any
    def __init__(self):
        ...
    @property
    def name(self):
        ...
    @property
    def actualTime(self):
        ...
    def set_transition(self, prev):
        ...
    def set_speed(self, prev):
        ...
    def set_state(self, prev):
        ...
    def set_activeLayerIdx(self, prev):
        ...
    def start(self):
        ...
    def stop(self):
        ...
    def pause(self):
        ...
    def requestTime(self, time):
        ...
    def requestLayerChange(self, layerIdx, time):
        ...

class SequenceSnapshot(object):
    syncTime: Any
    speed: Any
    state: Any
    activeLayerIdx: Any
    transition: Any
    def __init__(self, syncTime=0.0, speed=1.0, state=0, activeLayerIdx=0, transition=None):
        ...

class SequenceNetworkSyncSystem(CGF.System):
    SequenceSyncIterate: Any
    SequenceActivated: Any
    SequenceDeactivated: Any
    SnapshotActivated: Any
    SnapshotDeactivated: Any
    PauseActivated: Any
    PauseDeactivated: Any
    Reactions: Any
    __isSyncPaused: Any
    __snapshots: Any
    def __init__(self):
        ...
    def update(self):
        ...
    @staticmethod
    def __syncSequence(sync, sequence):
        ...
    @staticmethod
    def __trySyncTransition(sync, sequence):
        ...
    @staticmethod
    def __trySyncActiveLayerIdx(sync, sequence):
        ...
    @staticmethod
    def __syncLayer(sync, sequence):
        ...
    @staticmethod
    def __updateTime(sync, sequence):
        ...
