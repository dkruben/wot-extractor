# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/uilogging/core/integration.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import json as json
import logging as logging
import typing as typing
from gui.impl.gen.view_models.common.ui_logger_model import UiLoggerModel as UiLoggerModel
from helpers import dependency as dependency
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from skeletons.ui_logging import IUILoggingCore as IUILoggingCore, IUILoggingListener as IUILoggingListener
from wotdecorators import noexcept as noexcept
_logger: Any

class UILoggingListener(IUILoggingListener):
    _core: Any
    __slots__: tuple
    __model: Any
    def __init__(self):
        ...
    def fini(self):
        ...
    # decorador original: @noexcept
    def _log(self, args):
        ...
