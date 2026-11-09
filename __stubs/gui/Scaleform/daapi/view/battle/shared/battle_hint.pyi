# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/battle_hint.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from gui.battle_control.controllers.battle_hints.component import BattleHintComponent as BattleHintComponent
from gui.Scaleform.daapi.view.meta.BattleHintMeta import BattleHintMeta as BattleHintMeta
from gui.battle_control.controllers.battle_hints.queues import BattleHintQueueParams as BattleHintQueueParams
from hints.battle.schemas.base import CHMType as CHMType
_logger: Any
defaultHintQueueParams: Any

class BattleHint(BattleHintComponent, BattleHintMeta):
    def _showHint(self, model, params):
        ...
    def _hideHint(self):
        ...
    def _cancelFadeOut(self):
        ...

class DefaultBattleHint(BattleHint):
    def __init__(self):
        ...
