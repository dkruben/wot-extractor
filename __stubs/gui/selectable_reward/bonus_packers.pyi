# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/selectable_reward/bonus_packers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.battle_pass.battle_pass_helpers import getOfferTokenByGift as getOfferTokenByGift
from gui.impl.backport import TooltipData as TooltipData
from gui.shared.missions.packers.bonus import BACKPORT_TOOLTIP_CONTENT_ID as BACKPORT_TOOLTIP_CONTENT_ID, BaseBonusUIPacker as BaseBonusUIPacker
from helpers import dependency as dependency
from shared_utils import first as first
from skeletons.gui.offers import IOffersDataProvider as IOffersDataProvider
from typing import List as List, Union as Union
from account_helpers.offers.events_data import OfferEventData as OfferEventData
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel as BonusModel
from gui.impl.gen.view_models.views.lobby.battle_pass.reward_item_model import RewardItemModel as RewardItemModel
from gui.server_events.bonuses import SelectableBonus as SelectableBonus

class SelectableBonusPacker(BaseBonusUIPacker):
    __offersProvider: Any
    @classmethod
    def getValue(cls, bonus):
        ...
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def _packSingleBonus(cls, bonus):
        ...
    @classmethod
    def _makeRewardItemModel(cls):
        ...
    @classmethod
    def _getToolTip(cls, bonus):
        ...
    @classmethod
    def _getTooltipSpecialAlias(cls):
        ...
    @classmethod
    def _getContentId(cls, bonus):
        ...
    @classmethod
    def __getBonusOffer(cls, bonus):
        ...
