# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/CustomEffect.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems
from past.builtins import intern as intern, xrange as xrange
import material_kinds as material_kinds
from items import _xml as _xml
from debug_utils import LOG_ERROR as LOG_ERROR, LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION
from helpers.PixieNode import EffectNode as EffectNode
from helpers import EffectsList as EffectsList
from soft_exception import SoftException as SoftException
gNodes: dict
gEffectLists: dict

class RangeTable(object):
    keys: Any
    values: Any
    def __init__(self, keys, values):
        ...
    def lookup(self, point, defaultValue=None):
        ...

class SelectorDescFactory(object):
    @staticmethod
    def initFactory(section):
        ...
    @staticmethod
    def releseFactory():
        ...
    @staticmethod
    def readEffectLists(dataSection):
        ...
    @staticmethod
    def readNodes(dataSection):
        ...
    @staticmethod
    def create(selectorDesc, effects=None):
        ...

class SelectorDesc(object):
    __slots__: tuple
    _variable: Any
    _isPC: Any
    def __init__(self):
        ...
    def read(self, dataSection, effects):
        ...
    def fillTemplate(self, args, effects):
        ...
    def getActiveEffects(self, effects, args, resetEffectArgs=None):
        ...

class DiscreteSelectorDesc(SelectorDesc):
    __slots__: tuple
    _selectors: Any
    _variable: Any
    @property
    def selectors(self):
        ...
    def __init__(self):
        ...
    def read(self, dataSection, effects):
        ...
    def fillTemplate(self, args, effects):
        ...
    def getActiveEffects(self, effects, args, resetEffectArgs=None):
        ...

class MatkindSelectorDesc(DiscreteSelectorDesc):
    __slots__: tuple
    _variable: Any
    def read(self, dataSection, effects):
        ...

class RangeSelectorDesc(SelectorDesc):
    __slots__: tuple
    _selectors: Any
    __keys: Any
    _variable: Any
    def __init__(self):
        ...
    def read(self, dataSection, effects):
        ...
    def fillTemplate(self, args, effects):
        ...
    def getActiveEffects(self, effects, args, resetEffectArgs=None):
        ...

class UnionSelectorDesc(SelectorDesc):
    __slots__: tuple
    _selectors: Any
    def __init__(self):
        ...
    def read(self, dataSection, effects):
        ...
    def fillTemplate(self, args, effects):
        ...
    def getActiveEffects(self, effects, args, resetEffectArgs=None):
        ...

class EffectSelectorDesc(SelectorDesc):
    __slots__: tuple
    __hardPoint: Any
    _id: Any
    __ttl: Any
    _effectList: Any
    _variable: Any
    @property
    def isEffectList(self):
        ...
    def __init__(self):
        ...
    def read(self, dataSection, effects):
        ...
    def fillTemplate(self, args, effects):
        ...
    def getActiveEffects(self, effects, args, resetEffectArgs=None):
        ...
    def __makeId(self, effects):
        ...
    def __makeIdWithHP(self, effects):
        ...

class EffectListSelectorDesc(EffectSelectorDesc):
    __slots__: tuple
    _effectList: Any
    def __init__(self):
        ...

class EffectDescriptorBase(object):
    __slots__: tuple
    _selectorDesc: Any
    def __init__(self):
        ...
    def getActiveEffects(self, effects, args, resetEffectArgs):
        ...

class CustomEffectsDescriptor(EffectDescriptorBase):
    __slots__: tuple
    __effects: Any
    _selectorDesc: Any
    @staticmethod
    def getDescriptor(dataSection, customDescriptors, xmlCtx, name):
        ...
    @property
    def effects(self):
        ...
    def __init__(self, dataSection):
        ...
    def destroy(self):
        ...
    def create(self, args):
        ...
    def getActiveEffects(self, effects, args, resetEffectArgs):
        ...

class ExhaustEffectDescriptor(EffectDescriptorBase):
    __slots__: tuple
    __descriptors: Any
    nodes: Any
    def __init__(self, dataSection, xmlCtx, customDescriptors, name):
        ...
    @property
    def descriptors(self):
        ...
    @descriptors.setter
    def descriptors(self, value):
        ...
    def create(self, args):
        ...
    def getActiveEffects(self, effects, args, resetEffectArgs):
        ...

class EffectSettings(object):
    SETTINGS_NO = 0
    SETTING_DUST = 1
    SETTING_EXHAUST = 2

class MainSelectorBase(object):
    _activeEffectId: Any
    _effectSelector: Any
    _effectNodes: Any
    _enabled: Any
    @property
    def effectNodes(self):
        ...
    def __init__(self, selectorDesc, args):
        ...
    def destroy(self):
        ...
    def settingsFlags(self):
        ...
    def enable(self, effectID, enable):
        ...
    def start(self):
        ...
    def stop(self):
        ...
    def update(self, args, effectsToReset):
        ...
    def __resetEffects(self, resetEffectArgs):
        ...

class MainCustomSelector(MainSelectorBase):
    _effectNodes: Any
    def __init__(self, selectorDesc, args):
        ...
    def settingsFlags(self):
        ...
    def __createEffects(self, effects, args):
        ...
    def enable(self, effectID, enable):
        ...

class ExhaustMainSelector(MainSelectorBase):
    _effectNodes: Any
    def __init__(self, selectorDesc, args, nodes):
        ...
    def settingsFlags(self):
        ...
    def __createEffects(self, effects, args, nodes):
        ...
    def enable(self, effectID, enable):
        ...

def getEffectList(name):
    ...
def setEffectList(data):
    ...
def makeDescVariable(templateVar, args):
    ...
