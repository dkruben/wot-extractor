# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/lootbox_system/base/utils.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import random as random
from future.utils import viewitems as viewitems, viewvalues as viewvalues
from typing import TYPE_CHECKING as TYPE_CHECKING
import BigWorld as BigWorld
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from account_helpers.AccountSettings import LOOT_BOXES_OPEN_ANIMATION_ENABLED as LOOT_BOXES_OPEN_ANIMATION_ENABLED
from adisp import adisp_async as adisp_async, adisp_process as adisp_process
from constants import REROLL_STOP_TOKEN_PREFIX as REROLL_STOP_TOKEN_PREFIX
from gui import GUI_SETTINGS as GUI_SETTINGS, SystemMessages as SystemMessages
from gui.Scaleform.daapi.view.lobby.store.browser.shop_helpers import getShopURL as getShopURL
from gui.impl import backport as backport
from gui.lootbox_system.base.awards_manager import AwardsManager as AwardsManager
from gui.lootbox_system.base.common import COUNTRY_CODES_FOR_EXTERNAL_LOOT_LIST as COUNTRY_CODES_FOR_EXTERNAL_LOOT_LIST, REROLLABLE_BOX_OPEN_COUNT as REROLLABLE_BOX_OPEN_COUNT, getTextResource as getTextResource
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, events as events, g_eventBus as g_eventBus
from gui.shared.gui_items.processors.loot_boxes import LootBoxSystemOpenProcessor as LootBoxSystemOpenProcessor, AcceptLootBoxRerollProcessor as AcceptLootBoxRerollProcessor, RerollLootBoxProcessor as RerollLootBoxProcessor
from gui.shared.notifications import NotificationPriorityLevel as NotificationPriorityLevel
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from shared_utils import findFirst as findFirst, first as first
from skeletons.gui.game_control import ILootBoxSystemController as ILootBoxSystemController
from skeletons.gui.shared import IItemsCache as IItemsCache
from typing import Callable as Callable, List as List, Tuple as Tuple
from gui.shared.gui_items.customization.c11n_items import Style as Style
from gui.shared.gui_items.loot_box import LootBox as LootBox
from gui.server_events.bonuses import SimpleBonus as SimpleBonus
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
_logger: Any

# decorador original: @adisp_process
# decorador original: @dependency.replace_none_kwargs(...)
def openBoxes(eventName, category, count, processResult=None, lootBoxes=None, isReroll=False):
    ...
# decorador original: @adisp_process
def _openRerollableBox(eventName, category, processResult=None):
    ...
def _pushOpeningErrorEvent():
    ...
# decorador original: @adisp_async
# decorador original: @adisp_process
def acceptRerollableBoxRewards(eventName, category, callback):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getPreferredBox(eventName, category='', lootBoxes=None):
    ...
def getSystemSettings(setting):
    ...
def getInfoPageSettings(eventName, setting):
    ...
def getIsShowIntro(eventName):
    ...
def getIntroVideoUrl(eventName):
    ...
def getIsStartFinishNotificationsVisible(eventName):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getOpeningOptions(eventName, category, lootBoxes=None):
    ...
def getShopOverlayUrl(eventName):
    ...
def isShopVisible(eventName):
    ...
def isCountryForShowingExternalLootList():
    ...
def openExternalLootList():
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getIsAnimationActive(eventName, lootBoxes=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def setIsAnimationActive(eventName, value, lootBoxes=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getLootboxStatisticsKey(eventName, boxID=None, itemsCache=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getVehicleForStyle(style, itemsCache=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def _getVehiclesForStylePreview(criteria=None, itemsCache=None):
    ...
def hasStopRerollToken(bonuses):
    ...
