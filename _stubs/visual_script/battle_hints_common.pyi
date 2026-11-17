# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/visual_script/battle_hints_common.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from hints_common.battle.schemas.const import BLOCK_ALL_HINTS_SCOPE_FILTER as BLOCK_ALL_HINTS_SCOPE_FILTER
from visual_script.block import Block as Block, Meta as Meta, InitParam as InitParam
from visual_script.misc import errorVScript as errorVScript, ASPECT as ASPECT, EDITOR_TYPE as EDITOR_TYPE
from visual_script.slot_types import SLOT_TYPE as SLOT_TYPE
from hints_common.battle.manager import CommonBattleHintsModelsManager as CommonBattleHintsModelsManager

class HintsMeta(Meta):
    @classmethod
    def blockColor(cls):
        ...
    @classmethod
    def blockCategory(cls):
        ...
    @classmethod
    def blockIcon(cls):
        ...

class BaseSelectHint(Block, HintsMeta):
    _hintId: Any
    _id: Any
    def __init__(self, *args, **kwargs):
        ...
    def validate(self):
        ...
    @classmethod
    def initParams(cls):
        ...
    def captionText(self):
        ...
    @classmethod
    def blockAspects(cls):
        ...
    @classmethod
    def _getModelsManager(cls, initialize=False):
        ...

class BaseHintAction(Block, HintsMeta):
    _in: Any
    _hintId: Any
    _out: Any
    def __init__(self, *args, **kwargs):
        ...
    def _execute(self):
        ...
    def _getReceivers(self):
        ...
    def _doAction(self, controller, hintId):
        ...

class HintActionParamsMixin(object):
    RESERVED: tuple
    _params: Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def initParams(cls):
        ...
    def _prepareParams(self, paramsString):
        ...
    def _getParams(self):
        ...

def _getHintsChoices(modelsMgr):
    ...
