# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/gui/fade_in_out.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from functools import wraps as wraps
from BWUtil import AsyncReturn as AsyncReturn
from gui.impl.common.fade_manager import UseFading as UseFading
from gui.shared.close_confiramtor_helper import CloseConfirmatorsHelper as CloseConfirmatorsHelper
from helpers import dependency as dependency
from story_mode.skeletons.story_mode_fading_controller import IStoryModeFadingController as IStoryModeFadingController
from wg_async import wg_await as wg_await, wg_async as wg_async, forwardAsFuture as forwardAsFuture
_logger: Any

class UseStoryModeFading(UseFading):
    _fadeManager: Any

class UseHeaderNavigationImpossible(object):
    def __call__(self, func):
        ...
