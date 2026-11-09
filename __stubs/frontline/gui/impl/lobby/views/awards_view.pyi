# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/impl/lobby/views/awards_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems
import SoundGroups as SoundGroups
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags, WindowLayer as WindowLayer
from gui.battle_pass.battle_pass_decorators import createBackportTooltipDecorator as createBackportTooltipDecorator, createTooltipContentDecorator as createTooltipContentDecorator
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.common.awards_view_model import AwardsViewModel as AwardsViewModel
from gui.impl.gen.view_models.views.lobby.common.reward_item_model import RewardItemModel as RewardItemModel
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.lobby_window import LobbyNotificationWindow as LobbyNotificationWindow
from gui.server_events.bonuses import getNonQuestBonuses as getNonQuestBonuses, mergeBonuses as mergeBonuses, splitBonuses as splitBonuses
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.missions.packers.bonus import ItemBonusUIPacker as ItemBonusUIPacker, BonusUIPacker as BonusUIPacker, getDefaultBonusPackersMap as getDefaultBonusPackersMap
from gui.sounds.epic_sound_constants import EPIC_SOUND as EPIC_SOUND
from helpers import dependency as dependency
from skeletons.gui.game_control import IEpicBattleMetaGameController as IEpicBattleMetaGameController
MAIN_REWARDS_LIMIT = 4

class AwardsView(ViewImpl):
    __slots__: tuple
    __isAnimationEnded: Any
    __tooltipItems: Any
    __onCloseCallback: Any
    __onAnimationEndedCallback: Any
    def __init__(self, bonuses, onCloseCallback=None, onAnimationEnded=None):
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
    def _finalize(self):
        ...
    def _onLoading(self, bonuses, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def __onAnimationEnded(self):
        ...
    @staticmethod
    def __safeCall(callback, *args, **kwargs):
        ...
    @staticmethod
    def __countBonuses(bonuses):
        ...

class AwardsWindow(LobbyNotificationWindow):
    __slots__: tuple
    __epicController: Any
    __params: Any
    def __init__(self, bonuses, onCloseCallback=None, onAnimationEndedCallback=None):
        ...
    def isParamsEqual(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...

class FrontlineItemBonusUIPacker(ItemBonusUIPacker):
    @classmethod
    def _packSingleBonus(cls, bonus, item, count):
        ...
    @classmethod
    def _getBonusModel(cls):
        ...

def composeBonuses(rewards, ctx=None):
    ...
def getFrontlineBonusPacker():
    ...
def packBonusModelAndTooltipData(rewards, bonusModelsListMain, bonusModelsListAdditional, tooltipData=None, ctx=None):
    ...
