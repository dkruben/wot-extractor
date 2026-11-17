# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/battle_hints/replay.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from typing import Optional as Optional, Dict as Dict, Union as Union
import BattleReplay as BattleReplay
from BattleReplay import CallbackDataNames as CallbackDataNames
from PlayerEvents import g_playerEvents as g_playerEvents
from gui.battle_control.controllers.battle_hints.common import getLogger as getLogger
from helpers import dependency as dependency
from hints.battle import manager as battleHintsModelsMgr
from skeletons.gui.battle_hints.battle_hints_overlap_controller import IBattleHintsOverlapController as IBattleHintsOverlapController
from hints.battle.schemas.base import CHMType as CHMType
from gui.battle_control.controllers.battle_hints.queues import BattleHint as BattleHint
from gui.battle_control.controllers.battle_hints.controller import BattleHintsController as BattleHintsController
_logger: Any

class BattleHintsReplayRecorder(object):
    def __init__(self):
        ...
    def fini(self):
        ...
    def onShowBattleHint(self, battleHint):
        ...
    def onHideBattleHint(self, battleHint):
        ...
    def serializeMethod(self, eventName, hintName, params):
        ...

class BattleHintsReplayPlayer(object):
    _overlapController: Any
    _modelsMgr: Any
    battleHintsCtrl: Any
    __currentHint: Any
    def __init__(self, battleHintsCtrl):
        ...
    def fini(self):
        ...
    def _getHint(self, hintName, params):
        ...
    def _showHint(self, hintName, params):
        ...
    def _hideHint(self, hintName, params):
        ...

def getReplayController(battleHintsCtrl):
    ...
