# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/visual_script_client/sound_blocks.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import BigWorld as BigWorld
from visual_script import ASPECT as ASPECT
from visual_script.block import Block as Block, Meta as Meta
from visual_script.dependency import dependencyImporter as dependencyImporter
from visual_script.misc import errorVScript as errorVScript, EDITOR_TYPE as EDITOR_TYPE
from visual_script.slot_types import SLOT_TYPE as SLOT_TYPE, arrayOf as arrayOf
BattleReplay: Any
SoundGroups: Any
MusicControllerWWISE: Any
helpers: Any
Vehicular: Any
tankStructure: Any
_logger: Any

class SoundMeta(Meta):
    @classmethod
    def blockColor(cls):
        ...
    @classmethod
    def blockCategory(cls):
        ...
    @classmethod
    def blockIcon(cls):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class PlaySound(Block, SoundMeta):
    _in: Any
    _sound: Any
    _out: Any
    _onSoundStop: Any
    def __init__(self, *args, **kwargs):
        ...
    def _execute(self):
        ...
    def __onSoundEnd(self, sound):
        ...

class StopSound(Block, SoundMeta):
    _in: Any
    _sound: Any
    _out: Any
    def __init__(self, *args, **kwargs):
        ...
    def _execute(self):
        ...

class Create2DSound(Block, SoundMeta):
    _soundName: Any
    _sound: Any
    def __init__(self, *args, **kwargs):
        ...
    def _execute(self):
        ...

class Create3DSound(Block, SoundMeta):
    _soundName: Any
    _soundObjectName: Any
    _position: Any
    _sound: Any
    def __init__(self, *args, **kwargs):
        ...
    def _execute(self):
        ...

class SetMutedSounds(Block, SoundMeta):
    _in: Any
    _soundNames: Any
    _out: Any
    def __init__(self, *args, **kwargs):
        ...
    def validate(self):
        ...
    def _execute(self):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class PlayCombatMusic(Block, SoundMeta):
    _play: Any
    _stop: Any
    _musicId: Any
    _out: Any
    __combatMusic: Any
    def __init__(self, *args, **kwargs):
        ...
    def _doPlay(self):
        ...
    def _doMute(self):
        ...
    def _execute(self, play):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class SetMusicSkipArenaChanges(Block, SoundMeta):
    _set: Any
    _skip: Any
    _out: Any
    def __init__(self, *args, **kwargs):
        ...
    def _execute(self):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class SetSoundRTPC(Block, SoundMeta):
    _in: Any
    _out: Any
    _soundIn: Any
    _soundOut: Any
    _rtpcName: Any
    _rtpcValue: Any
    def __init__(self, *args, **kwargs):
        ...
    def _setValue(self):
        ...

class SetGlobalSoundRTPC(Block, SoundMeta):
    _in: Any
    _out: Any
    _rtpcName: Any
    _rtpcValue: Any
    def __init__(self, *args, **kwargs):
        ...
    def _setValue(self):
        ...

class SetSoundSwitch(Block, SoundMeta):
    _in: Any
    _out: Any
    _soundIn: Any
    _soundOut: Any
    _switchName: Any
    _switchValue: Any
    def __init__(self, *args, **kwargs):
        ...
    def _setValue(self):
        ...

class GetSoundName(Block, SoundMeta):
    _sound: Any
    _name: Any
    def __init__(self, *args, **kwargs):
        ...
    def _execute(self):
        ...

class IsSoundPlaying(Block, SoundMeta):
    _sound: Any
    _isPlaying: Any
    def __init__(self, *args, **kwargs):
        ...
    def _execute(self):
        ...

class PlayGlobalSound(Block, SoundMeta):
    _in: Any
    _sound: Any
    _out: Any
    def __init__(self, *args, **kwargs):
        ...
    def _execute(self):
        ...

class SetGlobalSoundSwitch(Block, SoundMeta):
    _in: Any
    _out: Any
    _switchName: Any
    _switchValue: Any
    def __init__(self, *args, **kwargs):
        ...
    def _setValue(self):
        ...

class SetGlobalSoundState(Block, SoundMeta):
    _in: Any
    _out: Any
    _stateGroupName: Any
    _stateName: Any
    def __init__(self, *args, **kwargs):
        ...
    def _setValue(self):
        ...

class TriggerSoundOnEngine(Block, SoundMeta):
    _in: Any
    _object: Any
    _eventName: Any
    _out: Any
    def __init__(self, *args, **kwargs):
        ...
    def _execute(self):
        ...

class ScheduleDelayedSound2D(Block, SoundMeta):
    _start: Any
    _stop: Any
    _remainingTime: Any
    _timeBeforeEnd: Any
    _threshold: Any
    _sound: Any
    _startOut: Any
    _stopOut: Any
    __timerCallbackID: Any
    def __init__(self, *args, **kwargs):
        ...
    def captionText(self):
        ...
    def onFinishScript(self):
        ...
    def __initDefaults(self):
        ...
    def __start(self):
        ...
    def __stop(self):
        ...
    def __startTimer(self, delay):
        ...
    def __cancelTimer(self):
        ...
    def __playSoundAfterDelay(self):
        ...
    def __playSound(self):
        ...
    def __stopSound(self):
        ...
