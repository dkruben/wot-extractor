# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/gui/scaleform/daapi/view/battle/delayed_sixth_sense_indicator.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewvalues as viewvalues
import BigWorld as BigWorld
import SoundGroups as SoundGroups
import WWISE as WWISE
from constants import SERVER_TICK_LENGTH as SERVER_TICK_LENGTH
from SMDetectionDelayObservableComponent import SMDetectionDelayObservableComponent as SMDetectionDelayObservableComponent
from story_mode.gui.scaleform.daapi.view.meta.DelayedSixthSenseMeta import DelayedSixthSenseMeta as DelayedSixthSenseMeta
from story_mode.gui.sound_constants import VDAY_SIXTH_SENSE_SOUND_START as VDAY_SIXTH_SENSE_SOUND_START, VDAY_SIXTH_SENSE_SOUND_STOP as VDAY_SIXTH_SENSE_SOUND_STOP, VDAY_SIXTH_SENSE_RTPC_VALUE as VDAY_SIXTH_SENSE_RTPC_VALUE

class SixthSenseSound(object):
    __startSound: Any
    def __init__(self):
        ...
    def playStart(self):
        ...
    def playStop(self):
        ...
    def fini(self):
        ...
    def update(self, rtpcValue):
        ...

class DelayedSixthSenseIndicator(DelayedSixthSenseMeta):
    FULL_PROGRESS = 100
    _timers: Any
    _timerId: Any
    _isShown: Any
    _sound: Any
    def __init__(self):
        ...
    def _populate(self):
        ...
    def _update(self):
        ...
    def _dispose(self):
        ...
    def __onTimersChange(self, _, timers):
        ...
