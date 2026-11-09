# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/progressive_reward/progressive_reward_award_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from frameworks.wulf import ViewSettings as ViewSettings
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.impl.auxiliary.rewards_helper import getRewardTooltipContent as getRewardTooltipContent, getRewardRendererModelPresenter as getRewardRendererModelPresenter, BLUEPRINTS_CONGRAT_TYPES as BLUEPRINTS_CONGRAT_TYPES, fillStepsModel as fillStepsModel, getLastCongratsIndex as getLastCongratsIndex
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.progressive_reward.progressive_reward_award_model import ProgressiveRewardAwardModel as ProgressiveRewardAwardModel
from gui.impl.gen.view_models.views.loot_box_view.loot_congrats_types import LootCongratsTypes as LootCongratsTypes
from gui.impl.gen.view_models.views.lobby.blueprints.blueprint_screen_tooltips import BlueprintScreenTooltips as BlueprintScreenTooltips
from gui.impl.lobby.progressive_reward.progressive_award_sounds import setSoundState as setSoundState, ProgressiveRewardSoundEvents as ProgressiveRewardSoundEvents
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.lobby_window import LobbyNotificationWindow as LobbyNotificationWindow
from gui.impl.backport import createTooltipData as createTooltipData, BackportTooltipWindow as BackportTooltipWindow, TooltipData as TooltipData
from gui.Scaleform.daapi.view.lobby.techtree.techtree_dp import g_techTreeDP as g_techTreeDP
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.shared.event_dispatcher import showBlueprintView as showBlueprintView
from helpers import dependency as dependency
from skeletons.gui.server_events import IEventsCache as IEventsCache
_logger: Any

class ProgressiveRewardAwardView(ViewImpl):
    _eventsCache: Any
    __slots__: tuple
    __items: Any
    __bonuses: Any
    __specialRewardType: Any
    __currentStep: Any
    def __init__(self, contentResId, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTip(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _initialize(self, bonuses, specialRewardType, currentStep):
        ...
    def _finalize(self):
        ...
    def __update(self, _=None):
        ...
    def __onWindowClose(self, _=None):
        ...
    def __onDestroy(self, _=None):
        ...
    def __setSteps(self, currentStep):
        ...
    def __setBonuses(self, bonuses):
        ...
    def __onSpecialActionButtonClick(self, responseDict):
        ...
    def __getBackportTooltipData(self, event):
        ...
    def __isEpicReward(self):
        ...

class ProgressiveRewardAwardWindow(LobbyNotificationWindow):
    __slots__: tuple
    def __init__(self, bonuses, specialRewardType, currentStep):
        ...

def _getVehicleCD(value):
    ...
