# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/Scaleform/daapi/view/lobby/tooltips/battle_royale_tooltip_quest_helper.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.Scaleform.genConsts.BLOCKS_TOOLTIP_TYPES import BLOCKS_TOOLTIP_TYPES as BLOCKS_TOOLTIP_TYPES
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.server_events.awards_formatters import AWARDS_SIZES as AWARDS_SIZES, AwardsPacker as AwardsPacker, getEpicSetFormattersMap as getEpicSetFormattersMap, SimpleBonusFormatter as SimpleBonusFormatter, CurrenciesBonusFormatter as CurrenciesBonusFormatter, TokenBonusFormatter as TokenBonusFormatter
from gui.shared.formatters import text_styles as text_styles, icons as icons
from gui.shared.money import Currency as Currency
from gui.shared.tooltips import formatters as formatters

class _BattleRoyaleSimpleFormatter(SimpleBonusFormatter):
    @classmethod
    def _getImages(cls, bonus):
        ...

class _BattleRoyaleCurrenciesFormatter(CurrenciesBonusFormatter):
    @classmethod
    def _getImages(cls, bonus):
        ...

class _BattleRoyaleTokenFormatter(TokenBonusFormatter):
    def _formatBRComplexToken(self, complexToken, token, bonus):
        ...

def getQuestTooltipBlock(quest):
    ...
def _packQuestInfo(quest):
    ...
def _getBattleRoyaleAwardPacker():
    ...
def _getBattleRoyaleFormattersMap():
    ...
def _packQuestRewards(quest):
    ...
def _packQuestReward(bonus):
    ...
