# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/hangar/base/blur.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.shared.view_helpers.blur_manager import ImmediateSceneBlurConfig as ImmediateSceneBlurConfig
from helpers import dependency as dependency
from skeletons.gui.game_control import IBlurController as IBlurController, IBlurEffect as IBlurEffect
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace

class RandomHangarBlur(object):
    __blurCtrl: Any
    __hangarSpace: Any
    __settings: Any
    __blur: Any
    def __init__(self, settings=None, enabled=True, persistent=True):
        ...
    def init(self):
        ...
    def destroy(self):
        ...
    def enable(self):
        ...
    def disable(self):
        ...
    def __handleSpaceChange(self):
        ...

def createConfig(enabled=False, spaceID=0, settings=None, persistent=False):
    ...
