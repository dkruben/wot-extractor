# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gui_factories.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from constants import IS_DEVELOPMENT as IS_DEVELOPMENT
from debug_utils import LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION, LOG_ERROR as LOG_ERROR
from frameworks.wulf import WindowLayer as WindowLayer
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent as BaseDAAPIComponent
from gui.Scaleform.framework.entities.BaseDAAPIModule import BaseDAAPIModule as BaseDAAPIModule
from gui.Scaleform.framework.entities.View import View as View
from gui.Scaleform.framework.entities.wulf_adapter import WulfPackageLayoutAdapter as WulfPackageLayoutAdapter
from gui.shared.events import LoadViewEvent as LoadViewEvent
from py2to3.backport.inspect import getargspec as getargspec
from soft_exception import SoftException as SoftException
from typing import Tuple as Tuple

class BaseGuiEntityFactory(object):
    __managedLayers: Any
    def __init__(self, managedLayers):
        ...
    def getManagedLayers(self):
        ...
    def validate(self, settings):
        ...
    def create(self, settings, *args, **kwargs):
        ...
    def initialize(self, pyEntity, gfxEntity, extra=None):
        ...

class DAAPIModuleFactory(BaseGuiEntityFactory):
    def validate(self, settings):
        ...
    def initialize(self, pyEntity, gfxEntity, extra=None):
        ...
    def create(self, settings, *args, **kwargs):
        ...

class ViewFactory(DAAPIModuleFactory):
    def validate(self, settings):
        ...
    def create(self, settings, *args, **kwargs):
        ...
    def initialize(self, pyEntity, gfxEntity, extra=None):
        ...

class GuiEntitiesFactories(object):
    __settings: Any
    __factories: Any
    __eventToAlias: Any
    __aliasToEvent: Any
    __layers: Any
    def __init__(self, factories=None):
        ...
    def initSettings(self, settingsList):
        ...
    def clearSettings(self, aliases):
        ...
    def addSettings(self, settings):
        ...
    def removeSettings(self, alias):
        ...
    def getSettings(self, alias):
        ...
    def getAliasByEvent(self, eventType):
        ...
    def makeShowPopoverEvent(self, loadParams, ctx=None):
        ...
    def factory(self, alias, *args, **kwargs):
        ...
    def initialize(self, pyEntity, gfxEntity, factoryIdx, extra=None):
        ...

def _getDefaultFactories():
    ...
