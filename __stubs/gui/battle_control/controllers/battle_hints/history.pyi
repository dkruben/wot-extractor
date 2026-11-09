# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/battle_hints/history.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import time as time
import typing as typing
import BattleReplay as BattleReplay
from PlayerEvents import g_playerEvents as g_playerEvents
from account_helpers import AccountSettings as AccountSettings
from debug_utils import LOG_WARNING as LOG_WARNING
from gui.battle_control.controllers.battle_hints.common import getLogger as getLogger
from wotdecorators import condition as condition
from gui.battle_control.controllers.battle_hints.queues import BattleHint as BattleHint
_logger: Any
_PREFS_NAME = 'displayHistory'

class BattleHintsHistory(object):
    __slots__: tuple
    ifEnabled: Any
    _history: Any
    _enabled: Any
    def __init__(self):
        ...
    def getLastDisplayTime(self, uniqueName):
        ...
    def getTotalDisplayCount(self, uniqueName):
        ...
    def getPerBattleCount(self, uniqueName):
        ...
    def destroy(self, *_, **__):
        ...
    # decorador original: @ifEnabled
    def _load(self):
        ...
    def _update(self, battleHint):
        ...

def _createEmptyHistory():
    ...
