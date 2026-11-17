# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/gui/messenger/formatters/service_channel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems, viewvalues as viewvalues
from adisp import adisp_async as adisp_async, adisp_process as adisp_process
from constants import SCENARIO_RESULT as SCENARIO_RESULT
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.gui_items import getItemTypeID as getItemTypeID
from gui.shared.gui_items.Vehicle import getUserName as getUserName
from helpers import time_utils as time_utils, dependency as dependency
from items import vehicles as vehicles_core
from messenger import g_settings as g_settings
from messenger.formatters import TimeFormatter as TimeFormatter
from messenger.formatters.service_channel import BattleResultsFormatter as BattleResultsFormatter, ServiceChannelFormatter as ServiceChannelFormatter
from messenger.formatters.service_channel_helpers import MessageData as MessageData
from skeletons.gui.shared import IItemsCache as IItemsCache
from story_mode_common.story_mode_constants import MissionId as MissionId
from story_mode.gui.shared.utils import getRewardList as getRewardList, getTasksCount as getTasksCount
from story_mode.skeletons.story_mode_controller import IStoryModeController as IStoryModeController
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from skeletons.gui.battle_results import IBattleResultsService as IBattleResultsService
from skeletons.gui.game_control import IBattlePassController as IBattlePassController

class StoryModeResultsFormatter(BattleResultsFormatter):
    _storyModeCtrl: Any
    _battleResultsService: Any
    _customizationService: Any
    _battlePass: Any
    _itemsCache: Any
    _battleResultKeys: Any
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def format(self, message, callback):
        ...
    def _prepareFormatData(self, message):
        ...

class StoryModeAwardFormatter(ServiceChannelFormatter):
    __TEMPLATE = 'storyModeAwardMessage'
    def format(self, message, *args):
        ...
