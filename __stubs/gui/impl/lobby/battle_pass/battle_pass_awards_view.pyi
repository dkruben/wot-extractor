# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/battle_pass/battle_pass_awards_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems
import SoundGroups as SoundGroups
from battle_pass_common import BattlePassRewardReason as BattlePassRewardReason, FinalReward as FinalReward
from frameworks.wulf import ViewSettings as ViewSettings, ViewStatus as ViewStatus, WindowFlags as WindowFlags
from gui.battle_pass.battle_pass_award import BattlePassAwardsManager as BattlePassAwardsManager
from gui.battle_pass.battle_pass_bonuses_packers import packBonusModelAndTooltipData as packBonusModelAndTooltipData, useBigAwardInjection as useBigAwardInjection
from gui.battle_pass.battle_pass_decorators import createBackportTooltipDecorator as createBackportTooltipDecorator, createTooltipContentDecorator as createTooltipContentDecorator
from gui.battle_pass.battle_pass_helpers import getStyleInfoForChapter as getStyleInfoForChapter
from gui.battle_pass.sounds import BattlePassSounds as BattlePassSounds
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.battle_pass.battle_pass_awards_view_model import BattlePassAwardsViewModel as BattlePassAwardsViewModel, RewardReason as RewardReason
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.lobby_window import LobbyNotificationWindow as LobbyNotificationWindow
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, events as events, g_eventBus as g_eventBus
from gui.shared.event_dispatcher import showBattlePass as showBattlePass
from gui.sounds.filters import switchHangarOverlaySoundFilter as switchHangarOverlaySoundFilter
from helpers import dependency as dependency
from skeletons.gui.game_control import IBattlePassController as IBattlePassController
MAP_REWARD_REASON: dict
MAIN_REWARDS_LIMIT = 4
FINAL_REWARDS_LIMIT = 3
STANDART_REWARD_SIZE = 1
WIDE_REWARD_SIZE = 1.5
REWARD_SIZES: dict

class BattlePassAwardsView(ViewImpl):
    __slots__: tuple
    __battlePass: Any
    __tooltipItems: Any
    __closeCallback: Any
    __exitCallback: Any
    __showBuyCallback: Any
    __needNotifyClosing: Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    # decorador original: @createBackportTooltipDecorator(...)
    def createToolTip(self, event):
        ...
    # decorador original: @createTooltipContentDecorator(...)
    def createToolTipContent(self, event, contentID):
        ...
    def getTooltipData(self, event):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, bonuses, packageBonuses, data, starterPack, needNotifyClosing, *args, **kwargs):
        ...
    def _onLoaded(self, data, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def __setAwards(self, bonuses, isFinalReward):
        ...
    def __setMainRewards(self, rewards, isFinalReward):
        ...
    @staticmethod
    def __getRewardWeight(bonus):
        ...
    def __setPackageRewards(self, bonuses):
        ...
    def __onBuyClick(self):
        ...
    def __close(self):
        ...
    def __showPostProgression(self):
        ...

class BattlePassAwardWindow(LobbyNotificationWindow):
    __slots__: tuple
    __params: Any
    def __init__(self, bonuses, data, packageRewards=None, starterPack=None, needNotifyClosing=True):
        ...
    def isParamsEqual(self, *args, **kwargs):
        ...
