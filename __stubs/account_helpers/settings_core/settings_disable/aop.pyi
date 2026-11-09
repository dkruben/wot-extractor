# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/account_helpers/settings_core/settings_disable/aop.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems
from typing import TYPE_CHECKING as TYPE_CHECKING
from helpers import aop as aop
from typing import Dict as Dict, Sequence as Sequence

class _FlashDisableSettingsAspect(aop.Aspect):
    __disabledSettings: Any
    def __init__(self, settings):
        ...
    def atCall(self, cd):
        ...
    def __disableControl(self, cd, itemId, guiPath):
        ...

class DisableCameraSettingsFlashPointcut(aop.Pointcut):
    def __init__(self, settings):
        ...

class DisableAltModeTogglePointcut(aop.Pointcut):
    def __init__(self):
        ...
