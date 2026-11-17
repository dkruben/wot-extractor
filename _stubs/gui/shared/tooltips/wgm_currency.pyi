# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/tooltips/wgm_currency.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewvalues as viewvalues
from debug_utils import LOG_ERROR as LOG_ERROR
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.impl import backport as backport
from gui.shared.formatters import text_styles as text_styles
from gui.shared.money import Currency as Currency
from gui.shared.tooltips import formatters as formatters
from gui.shared.tooltips.common import DynamicBlocksTooltipData as DynamicBlocksTooltipData
from gui.shared.utils.requesters import wgm_balance_info_requester as wgm_balance_info_requester
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
_WAITING_FOR_DATA = ''
_UNKNOWN_VALUE = '-'

class WGMCurrencyTooltip(DynamicBlocksTooltipData):
    itemsCache: Any
    __requester: Any
    __data: Any
    _btnType: Any
    _hideActionBlock: Any
    def __init__(self, ctx):
        ...
    def getWGMCurrencyValue(self, key):
        ...
    def updateData(self):
        ...
    def stopUpdates(self):
        ...
    def changeVisibility(self, isVisible):
        ...
    @classmethod
    def isWGMAvailable(cls):
        ...
    def _packBlocks(self, btnType=None, hideActionBlock=False, *args, **kwargs):
        ...
    def _getAlternativeData(self):
        ...
    def __onDataResponse(self, data):
        ...
    @staticmethod
    def __checkDiff(d1, d2):
        ...
    def __getValueBlocks(self):
        ...
    def __getGoldString(self, goldType):
        ...
    def __getGoldTotal(self):
        ...
    def __getCreditsString(self, creditsType):
        ...
    def __getCreditsTotal(self):
        ...
