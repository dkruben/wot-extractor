# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/views/progression_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from battle_royale.gui.impl.gen.view_models.views.lobby.views.progression.progress_level_model import ProgressLevelModel as ProgressLevelModel
from battle_royale.gui.impl.gen.view_models.views.lobby.views.progression.progression_view_model import ProgressionViewModel as ProgressionViewModel, ProgressionState as ProgressionState
from battle_royale.gui.impl.lobby.br_helpers.utils import setEventInfo as setEventInfo
from battle_royale.gui.impl.lobby.tooltips.proxy_currency_tooltip_view import ProxyCurrencyTooltipView as ProxyCurrencyTooltipView
from battle_royale.gui.impl.lobby.views.bonus_packer import getBonusPacker as getBonusPacker
from battle_royale.gui.impl.lobby.views.quests_packer import getEventUIDataPacker as getEventUIDataPacker
from battle_royale.skeletons.game_controller import IBRProgressionOnTokensController as IBRProgressionOnTokensController
from frameworks.wulf.view.submodel_presenter import SubModelPresenter as SubModelPresenter
from gui.Scaleform.daapi.view.common.battle_royale.br_helpers import sortQuestsByProgressionPointBonus as sortQuestsByProgressionPointBonus
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.battle_pass.battle_pass_bonuses_packers import packBonusModelAndTooltipData as packBonusModelAndTooltipData
from gui.impl.backport import createTooltipData as createTooltipData
from gui.impl.gen import R as R
from gui.impl.lobby.common.view_wrappers import createBackportTooltipDecorator as createBackportTooltipDecorator
from gui.impl.lobby.missions.missions_helpers import needToUpdateQuestsInModel as needToUpdateQuestsInModel
from gui.impl.lobby.tooltips.additional_rewards_tooltip import AdditionalRewardsTooltip as AdditionalRewardsTooltip
from gui.server_events.events_helpers import EventInfoModel as EventInfoModel
from gui.shared import event_dispatcher as event_dispatcher
from gui.shared.utils.scheduled_notifications import SimpleNotifier as SimpleNotifier
from helpers import dependency as dependency, time_utils as time_utils
from helpers.time_utils import ONE_DAY as ONE_DAY, ONE_MINUTE as ONE_MINUTE, getServerUTCTime as getServerUTCTime
from math_common import round_py2_style_int as round_py2_style_int
from skeletons.gui.game_control import IBattleRoyaleController as IBattleRoyaleController
from skeletons.gui.server_events import IEventsCache as IEventsCache

class ProgressionView(SubModelPresenter):
    battleRoyale: Any
    brProgression: Any
    eventsCache: Any
    _UPDATE_TIMER_DELAY = ONE_MINUTE
    __slots__: tuple
    __tooltipData: Any
    __notifier: Any
    __bonuses: Any
    def __init__(self, viewModel, parentView):
        ...
    @property
    def viewModel(self):
        ...
    def getParentWindow(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    # decorador original: @createBackportTooltipDecorator(...)
    def createToolTip(self, event):
        ...
    def getTooltipData(self, event):
        ...
    def initialize(self, *args, **kwargs):
        ...
    def finalize(self):
        ...
    def _getEvents(self):
        ...
    def __restartNotifier(self, updateTime):
        ...
    def __stopNotification(self):
        ...
    def __onClose(self):
        ...
    def __updateQuestTimer(self):
        ...
    def __updateMissionVisitedArray(self, missionVisitedArray, questsIDs):
        ...
    def __onSyncCompleted(self, *_):
        ...
    def __updateProgressionPoints(self):
        ...
    def __updateModel(self):
        ...
    def __onPollServerTime(self):
        ...
    def __updateProgression(self, data, pointsData, model):
        ...
    def __updateBattleQuestsCards(self, battleQuestsModel, data):
        ...
    def __setBattleQuestTimeLeft(self, battleQuestsModel):
        ...
    def __markAsVisited(self, data):
        ...
    def __updateBattleQuestsIfNeeded(self, battleQuestsModel):
        ...
