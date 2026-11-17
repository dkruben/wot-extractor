# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/battle_hints/queues.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import time as time
from functools import partial as partial
import typing as typing
from future.utils import viewvalues as viewvalues
import BigWorld as BigWorld
import SoundGroups as SoundGroups
from gui.battle_control.controllers.battle_hints.common import getLogger as getLogger, DEFAULT_LOGGER_NAME as DEFAULT_LOGGER_NAME, HIGHEST_PRIORITY as HIGHEST_PRIORITY, QUEUE_HINTS_MAX_SIZE as QUEUE_HINTS_MAX_SIZE, HIDE_ANIMATION_TIMEOUT as HIDE_ANIMATION_TIMEOUT
from shared_utils import safeCancelCallback as safeCancelCallback
from helpers.log.adapters import getWithContext as getWithContext
from wotdecorators import condition as condition
from debug_utils import LOG_WARNING as LOG_WARNING
from PlayerEvents import g_playerEvents as g_playerEvents
import weakref as weakref
from typing import Optional as Optional, Dict as Dict, Union as Union, Tuple as Tuple, List as List, Type as Type
from hints.battle.schemas.base import CHMType as CHMType
from gui.battle_control.controllers.battle_hints.component import BattleHintComponent as BattleHintComponent
from gui.battle_control.controllers.battle_hints.history import BattleHintsHistory as BattleHintsHistory
_hintLogger: Any
_mgrLogger: Any

class BattleHint(object):
    __slots__: tuple
    _model: Any
    _component: Any
    _history: Any
    _params: Any
    _enqueueTime: Any
    _startDisplayTime: Any
    _maxPriorityOffset: Any
    def __init__(self, model, component, history=None, params=None):
        ...
    def __eq__(self, other):
        ...
    def __ne__(self, other):
        ...
    def __hash__(self):
        ...
    @property
    def model(self):
        ...
    @property
    def uniqueName(self):
        ...
    @property
    def unique(self):
        ...
    @property
    def showTime(self):
        ...
    @property
    def minShowTime(self):
        ...
    @property
    def minDisplayTimeLeft(self):
        ...
    @property
    def params(self):
        ...
    def setMaxPriority(self, offset):
        ...
    def getPriority(self, currentTime):
        ...
    def canBeShown(self, currentTime=None):
        ...
    def enqueued(self):
        ...
    def show(self):
        ...
    def hide(self):
        ...
    def cancelFadeOut(self):
        ...
    def isOutdated(self, currentTime):
        ...
    def _getLastDisplayTime(self):
        ...
    def _isOnCooldown(self, currentTime=None):
        ...
    def _playSound(self):
        ...

class BattleHintsQueue(object):
    __slots__: tuple
    ifEnabled: Any
    _maxSize: Any
    _displayed: Any
    _queue: Any
    _delayerId: Any
    _withFadeOut: Any
    _fadeOutCallbackId: Any
    _enabled: Any
    _logger: Any
    def __init__(self, maxSize=..., withFadeOut=True):
        ...
    # decorador original: @ifEnabled
    def add(self, hint):
        ...
    # decorador original: @ifEnabled
    def remove(self, hint):
        ...
    # decorador original: @ifEnabled
    def hide(self, hint, immediately=False):
        ...
    # decorador original: @ifEnabled
    def onFadeOutFinished(self):
        ...
    def destroy(self):
        ...
    # decorador original: @ifEnabled
    def _onWaitingFadeOutTimeout(self, hint):
        ...
    @property
    def _waitingForFadeOut(self):
        ...
    def _showNextHint(self):
        ...
    def _selectNextHint(self):
        ...
    def _show(self, hint):
        ...
    def _hide(self, withFadeOut=True):
        ...
    def _stopWaitingFadeOut(self):
        ...
    def _startWaitingFadeOut(self, hint):
        ...
    def _stopDelayer(self):
        ...
    def _restartDelayer(self, delay):
        ...

class BattleHintQueueParams(object):
    __slots__: tuple
    _name: Any
    _queueClass: Any
    _maxSize: Any
    _withFadeOut: Any
    _hintClass: Any
    _queueId: Any
    def __init__(self, name, queueClass=None, maxSize=..., withFadeOut=True, hintClass=None):
        ...
    @property
    def queueId(self):
        ...
    def createQueue(self):
        ...
    def createHint(self, model, component, history=None, params=None):
        ...
    def __repr__(self):
        ...

class BattleHintsQueuesMgr(object):
    __slots__: tuple
    ifEnabled: Any
    _queues: Any
    _enabled: Any
    def __init__(self):
        ...
    # decorador original: @ifEnabled
    def get(self, params):
        ...
    def destroy(self):
        ...
