# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/gui_items/dossier/achievements/simple_progress_achvs.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB
from dossiers2.custom.cache import getCache as getDossiersCache
from dossiers2.custom.collector20 import getCollector20Config as getCollector20Config
from dossiers2.custom.helpers import getCollector20Requirements as getCollector20Requirements
from gui.shared.gui_items.dossier.achievements.abstract import SimpleProgressAchievement as SimpleProgressAchievement
from gui.shared.gui_items.dossier.achievements.abstract.mixins import Deprecated as Deprecated, HasVehiclesList as HasVehiclesList

class BeasthunterAchievement(SimpleProgressAchievement):
    __slots__: tuple
    def __init__(self, dossier, value=None):
        ...
    def getNextLevelInfo(self):
        ...
    def _readProgressValue(self, dossier):
        ...

class BruteForceAchievement(SimpleProgressAchievement):
    __slots__: tuple
    def __init__(self, dossier, value=None):
        ...
    def _readProgressValue(self, dossier):
        ...

class CrucialShotAchievement(SimpleProgressAchievement):
    __slots__: tuple
    def __init__(self, dossier, value=None):
        ...
    def _readProgressValue(self, dossier):
        ...

class InfiltratorAchievement(SimpleProgressAchievement):
    __slots__: tuple
    def __init__(self, dossier, value=None):
        ...
    def _readProgressValue(self, dossier):
        ...

class GeniusForWarAchievement(SimpleProgressAchievement):
    __slots__: tuple
    def __init__(self, dossier, value=None):
        ...
    def _readProgressValue(self, dossier):
        ...

class GuerrillaAchievement(SimpleProgressAchievement):
    __slots__: tuple
    def __init__(self, dossier, value=None):
        ...
    def _readProgressValue(self, dossier):
        ...

class HeavyFireAchievement(SimpleProgressAchievement):
    __slots__: tuple
    def __init__(self, dossier, value=None):
        ...
    def _readProgressValue(self, dossier):
        ...

class FightingReconnaissanceAchievement(SimpleProgressAchievement):
    __slots__: tuple
    def __init__(self, dossier, value=None):
        ...
    def _readProgressValue(self, dossier):
        ...

class FireAndSteelAchievement(SimpleProgressAchievement):
    __slots__: tuple
    def __init__(self, dossier, value=None):
        ...
    def _readProgressValue(self, dossier):
        ...

class MousebaneAchievement(SimpleProgressAchievement):
    __slots__: tuple
    def __init__(self, dossier, value=None):
        ...
    def getNextLevelInfo(self):
        ...
    def _readProgressValue(self, dossier):
        ...

class ReliableComradeAchievement(Deprecated, SimpleProgressAchievement):
    __slots__: tuple
    def __init__(self, dossier, value=None):
        ...
    def _readProgressValue(self, dossier):
        ...

class RangerAchievement(SimpleProgressAchievement):
    __slots__: tuple
    def __init__(self, dossier, value=None):
        ...
    def _readProgressValue(self, dossier):
        ...

class PrematureDetonationAchievement(SimpleProgressAchievement):
    __slots__: tuple
    def __init__(self, dossier, value=None):
        ...
    def _readProgressValue(self, dossier):
        ...

class PromisingFighterAchievement(SimpleProgressAchievement):
    __slots__: tuple
    def __init__(self, dossier, value=None):
        ...
    def _readProgressValue(self, dossier):
        ...

class PattonValleyAchievement(SimpleProgressAchievement):
    __slots__: tuple
    def __init__(self, dossier, value=None):
        ...
    def _readProgressValue(self, dossier):
        ...

class PyromaniacAchievement(SimpleProgressAchievement):
    __slots__: tuple
    def __init__(self, dossier, value=None):
        ...
    def _readProgressValue(self, dossier):
        ...

class SentinelAchievement(SimpleProgressAchievement):
    __slots__: tuple
    def __init__(self, dossier, value=None):
        ...
    def _readProgressValue(self, dossier):
        ...

class SinaiAchievement(SimpleProgressAchievement):
    __slots__: tuple
    def __init__(self, dossier, value=None):
        ...
    def _readProgressValue(self, dossier):
        ...

class TankwomenAchievement(SimpleProgressAchievement):
    __slots__: tuple
    def __init__(self, dossier, value=None):
        ...
    def _readProgressValue(self, dossier):
        ...

class WolfAmongSheepAchievement(SimpleProgressAchievement):
    __slots__: tuple
    def __init__(self, dossier, value=None):
        ...
    def _readProgressValue(self, dossier):
        ...

class Collector20Achievement(HasVehiclesList, SimpleProgressAchievement):
    __itemsCache: Any
    _LIST_NAME = 'vehiclesToHaveInGarage'
    _vehTypeCompDescrs: Any
    def __init__(self, name, block, dossier, value=None):
        ...
    def _getVehiclesDescrsList(self):
        ...
    def _readLevelUpTotalValue(self, dossier):
        ...
    def _readLevelUpValue(self, dossier):
        ...
    @classmethod
    def _sortKey(cls, v):
        ...
