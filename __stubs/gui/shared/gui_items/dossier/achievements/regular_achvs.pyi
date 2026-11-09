# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/gui_items/dossier/achievements/regular_achvs.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB
from gui.shared.gui_items.dossier.achievements import validators as validators
from gui.shared.gui_items.dossier.achievements.abstract import RegularAchievement as RegularAchievement
from gui.shared.gui_items.dossier.achievements.abstract.mixins import NoProgressBar as NoProgressBar

class Achieved(RegularAchievement):
    __slots__: tuple
    @classmethod
    def checkIsValid(cls, block, name, dossier):
        ...

class HonoredRankAchievement(RegularAchievement):
    __slots__: tuple
    def __init__(self, dossier, value=None):
        ...
    def getIcons(self):
        ...
    @classmethod
    def checkIsInDossier(cls, block, name, dossier):
        ...
    @classmethod
    def checkIsValid(cls, block, name, dossier):
        ...
    def _readValue(self, dossier):
        ...
    @classmethod
    def __getCount(cls, dossier):
        ...

class MoonSphereAchievement(RegularAchievement, NoProgressBar):
    __slots__: tuple
    def __init__(self, dossier, value=None):
        ...
    @classmethod
    def checkIsValid(cls, block, name, dossier):
        ...

class LumberjackAchievement(RegularAchievement, NoProgressBar):
    __slots__: tuple
    def __init__(self, dossier, value=None):
        ...
    @classmethod
    def checkIsValid(cls, block, name, dossier):
        ...

class ReferralProgramSingleAchievement(RegularAchievement):
    __slots__: tuple
    @classmethod
    def checkIsValid(cls, block, name, dossier):
        ...
