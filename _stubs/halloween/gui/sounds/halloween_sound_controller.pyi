# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/sounds/halloween_sound_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BattleReplay as BattleReplay
import SoundGroups as SoundGroups
import WWISE as WWISE
from constants import IS_CHINA as IS_CHINA, IS_CT as IS_CT
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from halloween.gui.sounds import playSound as playSound
from halloween.skeletons.halloween_sound_controller import IHalloweenSoundController as IHalloweenSoundController
from halloween.skeletons.halloween_controller import IHalloweenController as IHalloweenController
from halloween.gui.sounds.sound_constants import SoundLanguage as SoundLanguage, HW_ENTER_EVENT as HW_ENTER_EVENT, HW_EXIT_EVENT as HW_EXIT_EVENT, HW_SOUND_REMAPPING as HW_SOUND_REMAPPING, HW_RESET_HANGAR_MUSIC_EVENT as HW_RESET_HANGAR_MUSIC_EVENT
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

class HalloweenSoundController(IHalloweenSoundController, IGlobalListener):
    _guiLoader: Any
    _hwController: Any
    _hangarEnterEventPlayed: Any
    def __init__(self, *args, **kwargs):
        ...
    def onAvatarBecomePlayer(self):
        ...
    def onLobbyInited(self, event):
        ...
    def onAccountBecomePlayer(self):
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

def getEventVoiceoverLanguage():
    ...
