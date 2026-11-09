# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/doc_loaders/GuiColorsLoader.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import listitems as listitems
import Math as Math
import ResMgr as ResMgr
from debug_utils import LOG_ERROR as LOG_ERROR, LOG_WARNING as LOG_WARNING, LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION
from items import _xml as _xml
DEFAULT_SUB_SCHEME = 'default'
COLOR_BLIND_SUB_SCHEME = 'color_blind'
_g_instance = None

class _GuiColorsLoader(object):
    XML_PATH = 'gui/gui_colors.xml'
    DEFAULT_ALIAS_COLOR = None
    DEFAULT_RGBA_COLOR: Any
    DEFAULT_COLOR_OFFSET: Any
    DEFAULT_TRANSFORM_COLOR_MULT: Any
    DEFAULT_TRANSFORM_COLOR_OFFSET = DEFAULT_COLOR_OFFSET
    DEFAULT_ADJUST_OFFSET = DEFAULT_COLOR_OFFSET
    ALIAS = 'alias_color'
    GROUP = 'schemeGroup'
    RGBA = 'rgba'
    MULT = 'mult'
    OFFSET = 'offset'
    TRANSFORM = 'transform'
    ADJUST = 'adjust'
    DEFAULTS: dict
    VECTOR4_NAMES: tuple
    STRING_NAMES: tuple
    DEFAULT_TAG = 'default'
    COLOR_BLIND_TAG = 'color_blind'
    DEFAULT_SCHEME: dict
    __colors: Any
    def __init__(self):
        ...
    def clear(self):
        ...
    def __readXML(self, xmlCtx):
        ...
    def __readHash(self, rootSection):
        ...
    def __overrideTags(self, rootSection, baseHash):
        ...
    def __readColorScheme(self, hashh):
        ...
    def __readVector4(self, section, tagName):
        ...
    def __readString(self, section, tagName):
        ...
    def __readTransformSection(self, section):
        ...
    def __readColorSection(self, section):
        ...
    def __initColorScheme(self, section):
        ...
    def __readFilters(self, section, color_scheme):
        ...
    def load(self):
        ...
    def items(self):
        ...
    def schemasNames(self):
        ...
    def getColorScheme(self, schemeName):
        ...
    def getSubScheme(self, schemeName, group):
        ...
    def getSubSchemeToFlash(self, schemeName, group):
        ...

def load():
    ...
