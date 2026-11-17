# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/common/score_reasons_common/visual_script_common.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from visual_script.block import Block as Block, Meta as Meta, InitParam as InitParam
from visual_script.misc import errorVScript as errorVScript, ASPECT as ASPECT, EDITOR_TYPE as EDITOR_TYPE
from visual_script.slot_types import SLOT_TYPE as SLOT_TYPE
from score_reasons_common.manager import ScoreReasonsModelsManager as ScoreReasonsModelsManager
_BLOCK_ALL_SCOPE_FILTER = '[all]'

class ScoreReasonsMeta(Meta):
    @classmethod
    def blockColor(cls):
        ...
    @classmethod
    def blockCategory(cls):
        ...
    @classmethod
    def blockIcon(cls):
        ...

class BaseSelectScoreReason(Block, ScoreReasonsMeta):
    _uniqueReason: Any
    _name: Any
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

def _getScoreReasonsChoices(modelsMgr):
    ...
