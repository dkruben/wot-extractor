# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/tutorial/control/sales/functional.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from debug_utils import LOG_ERROR as LOG_ERROR
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams as SFViewLoadParams
from gui.shared import g_eventBus as g_eventBus, events as events
from tutorial.control.functional import FunctionalEffect as FunctionalEffect
from tutorial.data.hints import HintProps as HintProps
from tutorial.gui import GUI_EFFECT_NAME as GUI_EFFECT_NAME

class LoadViewEffect(FunctionalEffect):
    _isRunning: Any
    def __init__(self, effect):
        ...
    def triggerEffect(self):
        ...

class FunctionalShowHint(FunctionalEffect):
    def isInstantaneous(self):
        ...
    def isStillRunning(self):
        ...
    def triggerEffect(self):
        ...

class FunctionalCloseHint(FunctionalEffect):
    def triggerEffect(self):
        ...
