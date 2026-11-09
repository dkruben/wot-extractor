# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/scaleform/daapi/view/battle/battle_hints.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import time as time
import typing as typing
from fort_rush.gui.scaleform.daapi.view.battle.hud import FortRushHudComponent as FortRushHudComponent
from gui.battle_control.controllers.battle_hints.component import BattleHintComponent as BattleHintComponent
from gui.battle_control.controllers.battle_hints.queues import BattleHintsQueue as BattleHintsQueue, BattleHint as BattleHint
from typing import Optional as Optional, Tuple as Tuple, Union as Union
from fort_rush.gui.battle_hints.battle_hints_schema import FortRushHintModel as FortRushHintModel
from gui.battle_control.controllers.battle_hints.queues import BattleHintQueueParams as BattleHintQueueParams
_logger: Any

class FortRushBattleHintComponent(BattleHintComponent, FortRushHudComponent):
    _alias: Any
    uniqueHints: Any
    def __init__(self, alias, queueParams):
        ...
    def getAlias(self):
        ...
    def _showHint(self, model, params):
        ...
    def _hideHint(self):
        ...

class FortRushBattleHintsQueue(BattleHintsQueue):
    _enabled: Any
    _queue: Any
    def destroy(self):
        ...

class FortRushBattleHint(BattleHint):
    def getPriority(self, currentTime):
        ...
    def show(self):
        ...
