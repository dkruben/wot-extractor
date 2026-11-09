# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/server_events/event_items.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems
from fun_random.gui.feature.fun_constants import FEP_PROGRESSION_TRIGGER_QUEST_ID as FEP_PROGRESSION_TRIGGER_QUEST_ID, PROGRESSION_COUNTER_TEMPLATE as PROGRESSION_COUNTER_TEMPLATE, FEP_PROGRESSION_ALT_TRIGGER_QUEST_ID as FEP_PROGRESSION_ALT_TRIGGER_QUEST_ID, FEP_PROGRESSION_UNLIMITED_TRIGGER_QUEST_ID as FEP_PROGRESSION_UNLIMITED_TRIGGER_QUEST_ID, FEP_PROGRESSION_UNLIMITED_ALT_TRIGGER_QUEST_ID as FEP_PROGRESSION_UNLIMITED_ALT_TRIGGER_QUEST_ID, PROGRESSION_UNLIMITED_COUNTER_TEMPLATE as PROGRESSION_UNLIMITED_COUNTER_TEMPLATE
from fun_random.gui.feature.util.fun_helpers import getProgressionNameByTrigger as getProgressionNameByTrigger, getIdByTrigger as getIdByTrigger, isFunProgressionTrigger as isFunProgressionTrigger, isFunProgressionUnlimitedTrigger as isFunProgressionUnlimitedTrigger
from fun_random.gui.feature.util.fun_mixins import FunProgressionWatcher as FunProgressionWatcher
from fun_random.gui.feature.util.fun_wrappers import hasActiveProgression as hasActiveProgression
from gui.server_events.event_items import Quest as Quest, IQuestBuilder as IQuestBuilder

class FunProgressionTriggerQuest(Quest, FunProgressionWatcher):
    COUNTER_TEMPLATE = PROGRESSION_COUNTER_TEMPLATE
    MAIN_TRIGGER_QUEST_ID = FEP_PROGRESSION_TRIGGER_QUEST_ID
    ALT_TRIGGER_QUEST_ID = FEP_PROGRESSION_ALT_TRIGGER_QUEST_ID
    __pName: Any
    __triggerId: Any
    __counterName: Any
    __altQuest: Any
    def __init__(self, qID, data, progress=None):
        ...
    def isMain(self):
        ...
    def findAndSaveAltQuest(self, quests):
        ...
    def getAltQuest(self):
        ...
    @classmethod
    def showMissionAction(cls):
        ...
    # decorador original: @hasActiveProgression(...)
    def isForActiveProgression(self):
        ...
    def isShowedPostBattle(self):
        ...
    def getCurrentProgress(self):
        ...
    def getTotalProgress(self):
        ...
    def getDetailedProgress(self):
        ...
    def getEarnedPoints(self):
        ...
    def getBonusCounterNumber(self):
        ...
    def getQuestCondition(self):
        ...
    def isCompleted(self, progress=None):
        ...

class FunProgressionUnlimitedTriggerQuest(FunProgressionTriggerQuest):
    COUNTER_TEMPLATE = PROGRESSION_UNLIMITED_COUNTER_TEMPLATE
    MAIN_TRIGGER_QUEST_ID = FEP_PROGRESSION_UNLIMITED_TRIGGER_QUEST_ID
    ALT_TRIGGER_QUEST_ID = FEP_PROGRESSION_UNLIMITED_ALT_TRIGGER_QUEST_ID
    def getQuestCondition(self):
        ...

class FunProgressionTriggerQuestBuilder(IQuestBuilder):
    @classmethod
    def isSuitableQuest(cls, questType, qID):
        ...
    @classmethod
    def buildQuest(cls, questType, qID, data, progress=None, expiryTime=None):
        ...

class FunProgressionUnlimitedTriggerQuestBuilder(IQuestBuilder):
    @classmethod
    def isSuitableQuest(cls, questType, qID):
        ...
    @classmethod
    def buildQuest(cls, questType, qID, data, progress=None, expiryTime=None):
        ...
