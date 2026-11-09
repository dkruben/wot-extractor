# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/user_missions/hangar_widget/providers/quest_providers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as ARENA_BONUS_TYPE_CAPS
from config_schemas.umg import WeightsModel as WeightsModel
from config_schemas.umg_config import umgConfigSchema as umgConfigSchema
from constants import PREMIUM_TYPE as PREMIUM_TYPE
from gui.impl.lobby.user_missions.hangar_widget.providers import ConfigKeys as ConfigKeys
from gui.impl.lobby.user_missions.hangar_widget.providers.user_mission_item import DailyQuestMissionItem as DailyQuestMissionItem, PremiumDailyQuestMissionItem as PremiumDailyQuestMissionItem, MissionItem as MissionItem, WeeklyQuestMissionItem as WeeklyQuestMissionItem
from gui.server_events.event_items import Quest as Quest
from gui.server_events.events_helpers import isDailyQuestsEnable as isDailyQuestsEnable, isPremiumQuestsEnable as isPremiumQuestsEnable, isWeeklyQuestsEnable as isWeeklyQuestsEnable, PremMissionsSortKey as PremMissionsSortKey
from skeletons.gui.game_control import IHangarGuiController as IHangarGuiController
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared import IItemsCache as IItemsCache
from helpers import dependency as dependency
import typing as typing
import logging as logging
_logger: Any

class QuestProviderBase(object):
    __hangarGuiCtrl: Any
    def getQuests(self):
        ...
    def updateConfig(self, config):
        ...
    def destroy(self):
        ...
    def _setRawData(self, item, raw):
        ...
    def _checkEnabled(self):
        ...
    def _checkBonusCaps(self, bonusCaps):
        ...
    def _setCompletedState(self, item, raw):
        ...
    def _setPacker(self, item, packer):
        ...

class DailyQuestProvider(QuestProviderBase):
    _KEY = ConfigKeys.REGULAR_DAILY
    _ITEM = DailyQuestMissionItem
    storage: Any
    config: Any
    def __init__(self, storage, config):
        ...
    def getQuests(self):
        ...
    def updateConfig(self, config):
        ...
    def destroy(self):
        ...
    def _checkEnabled(self):
        ...

class PremiumQuestProvider(QuestProviderBase):
    _itemsCache: Any
    storage: Any
    config: Any
    def __init__(self, storage, config):
        ...
    def getQuests(self):
        ...
    def updateConfig(self, config):
        ...
    def destroy(self):
        ...
    def _checkEnabled(self):
        ...

class WeeklyQuestProvider(QuestProviderBase):
    _KEY = ConfigKeys.WEEKLY
    _ITEM = WeeklyQuestMissionItem
    storage: Any
    weightsModel: Any
    def __init__(self, storage, config):
        ...
    def getQuests(self):
        ...
    def updateConfig(self, config):
        ...
    def destroy(self):
        ...
    def _setConditions(self, item, raw):
        ...
    def _checkEnabled(self):
        ...
