# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/battle_hints/controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import sys as sys
import weakref as weakref
import typing as typing
from typing import Optional as Optional, Dict as Dict, Tuple as Tuple, Union as Union
import BattleReplay as BattleReplay
from PlayerEvents import g_playerEvents as g_playerEvents
from debug_utils import LOG_DEBUG as LOG_DEBUG
from gui.battle_control.view_components import ViewComponentsController as ViewComponentsController
from gui.battle_control.battle_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from gui.battle_control.controllers.battle_hints import replay as replay
from gui.battle_control.controllers.battle_hints.common import getLogger as getLogger
from gui.battle_control.controllers.battle_hints.queues import BattleHintsQueuesMgr as BattleHintsQueuesMgr
from gui.battle_control.controllers.battle_hints.component import BattleHintComponent as BattleHintComponent
from gui.battle_control.controllers.battle_hints.history import BattleHintsHistory as BattleHintsHistory
from hints.battle import manager as battleHintsModelsMgr
from shared_utils import findFirst as findFirst
from ids_generators import SequenceIDGenerator as SequenceIDGenerator
from wotdecorators import condition as condition
from hints.battle.schemas.base import CHMType as CHMType
from gui.battle_control.controllers.battle_hints.queues import BattleHintsQueue as BattleHintsQueue, BattleHint as BattleHint
BHComponentTypes: Any
_logger: Any

class BattleHintsController(ViewComponentsController):
    __slots__: tuple
    ifStarted: Any
    _closeOnRoundFinished: Any
    _started: Any
    _modelsMgr: Any
    _queuesMgr: Any
    _history: Any
    _maxPriorityOffset: Any
    _components: Any
    _replayController: Any
    def __init__(self, closeOnRoundFinished=True):
        ...
    def getControllerID(self):
        ...
    def clearViewComponents(self):
        ...
    def startControl(self, *args):
        ...
    def stopControl(self):
        ...
    # decorador original: @ifStarted
    def showHint(self, hintName, params=None, immediately=False):
        ...
    # decorador original: @ifStarted
    def hideHint(self, hintName):
        ...
    # decorador original: @ifStarted
    def removeHint(self, hintName, hide=False):
        ...
    # decorador original: @ifStarted
    def onFadeOutFinished(self, component):
        ...
    def getComponent(self, alias):
        ...
    def checkHintInQueue(self, hintName):
        ...
    def _onRoundFinished(self, *_, **__):
        ...
    def _stop(self):
        ...
    def _prepare(self, hintName, params=None):
        ...
    def _getModel(self, hintName):
        ...
    def _findComponent(self, alias):
        ...
