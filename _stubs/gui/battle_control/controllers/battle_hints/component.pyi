# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/battle_hints/component.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from gui.battle_control.controllers.battle_hints.common import getLogger as getLogger
from gui.battle_control.controllers.battle_hints.queues import BattleHintQueueParams as BattleHintQueueParams
from hints.battle.schemas.base import CHMType as CHMType
from gui.battle_control.controllers.battle_hints.controller import BattleHintsController as BattleHintsController
_logger: Any

class IBattleHintView(object):
    def showHint(self, model, params):
        ...
    def hideHint(self, hint=None):
        ...

class BattleHintComponent(IBattleHintView):
    __sessionProvider: Any
    __battleHintsQueueParams: Any
    def __init__(self, battleHintsQueueParams=None, *args, **kwargs):
        ...
    def getBattleHintsQueueParams(self):
        ...
    def showHint(self, model, params=None):
        ...
    def hideHint(self):
        ...
    def cancelFadeOut(self):
        ...
    def onFadeOutFinished(self):
        ...
    def _showHint(self, model, params):
        ...
    def _hideHint(self):
        ...
    def _cancelFadeOut(self):
        ...
