# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/customization/context/styled_diffs_cache.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from future.utils import viewitems as viewitems
from helpers import dependency as dependency
from items.components.c11n_constants import SeasonType as SeasonType
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from gui.shared.gui_items.customization.c11n_items import Style as Style

class StyleDiffsCache(object):
    __service: Any
    __diffs: Any
    def __init__(self):
        ...
    def fini(self):
        ...
    def saveDiffs(self, style, diffs):
        ...
    def saveDiff(self, style, season, diff):
        ...
    def getDiffs(self, style):
        ...
    def getDiff(self, style, season):
        ...
    def clearDiffs(self):
        ...
    def clearModeDiffs(self, is3D):
        ...
