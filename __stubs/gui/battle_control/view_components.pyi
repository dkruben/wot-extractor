# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/view_components.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import weakref as weakref
from collections import defaultdict as defaultdict
from soft_exception import SoftException as SoftException
from gui.battle_control.battle_constants import VIEW_COMPONENT_RULE as VIEW_COMPONENT_RULE
from gui.battle_control.controllers.interfaces import IBattleController as IBattleController
_logger: Any

class IViewComponentsCtrlListener(object):
    def detachedFromCtrl(self, ctrlID):
        ...

class IViewComponentsController(IBattleController):
    __slots__: tuple
    def getControllerID(self):
        ...
    def stopControl(self):
        ...
    def startControl(self, *args):
        ...
    def setViewComponents(self, *components):
        ...
    def clearViewComponents(self):
        ...

class ViewComponentsController(IViewComponentsController):
    __slots__: tuple
    _viewComponents: Any
    def __init__(self):
        ...
    def setViewComponents(self, *components):
        ...
    def clearViewComponents(self):
        ...

class ComponentsBridgeError(SoftException):
    ...

class _ComponentsBridge(object):
    __components: Any
    __ctrls: Any
    __indexes: Any
    __componentToCrl: Any
    def __init__(self):
        ...
    def clear(self):
        ...
    def registerViewComponents(self, *data):
        ...
    def addViewComponent(self, componentID, component, rule=...):
        ...
    def removeViewComponent(self, componentID):
        ...
    def registerController(self, ctrl):
        ...
    def registerControllers(self, *ctrls):
        ...
    def __getIndexByComponentID(self, ctrlID, componentID):
        ...

def createComponentsBridge():
    ...
