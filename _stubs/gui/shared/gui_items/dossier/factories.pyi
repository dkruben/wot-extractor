# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/gui_items/dossier/factories.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems
import nations as nations
from dossiers2.ui.achievements import ACHIEVEMENT_TYPE as ACHIEVEMENT_TYPE, getType as getAchieveType, ACHIEVEMENT_BLOCK as _AB, RARE_STORAGE_RECORD as RARE_STORAGE_RECORD, HONORED_RANK_RECORD as HONORED_RANK_RECORD
from gui.shared.gui_items.dossier import achievements as _as
from gui.shared.gui_items.dossier.achievements import abstract as _abstract_achievements
from gui.shared.gui_items.dossier.achievements.loyal_service import LoyalServiceAchievement as LoyalServiceAchievement
_ACHIEVEMENTS_BY_BLOCK: dict
_ACHIEVEMENTS_BY_TYPE: dict
_ACHIEVEMENTS_BY_NAME: dict

class _AchieveFactory(object):
    _achieveClass: Any
    _name: Any
    _block: Any
    _dossier: Any
    def __init__(self, achieveClass, name, block, dossier):
        ...
    def getName(self):
        ...
    def getBlock(self):
        ...
    def getDossier(self):
        ...
    def getAchieveClass(self):
        ...
    def isInDossier(self):
        ...
    def isValid(self):
        ...
    def create(self, value=None):
        ...
    @classmethod
    def get(cls, achieveClass):
        ...

class _CustomAchieveFactory(_AchieveFactory):
    def create(self, value=None):
        ...
    @classmethod
    def get(cls, achieveClass):
        ...

class _BlockAchieveFactory(_AchieveFactory):
    def create(self, value=None):
        ...
    @classmethod
    def get(cls, achieveClass):
        ...

class _SequenceAchieveFactory(_AchieveFactory):
    def create(self, value=None):
        ...
    @classmethod
    def get(cls, achieveClass):
        ...
    def isInDossier(self):
        ...

class _RareAchievesFactory(_SequenceAchieveFactory):
    def isValid(self):
        ...
    @classmethod
    def get(cls):
        ...

class _NationAchieveFactory(_AchieveFactory):
    _nationID: Any
    def __init__(self, achieveClass, name, nationID, block, dossier):
        ...
    def getNationID(self):
        ...
    def create(self, value=None):
        ...
    @classmethod
    def get(cls, achieveClass, nationID=-1):
        ...

def getAchievementFactory(record, dossier=None):
    ...
