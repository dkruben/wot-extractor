# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/gui_items/dossier/achievements/mark_of_mastery.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB, MARK_OF_MASTERY as MARK_OF_MASTERY
from gui.shared.gui_items.dossier.achievements.abstract import ClassProgressAchievement as ClassProgressAchievement
from helpers import i18n as i18n
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
MASTERY_IS_NOT_ACHIEVED = 0

class MarkOfMasteryAchievement(ClassProgressAchievement):
    __slots__: tuple
    __prevMarkOfMastery: Any
    __compDescr: Any
    class MARK_OF_MASTERY(CONST_CONTAINER):
        MASTER = 4
        STEP_1 = 3
        STEP_2 = 2
        STEP_3 = 1
    def __init__(self, dossier, value=None):
        ...
    def getMarkOfMastery(self):
        ...
    def getPrevMarkOfMastery(self):
        ...
    def setPrevMarkOfMastery(self, prevMarkOfMastery):
        ...
    def getCompDescr(self):
        ...
    def setCompDescr(self, compDescr):
        ...
    def getIconName(self):
        ...
    def _getUserNameCtx(self):
        ...

def isMarkOfMasteryAchieved(markOfMasterVal):
    ...
