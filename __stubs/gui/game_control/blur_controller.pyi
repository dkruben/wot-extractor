# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/blur_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from gui.doc_loaders.blur_loader import readBlurSettings as readBlurSettings
from gui.shared.view_helpers.blur_manager import BlurManager as BlurManager, BlurEffect as BlurEffect
from skeletons.gui.game_control import IBlurController as IBlurController
_logger: Any

class BlurController(IBlurController):
    _settings: Any
    _manager: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def onAccountBecomeNonPlayer(self):
        ...
    def getSettingsByAlias(self, alias):
        ...
    def createBlur(self, config):
        ...
