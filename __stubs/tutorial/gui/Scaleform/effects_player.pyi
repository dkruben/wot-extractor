# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/tutorial/gui/Scaleform/effects_player.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from collections import defaultdict as defaultdict
from future.utils import viewitems as viewitems, viewvalues as viewvalues
from helpers import dependency as dependency
from gui.Scaleform.genConsts.TUTORIAL_TRIGGER_TYPES import TUTORIAL_TRIGGER_TYPES as TUTORIAL_TRIGGER_TYPES
from skeletons.tutorial import ITutorialLoader as ITutorialLoader
from tutorial.data.events import GuiEventType as GuiEventType
_logger: Any
_GUI_EVENT_TO_TRIGGER_TYPE: dict
_ACTION_TO_TRIGGER_TYPE: dict

class GUIEffectScope(object):
    COMPONENT = 0
    SCENE = 1

class GUIEffect(object):
    __slots__: tuple
    def clear(self):
        ...
    def play(self, effectData):
        ...
    def stop(self, effectID=None, effectSubType=None):
        ...
    def cancel(self, scopeType, scopeName):
        ...
    def isStillRunning(self, effectID=None, effectSubType=None):
        ...

class ApplicationEffect(GUIEffect):
    __tutorialLoader: Any
    __slots__: tuple
    _app: Any
    def __init__(self):
        ...
    def clear(self):
        ...
    def setApplication(self, app):
        ...
    def _getContainer(self, layer):
        ...
    def _getTutorialLayout(self):
        ...

class ShowChainHint(ApplicationEffect):
    __slots__: tuple
    _hintsDict: Any
    def __init__(self):
        ...
    def isStillRunning(self, effectID=None, effectSubType=None):
        ...
    def play(self, effectData):
        ...
    def stop(self, effectID=None, effectSubType=None):
        ...
    def cancel(self, scopeType, scopeName):
        ...

class ShowOnceOnlyHint(ShowChainHint):
    __slots__: tuple
    def stop(self, effectID=None, effectSubType=None):
        ...

class SetCriteriaEffect(ApplicationEffect):
    __slots__: tuple
    def play(self, effectData):
        ...

class SetTriggerEffect(ApplicationEffect):
    __slots__: tuple
    _triggersByItem: Any
    def __init__(self):
        ...
    def play(self, effectData):
        ...
    def stop(self, effectID=None, effectSubType=None):
        ...

class EffectsPlayer(object):
    __slots__: tuple
    _effects: Any
    def __init__(self, effects):
        ...
    def iterEffects(self):
        ...
    def filterByName(self, *names):
        ...
    def clear(self):
        ...
    def play(self, effectName, effectData):
        ...
    def stop(self, effectName, effectID, effectSubType=None):
        ...
    def cancel(self, scopeType, scopeName):
        ...
    def stopAll(self):
        ...
    def isStillRunning(self, effectName, effectID=None, effectSubType=None):
        ...
