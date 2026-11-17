# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/meta_view/pages/rank_rewards_page.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from collections import namedtuple as namedtuple
from functools import partial as partial
from future.utils import lzip as lzip
from shared_utils import first as first
from comp7.gui.impl.gen.view_models.views.lobby.enums import MetaRootViews as MetaRootViews, Rank as Rank
from comp7.gui.impl.gen.view_models.views.lobby.meta_view.pages.rank_rewards_item_model import RankRewardsItemModel as RankRewardsItemModel
from comp7.gui.impl.gen.view_models.views.lobby.meta_view.pages.rank_rewards_model import RankRewardsModel as RankRewardsModel
from comp7.gui.impl.lobby.comp7_helpers import comp7_model_helpers as comp7_model_helpers, comp7_shared as comp7_shared
from comp7.gui.impl.lobby.comp7_helpers.comp7_bonus_packer import packRanksRewardsQuestBonuses as packRanksRewardsQuestBonuses
from comp7.gui.impl.lobby.comp7_helpers.comp7_c11n_helpers import getStylePreviewVehicle as getStylePreviewVehicle, getPreviewOutfit as getPreviewOutfit
from comp7.gui.impl.lobby.comp7_helpers.comp7_quest_helpers import parseComp7RanksQuestID as parseComp7RanksQuestID, parseComp7PeriodicQuestID as parseComp7PeriodicQuestID, isComp7VisibleQuest as isComp7VisibleQuest, parseQuestsByDivision as parseQuestsByDivision
from comp7.gui.impl.lobby.meta_view.meta_view_helper import setProgressionItemData as setProgressionItemData, getRankDivisions as getRankDivisions
from comp7.gui.impl.lobby.meta_view.pages import PageSubModelPresenter as PageSubModelPresenter
from comp7.gui.impl.lobby.tooltips.fifth_rank_tooltip import FifthRankTooltip as FifthRankTooltip
from comp7.gui.impl.lobby.tooltips.general_rank_tooltip import GeneralRankTooltip as GeneralRankTooltip
from comp7.gui.impl.lobby.tooltips.sixth_rank_tooltip import SixthRankTooltip as SixthRankTooltip
from comp7.gui.shared import event_dispatcher as comp7_events
from comp7_common_const import Comp7QuestType as Comp7QuestType
from gui.impl.backport import BackportTooltipWindow as BackportTooltipWindow
from gui.impl.gen import R as R
from gui.impl.gui_decorators import args2params as args2params
from gui.impl.lobby.tooltips.additional_rewards_tooltip import AdditionalRewardsTooltip as AdditionalRewardsTooltip
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from helpers import dependency as dependency
from items.vehicles import makeVehicleTypeCompDescrByName as makeVehicleTypeCompDescrByName
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from skeletons.gui.game_control import IComp7Controller as IComp7Controller
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared import IItemsCache as IItemsCache
from comp7_ranks_common import Comp7Division as Comp7Division
from comp7.gui.impl.gen.view_models.views.lobby.comp7_style_bonus_model import Comp7StyleBonusModel as Comp7StyleBonusModel
from comp7.gui.impl.gen.view_models.views.lobby.qualification_model import QualificationModel as QualificationModel
from gui.server_events.event_items import TokenQuest as TokenQuest
from comp7.helpers.comp7_server_settings import Comp7RanksConfig as Comp7RanksConfig
_logger: Any
_BonusData: Any
_DEFAULT_PREVIEW_VEHICLE = 'uk:GB91_Super_Conqueror'

class RankRewardsPage(PageSubModelPresenter):
    __slots__: tuple
    __itemsCache: Any
    __c11nService: Any
    __eventsCache: Any
    __comp7Controller: Any
    __rankQuests: Any
    __periodicQuests: Any
    __bonusData: Any
    __itemIndex: Any
    def __init__(self, viewModel, parentView):
        ...
    @property
    def pageId(self):
        ...
    @property
    def viewModel(self):
        ...
    @property
    def ranksConfig(self):
        ...
    @property
    def itemIndex(self):
        ...
    def createToolTip(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def initialize(self, **params):
        ...
    def finalize(self):
        ...
    def _getEvents(self):
        ...
    def __updateQuests(self):
        ...
    def __setRanksData(self, model):
        ...
    def __setRank(self, itemModel, rank):
        ...
    def __setRankRewards(self, itemModel, division):
        ...
    def __setQualificationState(self, qualificationModel):
        ...
    def __onEventsSyncCompleted(self):
        ...
    def __onRanksConfigChanged(self):
        ...
    def __onRankUpdated(self, *_, **__):
        ...
    def __onQualificationStateUpdated(self):
        ...
    # decorador original: @args2params(...)
    def __onPreviewOpen(self, rank, index):
        ...
    @staticmethod
    def __setRewards(itemModel, bonusData):
        ...
