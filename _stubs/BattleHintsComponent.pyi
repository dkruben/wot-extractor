# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/BattleHintsComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import logging as logging
from BigWorld import DynamicScriptComponent as DynamicScriptComponent
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from gui.battle_control.controllers.battle_hints.controller import BattleHintsController as BattleHintsController
_logger: Any

class BattleHintsComponent(DynamicScriptComponent):
    sessionProvider: Any
    def showHint(self, hintName, hintParams, immediately=False):
        ...
    def hideHint(self, hintName):
        ...
    def removeHint(self, hintName, hide=False):
        ...
