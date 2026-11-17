# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/collector20_reward/packers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import logging as logging
from gui.impl import backport as backport
from gui.impl.backport import createTooltipData as createTooltipData
from gui.impl.gen import R as R
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.shared.missions.packers.bonus import BonusUIPacker as BonusUIPacker, DOSSIER_ACHIEVEMENT_POSTFIX as DOSSIER_ACHIEVEMENT_POSTFIX, DOSSIER_BADGE_ICON_PREFIX as DOSSIER_BADGE_ICON_PREFIX, DOSSIER_BADGE_POSTFIX as DOSSIER_BADGE_POSTFIX, DossierBonusUIPacker as DossierBonusUIPacker, getDefaultBonusPackersMap as getDefaultBonusPackersMap
from gui.impl.backport import TooltipData as TooltipData
from gui.server_events.bonuses import DossierBonus as DossierBonus
_logger: Any

class Collector20DossierBonusUIPacker(DossierBonusUIPacker):
    _REWARD_ORDER: tuple
    @classmethod
    def _getBadgeTooltip(cls, bonus):
        ...
    @classmethod
    def _getToolTip(cls, bonus):
        ...
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def _packBadges(cls, bonus):
        ...
    @classmethod
    def _packSingleAchievement(cls, achievement, bonus):
        ...
    @classmethod
    def __applyPackMethodsInOrder(cls, bonus, methodMapping):
        ...
    @staticmethod
    def __getSortedBadges(bonus):
        ...

def getCollector20RewardsBonusPacker():
    ...
