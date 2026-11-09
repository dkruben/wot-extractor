# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/framework/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from collections import namedtuple as namedtuple
from frameworks.wulf import WindowLayer as WindowLayer
import gui.Scaleform.framework.ScopeTemplates
from gui.Scaleform.framework.settings import UIFrameworkImpl as UIFrameworkImpl

class COMMON_VIEW_ALIAS(object):
    LOGIN = 'login'
    LOBBY = 'lobby'
    BATTLE = 'battle'
    CURSOR = 'cursor'
    WAITING = 'waiting'

# base nao representavel no stub: namedtuple(...)
class GroupedViewSettings:
    def getDAAPIObject(self):
        ...
    def replaceSettings(self, settings):
        ...
    def toImmutableSettings(self):
        ...

class ViewSettings(GroupedViewSettings):
    @staticmethod
    def __new__(cls, alias, clazz, url, layer, event, scope, cacheable, containers, canDrag, canClose, isModal, isCentered, flags):
        ...

class ComponentSettings(GroupedViewSettings):
    @staticmethod
    def __new__(cls, alias, clazz, scope):
        ...

# base nao representavel no stub: namedtuple(...)
class ContainerSettings:
    ...

def getSwfExtensionUrl(extension, swf):
    ...
