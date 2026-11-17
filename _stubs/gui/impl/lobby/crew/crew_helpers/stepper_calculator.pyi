# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/crew_helpers/stepper_calculator.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from math import ceil as ceil
from helpers import dependency as dependency
from items.tankmen import MAX_SKILL_LEVEL as MAX_SKILL_LEVEL
from gui.impl.lobby.crew.crew_helpers.skill_helpers import getSkillsLevelsForXp as getSkillsLevelsForXp
from skeletons.gui.shared import IItemsCache as IItemsCache

class FreeXpStepperCalculator(object):
    itemsCache: Any
    _currentTankman: Any
    _exchangeRate: Any
    _currentSkillsCount: Any
    _currentSkillLevel: Any
    _possibleSkillsCount: Any
    _possibleSkillLevel: Any
    _aquiringPersonalXpAmount: Any
    def __init__(self, exchangeRate):
        ...
    def setCurrentTankman(self, tankman):
        ...
    def setInitialPossibleValues(self):
        ...
    def setManualInputPossibleValues(self, possibleCount, possibleLevel):
        ...
    def setAquiringPersonalXp(self, value):
        ...
    def getLevelUpXpCost(self):
        ...
    def getLevelDownXpCost(self):
        ...
    def getSkillUpXpCost(self):
        ...
    def getSkillDownXpCost(self):
        ...
    def getMaxPossibleValue(self):
        ...
    def _countResultAndConvertToFreeXp(self):
        ...
    def __convertToFreeXp(self, value):
        ...
