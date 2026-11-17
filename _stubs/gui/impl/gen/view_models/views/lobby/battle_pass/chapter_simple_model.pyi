# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/chapter_simple_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import IntEnum as IntEnum
from frameworks.wulf import ViewModel as ViewModel

class ChapterStatus(IntEnum):
    ACTIVE = 0
    PAUSED = 1
    COMPLETED = 2
    NOTSTARTED = 3

class ChapterSimpleModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=4, commands=0):
        ...
    def getChapterID(self):
        ...
    def setChapterID(self, value):
        ...
    def getChapterStatus(self):
        ...
    def setChapterStatus(self, value):
        ...
    def getIsRegular(self):
        ...
    def setIsRegular(self, value):
        ...
    def getIsBattlePassPurchased(self):
        ...
    def setIsBattlePassPurchased(self, value):
        ...
    def _initialize(self):
        ...
