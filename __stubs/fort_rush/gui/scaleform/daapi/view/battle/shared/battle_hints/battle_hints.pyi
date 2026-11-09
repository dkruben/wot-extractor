# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/scaleform/daapi/view/battle/shared/battle_hints/battle_hints.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from fort_rush.gui.scaleform.daapi.view.meta.ExampleBattleHintMeta import ExampleBattleHintMeta as ExampleBattleHintMeta
from gui.battle_control.controllers.battle_hints.component import BattleHintComponent as BattleHintComponent
from gui.Scaleform.daapi.view.battle.shared.battle_hint import BattleHint as BattleHint
from gui.battle_control.controllers.battle_hints.queues import BattleHintQueueParams as BattleHintQueueParams
BATTLE_HINTS_QUEUE_ID: Any

class FortRushBattleHint(BattleHint):
    def __init__(self):
        ...

class FortRushOffsetBattleHint(BattleHintComponent, ExampleBattleHintMeta):
    def __init__(self):
        ...
    def _showHint(self, model, params):
        ...
    def _hideHint(self):
        ...
    def _cancelFadeOut(self):
        ...
