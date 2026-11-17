# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/formatters/auto_boxes_subformatters.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from future.utils import viewitems as viewitems
import BigWorld as BigWorld
from adisp import adisp_async as adisp_async, adisp_process as adisp_process
from dossiers2.ui.achievements import BADGES_BLOCK as BADGES_BLOCK
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.lootbox_system.base.awards import preformatRewardsInfo as preformatRewardsInfo
from gui.lootbox_system.base.common import TEXT_RESOURCE_PREFIX as TEXT_RESOURCE_PREFIX, NotificationPathPart as NotificationPathPart, getTextResource as getTextResource, DEFAULT_EVENT_NAME as DEFAULT_EVENT_NAME
from gui.server_events.bonuses import getMergedBonusesFromDicts as getMergedBonusesFromDicts
from gui.shared.gui_items.dossier import getAchievementFactory as getAchievementFactory
from gui.shared.gui_items.loot_box import ALL_LUNAR_NY_LOOT_BOX_TYPES as ALL_LUNAR_NY_LOOT_BOX_TYPES, WTLootBoxes as WTLootBoxes
from gui.shared.notifications import NotificationPriorityLevel as NotificationPriorityLevel
from helpers import dependency as dependency
from messenger import g_settings as g_settings
from messenger.formatters.service_channel import LootBoxAchievesFormatter as LootBoxAchievesFormatter, QuestAchievesFormatter as QuestAchievesFormatter, ServiceChannelFormatter as ServiceChannelFormatter, WaitItemsSyncFormatter as WaitItemsSyncFormatter
from messenger.formatters.service_channel_helpers import MessageData as MessageData, getCustomizationItemData as getCustomizationItemData, getRewardsForBoxes as getRewardsForBoxes
from skeletons.gui.shared import IItemsCache as IItemsCache

class IAutoLootBoxSubFormatter(object):
    @classmethod
    def getBoxesOfThisGroup(cls, data):
        ...
    @classmethod
    def _isBoxOfThisGroup(cls, boxID):
        ...
    @classmethod
    def _isBoxOfRequiredTypes(cls, boxID, boxTypes):
        ...

class AutoLootBoxSubFormatter(IAutoLootBoxSubFormatter):
    __itemsCache: Any
    @classmethod
    def getBoxesOfThisGroup(cls, data):
        ...
    @classmethod
    def _isBoxOfRequiredTypes(cls, boxID, boxTypes):
        ...

class AsyncAutoLootBoxSubFormatter(WaitItemsSyncFormatter, AutoLootBoxSubFormatter):
    _achievesFormatter: Any
    def __init__(self):
        ...

class SyncAutoLootBoxSubFormatter(ServiceChannelFormatter, AutoLootBoxSubFormatter):
    _achievesFormatter: Any
    def __init__(self):
        ...

class EventBoxesFormatter(AsyncAutoLootBoxSubFormatter):
    __itemsCache: Any
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def format(self, message, callback):
        ...
    @classmethod
    def _isBoxOfThisGroup(cls, boxID):
        ...
    @staticmethod
    def _getMessageTemplate():
        ...
    @staticmethod
    def _getTextResPath():
        ...
    def __getFormattedBoxes(self, message, openedBoxesIDs):
        ...

class LunarNYEnvelopeAutoOpenFormatter(AsyncAutoLootBoxSubFormatter):
    __MESSAGE_TEMPLATE = 'LunarBoxesAutoOpenMessage'
    _DECAL_TYPE_NAME = 'projection_decal'
    _achievesFormatter: Any
    def __init__(self):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def format(self, message, callback):
        ...
    @classmethod
    def formatAchieves(cls, rewards, formatter):
        ...
    @classmethod
    def _isBoxOfThisGroup(cls, boxID):
        ...
    @classmethod
    def __makeAchieve(cls, key, **kwargs):
        ...
    @staticmethod
    def __extractAchievements(data):
        ...
    @classmethod
    def __makeDecalsString(cls, customizations):
        ...

class LootBoxSystemAutoOpenFormatter(AsyncAutoLootBoxSubFormatter):
    __MESSAGE_TEMPLATE = 'LootBoxSystemAutoOpenMessage'
    __BREAK: Any
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def format(self, message, callback):
        ...
    @classmethod
    def getBoxesOfThisGroup(cls, data):
        ...
    def __getEventNames(self, data):
        ...
    def __getMessage(self, message, openedBoxes, eventName):
        ...
