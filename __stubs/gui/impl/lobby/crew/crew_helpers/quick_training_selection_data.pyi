# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/crew_helpers/quick_training_selection_data.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from typing import Dict as Dict
from gui.shared.gui_items.crew_book import CrewBook as CrewBook
COUNT_KEY = 'count'
IS_PERSONAL_KEY = 'isPersonal'

class QuickTrainingSelectionData(object):
    __slots__: tuple
    _freeXP: Any
    _selectedBooks: Any
    _preSelectedFreeXp: Any
    _aquiringCommonXp: Any
    _aquiringPersonalXp: Any
    _preSelectedCommonXp: Any
    _preSelectedPersonalXp: Any
    _preSelectedBookId: Any
    def __init__(self):
        ...
    @property
    def books(self):
        ...
    @property
    def freeXp(self):
        ...
    @freeXp.setter
    def freeXp(self, value):
        ...
    @property
    def preSelectedFreeXp(self):
        ...
    @property
    def hasAnyBook(self):
        ...
    @property
    def hasPersonalBook(self):
        ...
    @property
    def hasCommonBook(self):
        ...
    def isBookPreSelecteed(self, bookId):
        ...
    def getAcquiringBooksXpValues(self):
        ...
    def getAllAquiringBooksXpValue(self):
        ...
    def getPersonalBookId(self):
        ...
    def setBook(self, book, count):
        ...
    def setFreeXpFromPreSelected(self):
        ...
    def setPreSelectedFreeXp(self, freeXp):
        ...
    def setPreSelectedBook(self, book):
        ...
    def getBookCountById(self, bookId):
        ...
    def clear(self):
        ...
    def clearPreSelected(self):
        ...
