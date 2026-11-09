# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/helpers/PixieNode.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
from future.utils import viewitems as viewitems, viewvalues as viewvalues
import BigWorld as BigWorld
import Math as Math
from helpers.PixieBG import PixieBG as PixieBG
from helpers.EffectsList import EffectsListPlayer as EffectsListPlayer

class BaseNodeEffect(object):
    __slots__: tuple
    _enabled: Any
    @property
    def enabled(self):
        ...
    def __init__(self):
        ...
    def attach(self):
        ...
    def detach(self):
        ...

class PixieEffect(BaseNodeEffect):
    __slots__: tuple
    __pixieRef: Any
    __effectName: Any
    __ttl: Any
    __node: Any
    __ttlCallback: Any
    _enabled: Any
    def __init__(self, name, node, ttl):
        ...
    def __del__(self):
        ...
    def attach(self):
        ...
    def detach(self):
        ...
    def deactivate(self):
        ...
    def onLoadedCallback(self, pixie, clone):
        ...
    def __attach(self, pixie):
        ...
    def __attachTTL(self, pixie):
        ...
    def __detach(self):
        ...
    def __detachTTL(self):
        ...

class NodeEffectList(BaseNodeEffect):
    __slots__: tuple
    __node: Any
    __model: Any
    __timeLine: Any
    __player: Any
    def __init__(self, name, model, node):
        ...
    def __del__(self):
        ...
    def attach(self):
        ...
    def detach(self):
        ...
    def deactivate(self):
        ...

class EffectNode(object):
    __slots__: tuple
    _PIXIE_NAME = 0
    _PIXIE_ENABLED = 1
    _PIXIE_REF = 2
    _PIXIE_TTL = 3
    EFFECT_ID = 0
    EFFECT_TTL = 1
    EFFECT_LIST = 2
    __node: Any
    __remappedNode: Any
    __nodeName: Any
    __nodeDefaultLocalTranslation: Any
    __drawOrder: Any
    __waterY: Any
    __effects: Any
    @property
    def node(self):
        ...
    @property
    def nodeName(self):
        ...
    def __init__(self, model, nodeName, waterY, drawOrder, effects):
        ...
    def remapNode(self, fromNode, toNode, model):
        ...
    def deactivate(self):
        ...
    def destroy(self):
        ...
    def correctWater(self, waterShiftRel):
        ...
    def enable(self, effectID, enable):
        ...

class PixieCache(object):
    pixieCache: dict
    refCount = 0
    pixiesCount = 0
    @staticmethod
    def getPixie(name, callbackData):
        ...
    @staticmethod
    def incref():
        ...
    @staticmethod
    def decref():
        ...
    @staticmethod
    def onPixieLoaded(pixieBG):
        ...
