# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/user_missions/hangar_widget/utils.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from gui.Scaleform.genConsts.MISSIONS_STATES import MISSIONS_STATES as MISSIONS_STATES
from gui.impl.gen.view_models.views.lobby.user_missions.hub.tabs.basic_missions.daily.daily_mission_model import DailyMissionModel as DailyMissionModel
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.user_missions.widget.widget_quest_model import WidgetQuestModel as WidgetQuestModel
from gui.server_events.events_helpers import EventInfoModel as EventInfoModel
from gui.shared.missions.packers.conditions import CONDITION_GROUP_AND as CONDITION_GROUP_AND
from gui.shared.missions.packers.events import findFirstConditionModel as findFirstConditionModel, getEventUIDataPacker as getEventUIDataPacker
from helpers import dependency as dependency
from skeletons.gui.server_events import IEventsCache as IEventsCache
from typing import Union as Union
from gui.impl.lobby.user_missions.hangar_widget.providers.user_mission_item import MissionItem as MissionItem
from gui.server_events.event_items import Quest as Quest
from gui.impl.gen.view_models.views.lobby.user_missions.hub.tabs.basic_missions.weekly.weekly_mission_model import WeeklyMissionModel as WeeklyMissionModel
from gui.impl.lobby.user_missions.hangar_widget.providers.user_mission_item import WeeklyQuestMissionItem as WeeklyQuestMissionItem

class MissionItemPacker(object):
    def _getFirstConditionModelFromQuestModel(self, dailyQuestModel):
        ...
    # decorador original: @dependency.replace_none_kwargs(...)
    def packMissionItem(self, model, raw, readyForAnimation=True, eventsCache=None):
        ...
    def packSpecificMissionItem(self, model, data):
        ...

class DailyMissionItemPacker(MissionItemPacker):
    def _getFirstConditionModelFromQuestModel(self, dailyQuestModel):
        ...
    def packSpecificMissionItem(self, model, data):
        ...

class WeeklyMissionItemPacker(MissionItemPacker):
    def _getFirstConditionModelFromQuestModel(self, dailyQuestModel):
        ...
    def packSpecificMissionItem(self, model, data):
        ...

def getCountdown(missionItem):
    ...
def addSpecialConditions(model, commonCondition, specialConditionIds):
    ...
