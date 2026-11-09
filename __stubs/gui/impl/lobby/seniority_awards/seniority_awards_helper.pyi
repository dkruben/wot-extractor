# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/seniority_awards/seniority_awards_helper.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import BigWorld as BigWorld
from account_helpers.settings_core.settings_constants import SeniorityAwardsStorageKeys as SeniorityAwardsStorageKeys
from frameworks.wulf import ViewFlags as ViewFlags
from gui import SystemMessages as SystemMessages
from gui.impl import backport as backport
from gui.impl.auxiliary.rewards_helper import getRewardRendererModelPresenter as getRewardRendererModelPresenter, DEF_COMPENSATION_PRESENTERS as DEF_COMPENSATION_PRESENTERS
from gui.impl.auxiliary.tooltips.compensation_tooltip import CompensationTooltipContent as CompensationTooltipContent, VehicleCompensationTooltipContent as VehicleCompensationTooltipContent
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.loot_box_compensation_tooltip_model import LootBoxCompensationTooltipModel as LootBoxCompensationTooltipModel
from gui.impl.lobby.seniority_awards.seniority_awards_sounds import playSound as playSound, LootBoxViewEvents as LootBoxViewEvents
from gui.shared import g_eventBus as g_eventBus
from gui.shared.events import GameEvent as GameEvent
from gui.shared.notifications import NotificationPriorityLevel as NotificationPriorityLevel
from helpers import dependency as dependency
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.game_control import ISeniorityAwardsController as ISeniorityAwardsController
_logger: Any

def getVehicleCD(value):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def isSeniorityAwardsSystemNotificationShowed(notification, settings=None):
    ...
def setSeniorityAwardEventStateSetting(value):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def setSeniorityAwardsServerSetting(settingsSection, settings=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getRewardCategoryForUI(seniorityAwardsController=None):
    ...
def showRestrictedSysMessage():
    ...
def showVehicleSelectionTimeoutError():
    ...
def showVehicleSelectionMultipleTokensError():
    ...
def fireCloseToHangar():
    ...
def getLootboxRendererModelPresenter(reward):
    ...
def getRewardTooltipContent(event):
    ...
def _closeLootBoxWindows():
    ...
