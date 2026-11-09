# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/tutorial/settings.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
from future.utils import viewitems as viewitems
from soft_exception import SoftException as SoftException
TUTORIAL_VERSION = '0.4.0'
DOC_DIRECTORY = 'scripts/tutorial_docs'
BONUSES_REFS_FILE_PATH: Any
_SettingsDesc: Any
_ClassPath: Any
TUTORIAL_LOBBY_DISPATCHER: Any
TUTORIAL_BATTLE_DISPATCHER: Any
TUTORIAL_DESCRIPTOR_PARSER: Any
TUTORIAL_CHAPTER_PARSER: Any

class INITIAL_FLAG(object):
    GUI_LOADED = 1
    CHAPTER_RESOLVED = 2
    INITIALIZED: Any

class TUTORIAL_SETTINGS(object):
    SALES_TRIGGERS: Any

class _SettingsCollection(dict):
    def init(self, clazz):
        ...
    def getSettings(self, settingsID):
        ...

def createSettingsCollection():
    ...
def createTutorialElement(classPath, init=None):
    ...
