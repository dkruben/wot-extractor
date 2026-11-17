# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/view_helpers/blur_manager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
import weakref as weakref
from future.utils import listvalues as listvalues
from math import isnan as isnan
import GUI as GUI
from collections import deque as deque
from gui.app_loader.settings import APP_NAME_SPACE as _SPACE
from helpers import dependency as dependency
from ids_generators import Int32IDGenerator as Int32IDGenerator
from shared_utils import findFirst as findFirst
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.game_control import IBlurEffect as IBlurEffect, IBlurController as IBlurController
from Math import Vector4 as Vector4
_DEFAULT_BLUR_ANIM_REPEAT_COUNT = 10
_DEFAULT_UI_BLUR_RADIUS = 20
_logger: Any
_idsGenerator: Any

class BlurEffect(IBlurEffect):
    _blurId: Any
    _config: Any
    _manager: Any
    def __init__(self, manager, config):
        ...
    @property
    def blurId(self):
        ...
    def fini(self):
        ...
    def enable(self):
        ...
    def disable(self):
        ...
    @property
    def config(self):
        ...
    def updateConfig(self, config):
        ...

class BlurManager(object):
    _cache: Any
    def __init__(self):
        ...
    def fini(self):
        ...
    def clear(self):
        ...
    def registerBlur(self, blur):
        ...
    def unregisterBlur(self, blur):
        ...
    def updateBlur(self, blur):
        ...
    def _activeBlur(self):
        ...
    def _findBlurToRestore(self, blurCls):
        ...
    def _validateCache(self):
        ...
    def _isBlurInCache(self, blur):
        ...

class Blur(object):
    @classmethod
    def register(cls, prevBlur, blur):
        ...
    @classmethod
    def unregister(cls, blur, restoredBlur=None):
        ...
    @classmethod
    def getSpecificConfig(cls, config):
        ...
    @classmethod
    def apply(cls, blur):
        ...
    @classmethod
    def disable(cls, blur):
        ...

class ImmediateSceneBlur(Blur):
    @classmethod
    def getSpecificConfig(cls, config):
        ...
    @classmethod
    def apply(cls, blur):
        ...
    @classmethod
    def disable(cls, blur):
        ...

class SceneBlur(Blur):
    _globalBlur: Any
    _rects: Any
    @classmethod
    def unregister(cls, blur, restoredBlur=None):
        ...
    @classmethod
    def getSpecificConfig(cls, config):
        ...
    @classmethod
    def apply(cls, blur):
        ...
    @classmethod
    def disable(cls, blur):
        ...
    @classmethod
    def _clearRects(cls):
        ...

class UILayerBlur(Blur):
    @classmethod
    def getSpecificConfig(cls, config):
        ...
    @classmethod
    def apply(cls, blur):
        ...
    @classmethod
    def disable(cls, blur):
        ...

class ImmediateSceneBlurConfig(object):
    BLUR_CLS = ImmediateSceneBlur
    enabled: Any
    spaceID: Any
    settings: Any
    persistent: Any
    def __init__(self, enabled=False, spaceID=0, settings=None, persistent=False):
        ...

class SceneBlurConfig(object):
    BLUR_CLS = SceneBlur
    enabled: Any
    fadeTime: Any
    blurRadius: Any
    rects: Any
    persistent: Any
    def __init__(self, enabled=False, fadeTime=0, blurRadius=None, rects=None, persistent=False):
        ...

class UILayerBlurConfig(object):
    BLUR_CLS = UILayerBlur
    enabled: Any
    ownLayer: Any
    blurAnimRepeatCount: Any
    uiBlurRadius: Any
    persistent: Any
    def __init__(self, enabled=False, ownLayer=None, blurAnimRepeatCount=..., uiBlurRadius=..., persistent=False):
        ...

class CachedBlur(object):
    __sceneBlurConfig: Any
    __blurConfig: Any
    __rects: Any
    __blur: Any
    def __init__(self, enabled=False, fadeTime=0, ownLayer=None, blurAnimRepeatCount=..., blurRadius=None, uiBlurRadius=...):
        ...
    def fini(self):
        ...
    def enable(self):
        ...
    def disable(self):
        ...
    def addRect(self, blurRect):
        ...
    def changeRect(self, rectId, blurRect):
        ...
    def removeRect(self, rectId):
        ...
    @property
    def config(self):
        ...
    @property
    def enabled(self):
        ...
    def __updateRects(self):
        ...
