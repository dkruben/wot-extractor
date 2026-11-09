# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/selectable_reward/common.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from future.utils import viewitems as viewitems, viewvalues as viewvalues
from comp7.gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as COMP7_TOOLTIPS
from comp7.gui.selectable_reward.constants import Features as Features
from gui.impl.backport import TooltipData as TooltipData
from gui.selectable_reward.common import SelectableRewardManager as SelectableRewardManager
from helpers import dependency as dependency
from shared_utils import first as first
from skeletons.gui.offers import IOffersDataProvider as IOffersDataProvider
from gui.server_events.bonuses import SelectableBonus as SelectableBonus
from typing import Dict as Dict
_logger: Any

class Comp7SelectableRewardManager(SelectableRewardManager):
    _FEATURE = Features.COMP7
    _offersDataProvider: Any
    @classmethod
    def getTabTooltipData(cls, selectableBonus):
        ...
    @classmethod
    def getGiftCount(cls, bonus):
        ...
    @classmethod
    def getGiftCountPerToken(cls, bonus):
        ...
    @classmethod
    def getBonusOfferToken(cls, bonus):
        ...
    @classmethod
    def __getTokenGiftCount(cls, token, count):
        ...
