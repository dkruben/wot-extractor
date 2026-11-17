# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/tutorial/doc_loader/gui_config.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
from future.utils import viewitems as viewitems, viewvalues as viewvalues
from operator import getitem as getitem
import resource_helper as resource_helper
from debug_utils import LOG_ERROR as LOG_ERROR
from gui.Scaleform.genConsts.TWEEN_EFFECT_TYPES import TWEEN_EFFECT_TYPES as TWEEN_EFFECT_TYPES
__all__: tuple
_cache: dict
_SceneConfig: Any
_CommandData: Any
_ITEM_TYPE = resource_helper.RESOURCE_ITEM_TYPE

class _ItemConfig(object):
    __slots__: tuple
    __view: Any
    __path: Any
    __padding: Any
    __anim: Any
    __effectBuilders: Any
    def __init__(self, view='', path='', padding=None, anim=None, effectBuilders=None):
        ...
    @property
    def view(self):
        ...
    @property
    def path(self):
        ...
    @property
    def padding(self):
        ...
    @property
    def anim(self):
        ...
    @property
    def effectBuilders(self):
        ...
    @staticmethod
    def _defaultPadding():
        ...
    @staticmethod
    def _defaultAnimConfig():
        ...

class _TutorialConfig(object):
    __slots__: tuple
    __scenes: Any
    __guiItems: Any
    __commands: Any
    def __init__(self, scenes=None, items=None, commands=None):
        ...
    def isEmpty(self):
        ...
    def getSceneID(self, guiPage):
        ...
    def getSceneEvent(self, sceneID):
        ...
    def getItem(self, targetID):
        ...
    def getItems(self):
        ...
    def getCommand(self, commandID):
        ...
    def getCommands(self):
        ...

def readConfig(path, forced=False):
    ...
def clearConfig(path):
    ...
def _getEnumValueByName(name, enum):
    ...
def _listToBitmask(flagNamesList, flagsEnum):
    ...
def _readConfig(ctx, root, parentTag, childTag, itemClass):
    ...
