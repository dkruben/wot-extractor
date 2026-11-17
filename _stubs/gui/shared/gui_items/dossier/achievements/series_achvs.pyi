# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/gui_items/dossier/achievements/series_achvs.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB
from gui.shared.gui_items.dossier.achievements.abstract import SeriesAchievement as SeriesAchievement
from gui.shared.gui_items.dossier.achievements.abstract.mixins import Deprecated as Deprecated, Quest as Quest, NoProgressBar as NoProgressBar

class AimerAchievement(NoProgressBar, SeriesAchievement):
    def __init__(self, dossier, value=None):
        ...
    def _getCounterRecordNames(self):
        ...

class ArmorPiercerAchievement(SeriesAchievement):
    __slots__: tuple
    def __init__(self, dossier, value=None):
        ...
    def _getCounterRecordNames(self):
        ...

class DeathTrackAchievement(NoProgressBar, Quest, SeriesAchievement):
    def __init__(self, dossier, value=None):
        ...
    def _getCounterRecordNames(self):
        ...

class DiehardAchievement(SeriesAchievement):
    __slots__: tuple
    def __init__(self, dossier, value=None):
        ...
    def _getCounterRecordNames(self):
        ...

class EFC2016Achievement(Quest, SeriesAchievement):
    def __init__(self, dossier, value=None):
        ...
    def _getCounterRecordNames(self):
        ...

class InvincibleAchievement(SeriesAchievement):
    __slots__: tuple
    def __init__(self, dossier, value=None):
        ...
    def _getCounterRecordNames(self):
        ...

class HandOfDeathAchievement(SeriesAchievement):
    __slots__: tuple
    def __init__(self, dossier, value=None):
        ...
    def _getCounterRecordNames(self):
        ...

class RankedBattlesHeroAchievement(Quest, SeriesAchievement):
    def __init__(self, dossier, value=None):
        ...
    def _getCounterRecordNames(self):
        ...

class TacticalBreakthroughAchievement(SeriesAchievement):
    __slots__: tuple
    def __init__(self, dossier, value=None):
        ...
    def _getCounterRecordNames(self):
        ...

class TitleSniperAchievement(SeriesAchievement):
    __slots__: tuple
    def __init__(self, dossier, value=None):
        ...
    def _getCounterRecordNames(self):
        ...

class VictoryMarchAchievement(Deprecated, NoProgressBar, SeriesAchievement):
    def __init__(self, dossier, value=None):
        ...
    def _getCounterRecordNames(self):
        ...

class VictoryMarchClubAchievement(Deprecated, NoProgressBar, SeriesAchievement):
    def __init__(self, dossier, value=None):
        ...
    def _getCounterRecordNames(self):
        ...

class WFC2014Achievement(Quest, SeriesAchievement):
    def __init__(self, dossier, value=None):
        ...
    def _getCounterRecordNames(self):
        ...
