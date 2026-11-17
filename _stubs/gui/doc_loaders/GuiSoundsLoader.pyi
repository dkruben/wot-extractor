# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/doc_loaders/GuiSoundsLoader.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import ResMgr as ResMgr
from debug_utils import LOG_WARNING as LOG_WARNING
from items import _xml as _xml
from gui import doc_loaders as doc_loaders
import WWISE as WWISE
DEFAULT_GUI_SOUND_BANK = 'gui.bnk'
UNKNOWN_SOUND_BANK = ''

class GuiSoundsLoader(object):
    XML_PATH = 'gui/gui_sounds.xml'
    CONTROLS = 'controls'
    CONTROLS_DEFAULT = 'default'
    CONTROLS_SCHEMAS = 'schemas'
    CONTROLS_OVERRIDES = 'overrides'
    SCHEMA_SOUNDS = 'sounds'
    SCHEMA_GROUPS = 'groups'
    EFFECTS = 'effects'
    __schemas: Any
    __groups: Any
    __overrides: Any
    __default: Any
    __effects: Any
    def __init__(self):
        ...
    def __readControlsSounds(self, xmlCtx):
        ...
    def __readEffectsSounds(self, xmlCtx):
        ...
    def load(self):
        ...
    def getControlSound(self, controlType, state, controlID=None):
        ...
    def getEffectSound(self, effectName):
        ...
