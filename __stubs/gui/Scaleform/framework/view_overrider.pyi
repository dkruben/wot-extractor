# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/framework/view_overrider.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import typing as typing
import Event as Event
from helpers import dependency as dependency
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from typing import Callable as Callable, Any as Any, Dict as Dict, Tuple as Tuple, Optional as Optional, Union as Union
from gui.Scaleform.framework.managers.loaders import GuiImplViewLoadParams as GuiImplViewLoadParams, ViewLoadParams as ViewLoadParams

class ViewOverrider(object):
    __slots__: tuple
    __gui: _Any
    __delegates: _Any
    __lastOverrides: _Any
    onViewOverriden: _Any
    def __init__(self):
        ...
    def getOverrideData(self, loadParams, *args, **kwargs):
        ...
    def addOverride(self, alias, delegate):
        ...
    def removeOverride(self, alias, delegate):
        ...
    def isViewOverriden(self, alias):
        ...

class OverrideData(object):
    __slots__: tuple
    __loadParams: _Any
    __args: _Any
    __kwargs: _Any
    def __init__(self, loadParams, *args, **kwargs):
        ...
    @property
    def loadParams(self):
        ...
    @property
    def args(self):
        ...
    @property
    def kwargs(self):
        ...
    def checkCondition(self, *args, **kwargs):
        ...
    def prepareAdditionalParams(self, params, *args, **kwargs):
        ...
    def getFadeCtx(self):
        ...
