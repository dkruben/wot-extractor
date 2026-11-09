# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/account_completion/utils/common.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from constants import EMAIL_CONFIRMATION_QUEST_ID as EMAIL_CONFIRMATION_QUEST_ID
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams as SFViewLoadParams
from gui.impl.gen import R as R
from gui.server_events.bonuses import getNonQuestBonuses as getNonQuestBonuses
from gui.shared import g_eventBus as g_eventBus, events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.missions.packers.bonus import packMissionsBonusModelAndTooltipData as packMissionsBonusModelAndTooltipData, getDefaultBonusPacker as getDefaultBonusPacker
from gui.shared.money import Currency as Currency
from helpers import dependency as dependency
from shared_utils import first as first
from skeletons.gui.server_events import IEventsCache as IEventsCache
from gui.impl.gen.view_models.views.lobby.account_completion.add_credentials_model import AddCredentialsModel as AddCredentialsModel
from gui.impl.gen.view_models.views.lobby.account_completion.common.base_wgnp_overlay_view_model import BaseWgnpOverlayViewModel as BaseWgnpOverlayViewModel
from gui.impl.gen.view_models.views.lobby.account_completion.steam_email_confirm_rewards_view_model import SteamEmailConfirmRewardsViewModel as SteamEmailConfirmRewardsViewModel
from gui.impl.gen.view_models.views.lobby.account_completion.tooltips.hangar_tooltip_model import HangarTooltipModel as HangarTooltipModel
from gui.impl.backport import TooltipData as TooltipData
from gui.server_events.event_items import TokenQuest as TokenQuest
from typing import Optional as Optional, List as List, Dict as Dict, Union as Union
_BONUSES_ORDER: tuple
RESTRICTED_REQUEST_MIN_TIME = 5
DISABLE_BUTTON_TIME = 90

def _keyBonusesOrder(bonus):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getEmailConfirmationQuest(eventsCache=None):
    ...
def getSteamEmailConfirmBonuses(rewards=None):
    ...
def fillRewards(model, rewards=None, tooltipItems=None):
    ...
def showAccountAlreadyHasEmail(viewModel):
    ...
def openMenu():
    ...
def _createSteamEmailConfirmBonuses(rewards):
    ...
def _getSteamEmailConfirmBonusesFromQuest():
    ...
