# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/battle_matters/battle_matters_rewards_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from collections import OrderedDict as OrderedDict
import typing as typing
from future.utils import iteritems as iteritems
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags
from gui.impl.backport import BackportTooltipWindow as BackportTooltipWindow
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.battle_matters.battle_matters_rewards_view_model import BattleMattersRewardsViewModel as BattleMattersRewardsViewModel, State as State, RewardType as RewardType
from gui.impl.lobby.battle_matters.battle_matters_constants import SequenceNumber as SequenceNumber
from gui.impl.lobby.battle_matters.tooltips.battle_matters_token_tooltip_view import BattleMattersTokenTooltipView as BattleMattersTokenTooltipView
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.lobby_window import LobbyNotificationWindow as LobbyNotificationWindow
from gui.server_events.bonuses import getNonQuestBonuses as getNonQuestBonuses, getMergedBonusesFromDicts as getMergedBonusesFromDicts
from gui.server_events.events_dispatcher import showBattleMatters as showBattleMatters
from gui.shared.event_dispatcher import showDelayedReward as showDelayedReward, selectVehicleInHangar as selectVehicleInHangar, showHangar as showHangar
from gui.shared.missions.packers.bonus import packMissionsBonusModelAndTooltipData as packMissionsBonusModelAndTooltipData
from gui.impl.lobby.battle_matters.battle_matters_bonus_packer import getBattleMattersBonusPacker as getBattleMattersBonusPacker, bonusesSortKey as bonusesSortKey, blueprintsSortKey as blueprintsSortKey, battleMattersSortKey as battleMattersSortKey
from helpers import dependency as dependency
from sound_gui_manager import CommonSoundSpaceSettings as CommonSoundSpaceSettings
from shared_utils import first as first
from skeletons.gui.battle_matters import IBattleMattersController as IBattleMattersController
from gui.server_events.bonuses import VehiclesBonus as VehiclesBonus, TankmenBonus as TankmenBonus
from frameworks.wulf import ViewEvent as ViewEvent, View as View
from typing import Sequence as Sequence, Tuple as Tuple, Callable as Callable, Optional as Optional
from Event import Event as Event
_logger: Any
_CLIENT_REWARD_IDX = -1

class BattleMattersRewardsView(ViewImpl):
    __slots__: tuple
    _COMMON_SOUND_SPACE: Any
    __battleMattersController: Any
    __cds: Any
    __intermediateQuestID: Any
    __intermediateRewards: Any
    __regularQuestID: Any
    __regularRewards: Any
    __tooltipData: Any
    __questOrder: Any
    __isPairQuest: Any
    __isWithDelayed: Any
    __sequenceNumber: Any
    __delayedReward: Any
    def __init__(self, ctx):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def createToolTip(self, event):
        ...
    def onChooseVehicle(self):
        ...
    def onShowVehicle(self):
        ...
    def onClose(self):
        ...
    def onNextTask(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    @staticmethod
    def __getBonuses(rewards):
        ...
    def __fillVehicles(self, model, vehicles, packer):
        ...
    def __fillIntermediate(self, model, bonuses, packer):
        ...
    def __fillRegular(self, model, bonuses, packer):
        ...
    def __processVehicles(self):
        ...
    def __processDelayedBonuses(self, bonuses):
        ...
    def __getState(self):
        ...
    def __getBackportTooltipData(self, event):
        ...
    def __processBlueprints(self, bonuses):
        ...

class BattleMattersRewardsViewWindow(LobbyNotificationWindow):
    __slots__: tuple
    def __init__(self, parent=None, ctx=None):
        ...
