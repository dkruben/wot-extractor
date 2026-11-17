# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/impl/lobby/mode_selector/items/fun_random_mode_selector_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from fun_random.gui.feature.util.fun_mixins import FunAssetPacksMixin as FunAssetPacksMixin, FunSubModesWatcher as FunSubModesWatcher
from fun_random.gui.impl.lobby.common.fun_view_helpers import getConditionText as getConditionText
from shared_utils import first as first
from fun_random.gui.feature.sub_modes.base_sub_mode import IFunSubMode as IFunSubMode

class IModeSelectorHelper(object):
    __slots__: tuple
    def isDisabled(self):
        ...
    def getConditionText(self):
        ...
    def clear(self):
        ...

class _SingleModeSelectorHelper(IModeSelectorHelper, FunAssetPacksMixin, FunSubModesWatcher):
    __slots__: tuple
    __subMode: Any
    def __init__(self, subMode):
        ...
    def isDisabled(self):
        ...
    def getConditionText(self):
        ...
    def clear(self):
        ...

class _MultiModesSelectorHelper(IModeSelectorHelper):
    __slots__: tuple
    def isDisabled(self):
        ...
    def getConditionText(self):
        ...

def createSelectorHelper(subModes):
    ...
