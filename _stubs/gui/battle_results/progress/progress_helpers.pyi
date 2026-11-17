# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_results/progress/progress_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from copy import deepcopy as deepcopy
import typing as typing
import BigWorld as BigWorld
from collections import namedtuple as namedtuple
from personal_missions import PM_BRANCH as PM_BRANCH
from shared_utils import first as first
from gui.prestige.prestige_helpers import mapGradeIDToUI as mapGradeIDToUI, getCurrentGrade as getCurrentGrade, getCurrentProgress as getCurrentProgress, prestigePointsToXP as prestigePointsToXP, hasVehiclePrestige as hasVehiclePrestige, MAX_GRADE_ID as MAX_GRADE_ID
from helpers import dependency as dependency
from dog_tags_common.components_config import componentConfigAdapter as componentConfigAdapter
from skeletons.gui.battle_results import IBattleResultsService as IBattleResultsService
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.server_events import IEventsCache as IEventsCache
from gui.server_events.event_items import PersonalMission as PersonalMission, PMOperation as PMOperation
PrestigeProgress: Any
DogTagProgress: Any

def getPrestigeProgress(reusable):
    ...
def createPrestigeInfo(vehCD, prestigeData):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getDogTagsProgress(reusable, lobbyContext=None):
    ...
def createDogTagInfo(componentId, dogTagType):
    ...
def isQuestCompleted(_, pPrev, pCur):
    ...
def packQuestProgressData(qID, allCommonQuests, qProgress, isCompleted):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getReceivedTokensInfo(arenaUniqueID, battleResultsService=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def isPMOperationAndMissionEnabled(quest, eventsCache=None):
    ...
