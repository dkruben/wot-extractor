# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/visual_script_client/battle_hints_blocks.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from hints.battle import manager as battleHintsModelsMgr
from visual_script.slot_types import SLOT_TYPE as SLOT_TYPE
from visual_script.misc import ASPECT as ASPECT, errorVScript as errorVScript
from visual_script.block import Block as Block
from visual_script.dependency import dependencyImporter as dependencyImporter
from visual_script.battle_hints_common import BaseSelectHint as BaseSelectHint, BaseHintAction as BaseHintAction, HintActionParamsMixin as HintActionParamsMixin, HintsMeta as HintsMeta
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from gui.battle_control.controllers.battle_hints.controller import BattleHintsController as BattleHintsController
from hints.battle.schemas.base import CHMType as CHMType
from hints_common.battle.manager import CommonBattleHintsModelsManager as CommonBattleHintsModelsManager
dependency: Any

class SelectHint(BaseSelectHint):
    @classmethod
    def blockAspects(cls):
        ...
    @classmethod
    def _getModelsManager(cls, initialize=False):
        ...

class CanShowHint(Block, HintsMeta):
    _hintId: Any
    _result: Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def blockAspects(cls):
        ...
    def _execute(self):
        ...

class ReceiverMixin(object):
    def _getReceivers(self):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class ShowHint(ReceiverMixin, HintActionParamsMixin, BaseHintAction):
    RESERVED: Any
    _immediately: Any
    def __init__(self, *args, **kwargs):
        ...
    def _doAction(self, controller, hintId):
        ...

class HideHint(ReceiverMixin, BaseHintAction):
    def _doAction(self, controller, hintId):
        ...

class RemoveHint(ReceiverMixin, BaseHintAction):
    _hide: Any
    def __init__(self, *args, **kwargs):
        ...
    def _doAction(self, controller, hintId):
        ...
