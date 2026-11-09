# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/VOIP/VOIPHandler.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from wotdecorators import noexcept as noexcept
_logger: Any
MESSAGE_IDS: dict
MSG_VOIP_INITED = 0
MSG_VOIP_DESTROYED = 1
MSG_CAPTURE_DEVICES = 10
MSG_SET_CAPTURE_DEVICE = 11
MSG_SET_LOCAL_SPEAKER_VOLUME = 20
MSG_SET_LOCAL_MIC_VOLUME = 21
MSG_MUTE_LOCAL_MIC = 22
MSG_LOGIN_STATE_CHANGE = 30
MSG_SESSION_ADDED = 42
MSG_SESSION_REMOVED = 43
MSG_NETWORK_TEST = 50
MSG_PARTICIPANT_ADDED = 60
MSG_PARTICIPANT_REMOVED = 61
MSG_PARTICIPANT_UPDATED = 62
MSG_LOG = 100

class VOIPHandler(object):
    def __init__(self):
        ...
    def onVoipInited(self, data):
        ...
    def onVoipDestroyed(self, data):
        ...
    def onCaptureDevicesArrived(self, data):
        ...
    def onSetCaptureDevice(self, data):
        ...
    def onSetLocalSpeakerVolume(self, data):
        ...
    def onSetLocalMicVolume(self, data):
        ...
    def onMuteLocalMic(self, data):
        ...
    def onLoginStateChange(self, data):
        ...
    def onSessionAdded(self, data):
        ...
    def onSessionRemoved(self, data):
        ...
    def onNetworkTest(self, data):
        ...
    def onParticipantAdded(self, data):
        ...
    def onParticipantRemoved(self, data):
        ...
    def onParticipantUpdated(self, data):
        ...
    def onLog(self, data):
        ...
    # decorador original: @noexcept
    def __call__(self, message, data=None):
        ...
