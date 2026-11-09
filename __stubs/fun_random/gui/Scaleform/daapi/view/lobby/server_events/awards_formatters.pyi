# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/Scaleform/daapi/view/lobby/server_events/awards_formatters.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from future.utils import viewvalues as viewvalues
from constants import PREMIUM_ENTITLEMENTS as PREMIUM_ENTITLEMENTS
from fun_random.gui.feature.util.fun_mixins import FunAssetPacksMixin as FunAssetPacksMixin
from fun_random.gui.impl.lobby.common.lootboxes import FunRandomLootBoxTypes as FunRandomLootBoxTypes, sortTokenFunc as sortTokenFunc
from gui.Scaleform.daapi.view.lobby.missions.awards_formatters import CurtailingAwardsComposer as CurtailingAwardsComposer, formatShortData as formatShortData
from gui.impl import backport as backport
from gui.server_events.awards_formatters import AWARDS_SIZES as AWARDS_SIZES, AwardsPacker as AwardsPacker, getMissionsDefaultFormatterMap as getMissionsDefaultFormatterMap, TokenBonusFormatter as TokenBonusFormatter, UniversalPremiumDaysBonusFormatter as UniversalPremiumDaysBonusFormatter

class FunCurtailingAwardsComposer(CurtailingAwardsComposer):
    @classmethod
    def _getShortBonusesData(cls, preformattedBonuses, size=...):
        ...

class FunRandomLootBoxFormatter(TokenBonusFormatter, FunAssetPacksMixin):
    def _format(self, bonus):
        ...
    def _getLootboxUserName(self, lootBox):
        ...
    def _getLootboxIcon(self, lootBox, size):
        ...
    def _getIconPath(self, rarity):
        ...

class FunRandomRewardLootBoxFormatter(FunRandomLootBoxFormatter):
    def _getIconPath(self, rarity):
        ...

def getFunFormatterMap():
    ...
def getFunSpecialFormatterMap():
    ...
def getFunAwardsPacker(isSpecial=False):
    ...
