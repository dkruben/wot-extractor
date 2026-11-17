# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/sounds/ls_sound_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BattleReplay as BattleReplay
import SoundGroups as SoundGroups
import WWISE as WWISE
from constants import IS_CHINA as IS_CHINA
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from last_stand.gui.sounds import playSound as playSound
from last_stand.skeletons.ls_sound_controller import ILSSoundController as ILSSoundController
from last_stand.skeletons.ls_controller import ILSController as ILSController
from last_stand.gui.sounds.sound_constants import SoundLanguage as SoundLanguage, LS_ENTER_EVENT as LS_ENTER_EVENT, LS_EXIT_EVENT as LS_EXIT_EVENT
from helpers import dependency as dependency, getClientLanguage as getClientLanguage
from skeletons.gui.impl import IGuiLoader as IGuiLoader
_SOUNDS_WINDOW_STATUS_UPDATE: dict

class _StatusUpdateOperation(object):
    def execute(self):
        ...

class _StatusUpdateEvent(_StatusUpdateOperation):
    _event: Any
    def __init__(self, event):
        ...
    def execute(self):
        ...

class _StatusUpdateState(_StatusUpdateOperation):
    _group: Any
    _value: Any
    def __init__(self, group, value):
        ...
    def execute(self):
        ...

class LSSoundController(ILSSoundController, IGlobalListener):
    _guiLoader: Any
    lsCtrl: Any
    _hangarEnterEventPlayed: Any
    def __init__(self, *args, **kwargs):
        ...
    def onAvatarBecomePlayer(self):
        ...
    def onLobbyStarted(self, ctx):
        ...
    def onLobbyInited(self, event):
        ...
    def onAccountBecomeNonPlayer(self):
        ...
    def onConnected(self):
        ...
    def __setEventVoiceoverLanguage(self):
        ...
    def onPrbEntitySwitched(self):
        ...
    def playSoundEvent(self, audioEvent):
        ...
    def _playEnter(self):
        ...
    def _playExit(self):
        ...
    def __onWindowStatusChanged(self, uniqueID, newStatus):
        ...
