# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/chapter_choice_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.battle_pass.chapter_model import ChapterModel as ChapterModel

class ChapterChoiceViewModel(ViewModel):
    __slots__: tuple
    onPreviewClick: Any
    onChapterSelect: Any
    onAboutClick: Any
    onPointsInfoClick: Any
    onBuyClick: Any
    onViewLoaded: Any
    onClose: Any
    onShowPostProgression: Any
    showTankmen: Any
    def __init__(self, properties=5, commands=9):
        ...
    def getChapters(self):
        ...
    def setChapters(self, value):
        ...
    @staticmethod
    def getChaptersType():
        ...
    def getSelectedChapter(self):
        ...
    def setSelectedChapter(self, value):
        ...
    def getFreePoints(self):
        ...
    def setFreePoints(self, value):
        ...
    def getSeasonNum(self):
        ...
    def setSeasonNum(self, value):
        ...
    def getIsPostProgressionUnlocked(self):
        ...
    def setIsPostProgressionUnlocked(self, value):
        ...
    def _initialize(self):
        ...
