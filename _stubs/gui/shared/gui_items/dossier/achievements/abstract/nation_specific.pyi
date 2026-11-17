# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/gui_items/dossier/achievements/abstract/nation_specific.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from past.builtins import cmp as cmp
from dossiers2.custom import cache as cache
from dossiers2.custom.cache import getCache as getDossiersCache
from gui import nationSortKeyByIndex as nationSortKeyByIndex
from gui.shared.gui_items.dossier.achievements.abstract.simple_progress import SimpleProgressAchievement as SimpleProgressAchievement

class NationSpecificAchievement(SimpleProgressAchievement):
    __slots__: tuple
    _NATIONAL_VEHICLES = 'vehiclesInTreesByNation'
    _LIST_NAME = ''
    _nationID: Any
    def __init__(self, namePrefix, nationID, block, dossier, value=None):
        ...
    def getNationID(self):
        ...
    @classmethod
    def getVehiclesListTitle(cls):
        ...
    @classmethod
    def makeFullName(cls, name, nationID):
        ...
    def _readValue(self, dossier):
        ...
    def _readLevelUpTotalValue(self, dossier):
        ...
    @classmethod
    def _getAllSuitableVehicles(cls):
        ...
    def _getDoneStatus(self, dossier):
        ...
    def _compare(self, other):
        ...
