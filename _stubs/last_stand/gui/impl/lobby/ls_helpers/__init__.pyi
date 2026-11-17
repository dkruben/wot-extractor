# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/impl/lobby/ls_helpers/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from functools import wraps as wraps
from BWUtil import AsyncReturn as AsyncReturn
from last_stand_common.last_stand_constants import BOOSTER_FACTOR_NAMES as BOOSTER_FACTOR_NAMES, BOOSTER_FACTOR_OPERATIONS as BOOSTER_FACTOR_OPERATIONS
from wg_async import wg_await as wg_await, wg_async as wg_async, forwardAsFuture as forwardAsFuture
from gui.impl.backport import getNiceNumberFormat as getNiceNumberFormat
from gui.server_events.awards_formatters import AWARDS_SIZES as AWARDS_SIZES
from gui.server_events.events_helpers import EventInfoModel as EventInfoModel
from last_stand.gui.game_control.ls_artefacts_controller import getBonusPriority as getBonusPriority
from last_stand.gui.impl.gen.view_models.views.common.bonus_item_view_model import BonusItemViewModel as BonusItemViewModel
from last_stand.gui.impl.gen.view_models.views.lobby.widgets.meta_view_model import ArtefactStates as ArtefactStates
from last_stand.gui.impl.gen.view_models.views.lobby.widgets.reward_path_view_model import RewardPathViewModel as RewardPathViewModel
from last_stand.gui.impl.lobby.ls_helpers.bonuses_formatters import getLSMetaAwardFormatter as getLSMetaAwardFormatter, getImgName as getImgName, LSBonusesAwardsComposer as LSBonusesAwardsComposer
from last_stand.skeletons.ls_artefacts_controller import ILSArtefactsController as ILSArtefactsController
from last_stand.skeletons.ls_controller import ILSController as ILSController
from last_stand.skeletons.ls_quests_ui_cache import ILSQuestsUICache as ILSQuestsUICache
from helpers import dependency as dependency, time_utils as time_utils
from items.tankmen import MAX_SKILLS_EFFICIENCY as MAX_SKILLS_EFFICIENCY
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from ids_generators import SequenceIDGenerator as IDGenerator
from gui.server_events.awards_formatters import PreformattedBonus as PreformattedBonus
from gui.server_events.bonuses import SimpleBonus as SimpleBonus
from gui.server_events.event_items import Quest as Quest
PROMINENT_REWARD_TOOLTIP_ID = 'prominent_reward_tooltip'
INF_DISPLAY_BONUSES = 999

class UseHeaderNavigationImpossible(object):
    __slots__: tuple
    _hide: Any
    _show: Any
    _confirmationHelper: Any
    def __init__(self, confirmationHelper, show=True, hide=True):
        ...
    def __call__(self, func):
        ...

# decorador original: @dependency.replace_none_kwargs(...)
def isQuestCompleted(questID, questsCache=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getQuestDescription(questID, questsCache=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def isCustomizationHangarDisabled(lsCtrl=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getArtefactState(artefactID, ctrl=None):
    ...
def fillRewards(bonusRewards, bonusModels, maxBonuseInView, idGen, skipBonuses=None):
    ...
def fillRewardsForTooltips(bonusRewards, bonusModels, maxBonuseInView, skipBonuses=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def fillProminentBonus(resourceID, bonusRewards, bonusItemModel, ctrl=None):
    ...
def fillBaseBonusProperties(bonus, bonusModel):
    ...
def getQuestFinishTimeLeft(quest):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getBoosterFactorsParam(boosterName, ctrl=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def fillRewardPathWidgetViewModel(model, lastUnopenedArtefactId=None, lsCtrl=None, lsArtefactCtrl=None):
    ...
def getLSVehicleStatus(vehicle):
    ...
