# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/dossiers2/common/DossierDescr.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import struct as struct
from array import array as array
from future.utils import viewitems as viewitems
from typing import Dict as Dict, Iterable as Iterable
from dossiers2.common.DossierBlockBuilders import TYPE_BLOCK_BUILDER as TYPE_BLOCK_BUILDER
from dossiers2.custom.records import PLATFORM_ACHIEVEMENTS as PLATFORM_ACHIEVEMENTS

class DossierDescr(object):
    __compDescr: Any
    __headerFormat: Any
    __blocksOffset: Any
    __blocksLayout: Any
    __blocksIndexes: Any
    __blocksBuilders: Any
    __blocks: Any
    _dependentUpdates: Any
    __popUps: Any
    __logRecords: Any
    __blockRemoved: Any
    __version: Any
    __sizes: Any
    def __init__(self, compDescr, blockBuilders, headerFormat):
        ...
    def __getitem__(self, name):
        ...
    def __contains__(self, block):
        ...
    def removeBlock(self, name):
        ...
    def isBlockInLayout(self, block):
        ...
    def expand(self, name):
        ...
    def addPopUp(self, block, record, value, addLogRecord=True):
        ...
    def addLogRecord(self, block, record, value):
        ...
    def popPopUps(self):
        ...
    def popLogRecords(self):
        ...
    def getChanges(self):
        ...
    def checkPlatformAchievements(self, disabledAchievements, oldDossierDescr, revertAchievements):
        ...
    def makeCompDescr(self):
        ...
    def isEmpty(self):
        ...
