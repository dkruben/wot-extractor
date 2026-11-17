# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/messenger/formatters/loot_box_auto_open_subformatters.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import listitems as listitems, viewitems as viewitems
from adisp import adisp_async as adisp_async, adisp_process as adisp_process
from fun_random.gui.Scaleform.daapi.view.lobby.server_events.awards_formatters import getFunAwardsPacker as getFunAwardsPacker
from fun_random.gui.feature.util.fun_mixins import FunAssetPacksMixin as FunAssetPacksMixin
from fun_random.gui.impl.lobby.common.lootboxes import FunRandomLootBoxTypes as FunRandomLootBoxTypes
from fun_random.notification.decorators import FunRandomProgressionStageMessageDecorator as FunRandomProgressionStageMessageDecorator
from gui.Scaleform.daapi.view.lobby.missions.awards_formatters import CurtailingAwardsComposer as CurtailingAwardsComposer
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.loot_box_compensation_tooltip_types import LootBoxCompensationTooltipTypes as LootBoxCompensationTooltipTypes
from gui.impl.lobby.awards.packers import getVehicleUIData as getVehicleUIData
from gui.server_events.awards_formatters import AWARDS_SIZES as AWARDS_SIZES, LABEL_ALIGN as LABEL_ALIGN
from gui.server_events.bonuses import getNonQuestBonuses as getNonQuestBonuses, LootBoxTokensBonus as LootBoxTokensBonus, getMergedCompensatedBonuses as getMergedCompensatedBonuses, VehiclesBonus as VehiclesBonus
from gui.shared.formatters import text_styles as text_styles
from gui.shared.gui_items.Vehicle import getNationLessName as getNationLessName
from helpers import dependency as dependency
from messenger import g_settings as g_settings
from messenger.formatters.auto_boxes_subformatters import AsyncAutoLootBoxSubFormatter as AsyncAutoLootBoxSubFormatter
from messenger.formatters.service_channel import QuestAchievesFormatter as QuestAchievesFormatter
from messenger.formatters.service_channel_helpers import MessageData as MessageData
from shared_utils import first as first
from skeletons.gui.shared import IItemsCache as IItemsCache
MAX_AWARDS_COUNT = 4
MAIN_REWARD_PADDING = -12
MAIN_REWARD_GAP = -12
SMALL_REWARD_GAP = 5

class FunRandomMessageAwardsComposer(CurtailingAwardsComposer):
    itemsCache: Any
    def _packBonus(self, bonus, size=...):
        ...
    def _packMergedBonuses(self, mergedBonuses, size=...):
        ...
    def __packCompensationData(self, bonus, bonusDict, size):
        ...

class FunRandomLootboxAutoOpenFormatter(AsyncAutoLootBoxSubFormatter, FunAssetPacksMixin):
    __MESSAGE_TEMPLATE = 'FunRandomLootBoxesAutoOpenMessage'
    _achievesFormatter: Any
    def __init__(self):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def format(self, message, callback):
        ...
    @classmethod
    def _isBoxOfThisGroup(cls, boxID):
        ...
    def _collectBonusesData(self, data):
        ...
    def __getRawBonuses(self, rewards):
        ...
