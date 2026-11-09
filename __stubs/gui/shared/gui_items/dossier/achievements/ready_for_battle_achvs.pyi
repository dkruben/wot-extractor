# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/gui_items/dossier/achievements/ready_for_battle_achvs.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB
from gui.shared.gui_items.dossier.achievements.abstract import ClassProgressAchievement as ClassProgressAchievement, getCompletedPersonalMissionsCount as getCompletedPersonalMissionsCount
from nations import Alliances as Alliances
from personal_missions import PM_BRANCH as PM_BRANCH, PM3QType as PM3QType

class ReadyForBattleAchievement(ClassProgressAchievement):
    __slots__: tuple
    __name: Any
    __classifier: Any
    __branch: Any
    __isCurrentUserAchievement: Any
    def __init__(self, name, classifier, branch, dossier, value=None):
        ...
    def getNextLevelInfo(self):
        ...
    def _readProgressValue(self, dossier):
        ...
    def _readCurrentProgressValue(self, dossier):
        ...

class ReadyForBattleAchievement3Steps(ReadyForBattleAchievement):
    __slots__: tuple
    MIN_LVL = 3
    NO_LVL = 4

class ReadyForBattleALLAchievement(ReadyForBattleAchievement):
    __slots__: tuple
    def __init__(self, dossier, value=None):
        ...
    def _readCurrentProgressValue(self, dossier):
        ...

class ReadyForBattleAllianceFranceAchievement(ReadyForBattleAchievement3Steps):
    __slots__: tuple
    def __init__(self, dossier, value=None):
        ...

class ReadyForBattleAllianceGermanyAchievement(ReadyForBattleAchievement3Steps):
    __slots__: tuple
    def __init__(self, dossier, value=None):
        ...

class ReadyForBattleAllianceUSAAchievement(ReadyForBattleAchievement3Steps):
    __slots__: tuple
    def __init__(self, dossier, value=None):
        ...

class ReadyForBattleAllianceUSSRAchievement(ReadyForBattleAchievement3Steps):
    __slots__: tuple
    def __init__(self, dossier, value=None):
        ...

class ReadyForBattleATSPGAchievement(ReadyForBattleAchievement):
    __slots__: tuple
    def __init__(self, dossier, value=None):
        ...

class ReadyForBattleHTAchievement(ReadyForBattleAchievement):
    __slots__: tuple
    def __init__(self, dossier, value=None):
        ...

class ReadyForBattleLTAchievement(ReadyForBattleAchievement):
    __slots__: tuple
    def __init__(self, dossier, value=None):
        ...

class ReadyForBattleMTAchievement(ReadyForBattleAchievement):
    __slots__: tuple
    def __init__(self, dossier, value=None):
        ...

class ReadyForBattleSPGAchievement(ReadyForBattleAchievement):
    __slots__: tuple
    def __init__(self, dossier, value=None):
        ...

class ReadyForBattleAssault(ReadyForBattleAchievement3Steps):
    __slots__: tuple
    def __init__(self, dossier, value=None):
        ...

class ReadyForBattleSniper(ReadyForBattleAchievement3Steps):
    __slots__: tuple
    def __init__(self, dossier, value=None):
        ...

class ReadyForBattleSupport(ReadyForBattleAchievement3Steps):
    __slots__: tuple
    def __init__(self, dossier, value=None):
        ...

class ReadyForBattleFossaAssault(ReadyForBattleAchievement3Steps):
    __slots__: tuple
    def __init__(self, dossier, value=None):
        ...

class ReadyForBattleFossaSniper(ReadyForBattleAchievement3Steps):
    __slots__: tuple
    def __init__(self, dossier, value=None):
        ...

class ReadyForBattleFossaSupport(ReadyForBattleAchievement3Steps):
    __slots__: tuple
    def __init__(self, dossier, value=None):
        ...
