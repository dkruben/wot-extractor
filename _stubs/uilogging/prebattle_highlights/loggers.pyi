# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/uilogging/prebattle_highlights/loggers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import json as json
import logging as logging
from typing import TYPE_CHECKING as TYPE_CHECKING, NamedTuple as NamedTuple, Tuple as Tuple
from uilogging.base.logger import MetricsLogger as MetricsLogger
from uilogging.prebattle_highlights.constants import FEATURE as FEATURE, PrebattleHighlightsLogAction as PrebattleHighlightsLogAction, PrebattleHighlightsLogKeys as PrebattleHighlightsLogKeys
from typing import Dict as Dict, Any as Any, Optional as Optional
_logger: _Any
PBHViewingLogInfo: _Any

class PrebattleHighlightsEventLogger(MetricsLogger):
    __viewingLogInfo: _Any
    def __init__(self):
        ...
    def reset(self):
        ...
    def logStartViewingAction(self, info):
        ...
    def logStopViewingAction(self, viewStatus):
        ...
    def logSkipViewingEvent(self, info):
        ...
    def logUnfocusClientEvent(self):
        ...
