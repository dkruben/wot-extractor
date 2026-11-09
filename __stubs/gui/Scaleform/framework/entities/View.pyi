# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/framework/entities/View.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
import BigWorld as BigWorld
from collections import namedtuple as namedtuple
from gui.Scaleform.framework.settings import UIFrameworkImpl as UIFrameworkImpl
from gui.Scaleform.framework.entities.DisposableEntity import EntityState as EntityState
from gui.Scaleform.framework.entities.abstract.AbstractViewMeta import AbstractViewMeta as AbstractViewMeta
from gui.Scaleform.framework.entities.view_interface import ViewInterface as ViewInterface
from gui.doc_loaders import hints_layout as hints_layout
from gui.shared.events import FocusEvent as FocusEvent
from ids_generators import SequenceIDGenerator as SequenceIDGenerator
from skeletons.tutorial import ITutorialLoader as ITutorialLoader
from soft_exception import SoftException as SoftException
from sound_gui_manager import ViewSoundExtension as ViewSoundExtension
from helpers import dependency as dependency, uniprof as uniprof
from frameworks.wulf import Window as Window
from gui.sounds.ViewSoundManager import _ViewSoundsManager as _ViewSoundsManager
_logger: Any
_view_id_generator: Any
_ViewKey: Any

class ViewKey(_ViewKey):
    @staticmethod
    def __new__(cls, alias, name=None):
        ...
    def __repr__(self):
        ...
    def __hash__(self):
        ...
    def __eq__(self, other):
        ...

class ViewKeyDynamic(ViewKey):
    def __hash__(self):
        ...
    def __eq__(self, other):
        ...

class View(AbstractViewMeta, ViewInterface):
    _COMMON_SOUND_SPACE = None
    __tutorialLoader: Any
    __settings: Any
    __uid: Any
    __key: Any
    __soundExtension: Any
    __scope: Any
    __window: Any
    def __init__(self, *args, **kwargs):
        ...
    def __repr__(self):
        ...
    def __del__(self):
        ...
    @property
    def uiImpl(self):
        ...
    @property
    def settings(self):
        ...
    @property
    def layer(self):
        ...
    @property
    def viewScope(self):
        ...
    @property
    def key(self):
        ...
    @property
    def alias(self):
        ...
    @property
    def uniqueName(self):
        ...
    @property
    def soundManager(self):
        ...
    def isViewModal(self):
        ...
    def getUniqueName(self):
        ...
    def getSubContainersSettings(self):
        ...
    def getCurrentScope(self):
        ...
    def setCurrentScope(self, scope):
        ...
    def setSettings(self, settings):
        ...
    def setUniqueName(self, name):
        ...
    def setupContextHints(self, hintID, hintsArgs=None):
        ...
    def onFocusIn(self, alias):
        ...
    def getParentWindow(self):
        ...
    def setParentWindow(self, window):
        ...
    def isVisible(self):
        ...
    def canBeClosed(self):
        ...
    def initSoundManager(self, soundSpace):
        ...
    def _populate(self):
        ...
    def _destroy(self):
        ...
