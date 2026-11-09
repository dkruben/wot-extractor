# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/framework/managers/loaders.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from future.utils import viewvalues as viewvalues
import BigWorld as BigWorld
import Event as Event
import constants as constants
from gui.Scaleform.framework import ViewSettings as ViewSettings, ScopeTemplates as ScopeTemplates
from gui.Scaleform.framework.entities.View import View as View, ViewKey as ViewKey
from gui.Scaleform.framework.entities.abstract.LoaderManagerMeta import LoaderManagerMeta as LoaderManagerMeta
from gui.Scaleform.framework.entities.sf_window import SFWindow as SFWindow
from gui.Scaleform.framework.entities.view_impl_adaptor import ViewImplAdaptor as ViewImplAdaptor
from gui.Scaleform.framework.entities.wulf_adapter import WulfPackageLayoutAdapter as WulfPackageLayoutAdapter
from gui.Scaleform.framework.settings import UIFrameworkImpl as UIFrameworkImpl
from gui.Scaleform.framework.view_overrider import ViewOverrider as ViewOverrider
from gui.impl.common.fade_manager import UseFading as UseFading
from helpers import dependency as dependency, uniprof as uniprof
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from skeletons.tutorial import ITutorialLoader as ITutorialLoader
from soft_exception import SoftException as SoftException
from frameworks.wulf import Window as Window
from gui.Scaleform.framework.ScopeTemplates import SimpleScope as SimpleScope
_VIEW_REGION_COLOR = 3368601
_LOADING_VIEW_REGION_COLOR = 6710937
NO_IMPL_ALIAS = 'noImpl'
NO_IMPL_URL = 'development/noImpl.swf'
_logger: Any
g_viewOverrider: Any

class _LoadingItem(object):
    __slots__: tuple
    loadParams: Any
    pyEntity: Any
    factoryIdx: Any
    args: Any
    kwargs: Any
    isCancelled: Any
    isModal: Any
    uid: Any
    def __init__(self, loadParams, uid, pyEntity, factoryIdx, isModal, args, kwargs):
        ...
    def __repr__(self):
        ...
    @property
    def name(self):
        ...
    @property
    def loadMode(self):
        ...

class ViewLoadMode(CONST_CONTAINER):
    DEFAULT = 'default'
    PRELOAD = 'preload'

class ViewLoadParams(object):
    __slots__: tuple
    __viewKey: Any
    __loadMode: Any
    __parent: Any
    def __init__(self, viewKey, loadMode=..., parent=None):
        ...
    def __repr__(self):
        ...
    def __hash__(self):
        ...
    def __eq__(self, other):
        ...
    @property
    def uiImpl(self):
        ...
    @property
    def viewKey(self):
        ...
    @property
    def loadMode(self):
        ...
    @property
    def parent(self):
        ...

class SFViewLoadParams(ViewLoadParams):
    __slots__: tuple
    window: Any
    def __init__(self, alias, name=None, loadMode=..., parent=None):
        ...
    @property
    def uiImpl(self):
        ...

class GuiImplViewLoadParams(ViewLoadParams):
    __slots__: tuple
    __viewClass: Any
    __scope: Any
    def __init__(self, layoutID, viewClass, scope, parent=None):
        ...
    def __hash__(self):
        ...
    def __eq__(self, other):
        ...
    @property
    def uiImpl(self):
        ...
    @property
    def viewClass(self):
        ...
    @property
    def scope(self):
        ...

class LoaderManager(LoaderManagerMeta):
    __guiLoader: Any
    __tutorialLoader: Any
    __eManager: Any
    onViewLoadInit: Any
    onViewLoaded: Any
    onViewLoadError: Any
    onViewLoadCanceled: Any
    __app: Any
    __loadingItems: Any
    def __init__(self, app):
        ...
    def __repr__(self):
        ...
    def loadView(self, loadParams, *args, **kwargs):
        ...
    def cancelLoading(self, key):
        ...
    def getViewLoadingItem(self, key):
        ...
    def isViewLoading(self, key):
        ...
    def viewLoaded(self, alias, viewName, view):
        ...
    def viewLoadCanceled(self, alias, viewName):
        ...
    def viewLoadError(self, alias, viewName, text):
        ...
    def viewInitializationError(self, alias, viewName):
        ...
    def isModalViewLoading(self):
        ...
    def _dispose(self):
        ...
    def __handleViewDispose(self, view):
        ...
    def __handleViewLoaded(self, view):
        ...
    def __doLoadSFView(self, loadParams, *args, **kwargs):
        ...
    def __onWulfViewLoaded(self, pyEntity):
        ...
    def __onWulfViewLoadError(self, pyEntity):
        ...
    def __doLoadGuiImplView(self, loadParams, fadeParams, *args, **kwargs):
        ...
