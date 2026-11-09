# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/framework/ui_logging_manager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.framework.entities.abstract.UILoggerManagerMeta import UILoggerManagerMeta as UILoggerManagerMeta
from gui.shared.utils import flashObject2Dict as flashObject2Dict
from helpers import dependency as dependency
from skeletons.ui_logging import IUILoggingCore as IUILoggingCore
from wotdecorators import noexcept as noexcept

class UILoggerManager(UILoggerManagerMeta):
    _logger: Any
    # decorador original: @noexcept
    def onLog(self, feature, group, action, logLevel, params):
        ...
