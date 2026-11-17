# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_loading/resources/cdn/history.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import os as os
import typing as typing
from gui.game_loading import loggers as loggers
from gui.game_loading.common import loadDictFromJsonFile as loadDictFromJsonFile, saveDictToJsonFile as saveDictToJsonFile, deleteFile as deleteFile
from gui.game_loading.resources.cdn.config import createSequenceModel as createSequenceModel, dumpSequenceModel as dumpSequenceModel
from web.cache.web_cache import generateKey as generateKey
from gui.game_loading.resources.cdn.types import SequenceType as SequenceType, SlideType as SlideType
from gui.game_loading.resources.cdn.models import ConfigSequenceModel as ConfigSequenceModel
_logger: Any
_g_viewHistory = None

class ViewHistory(object):
    __slots__: tuple
    _filePath: Any
    _history: Any
    _selectedSequence: Any
    _changed: Any
    def __init__(self, filePath):
        ...
    def load(self):
        ...
    def save(self):
        ...
    def delete(self):
        ...
    @property
    def selectedSequence(self):
        ...
    def selectSequence(self, sequence):
        ...
    def deleteSelectedSequence(self):
        ...
    def getSequenceViewsCount(self, sequence):
        ...
    def getSequenceSlideViewsCount(self, sequence, slide):
        ...
    def addSequenceSlideViewsCount(self, sequence, slide, count=1):
        ...
    def removeSequenceFromHistory(self, sequence):
        ...
    @property
    def _rawSelectedSequence(self):
        ...
    def __repr__(self):
        ...

def getOrCreateViewHistory(dirPath):
    ...
def saveViewHistory():
    ...
