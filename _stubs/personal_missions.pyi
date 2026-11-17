# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/personal_missions.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from enum import Enum as Enum
import potapov_quests as potapov_quests
import persistent_data_cache_common as pdc
from quest_xml_source import QuestValidationSerializer as QuestValidationSerializer
g_cache = None
g_operationsCache = None
g_campaignsCache = None
PERSONAL_MISSIONS_XML_PATH = potapov_quests.POTAPOV_QUEST_XML_PATH
REGULAR_OPERATION_SPEC_LVL_RESTRICTION = 1
OPERATION_11_LVL_RESTRICTION = 11
PERSONAL_MISSION_REGULAR_MIN_LEVEL = 6
PM_BRANCH_TO_FREE_TOKEN_NAME = potapov_quests.PM_BRANCH_TO_FREE_TOKEN_NAME
PM_BRANCH_TO_FINAL_PAWN_COST = potapov_quests.PM_BRANCH_TO_FINAL_PAWN_COST
PM_REWARD_BY_DEMAND = potapov_quests.PQ_REWARD_BY_DEMAND
PM_BRANCH_TO_PM_PROGRESS_KEY: dict

class PM_BRANCH(potapov_quests.PQ_BRANCH):
    ...

class PM_STATE(potapov_quests.PQ_STATE):
    ...

class PM_FLAG(potapov_quests.PQ_FLAG):
    ...

class PM_SWITCHES(potapov_quests.PQ_SWITCHES):
    ...

class PM3QType(object):
    ASSAULT = 'Assault'
    SNIPER = 'Sniper'
    SUPPORT = 'Support'

class CampaignsCache(potapov_quests.SeasonCache):
    def getCampaignInfo(self, campaignID):
        ...

class OperationsCache(potapov_quests.TileCache):
    def getOperationInfo(self, operationID):
        ...

class PMCache(potapov_quests.PQCache):
    def questByPersonalMissionID(self, missionID):
        ...
    def hasMission(self, missionID):
        ...
    def isPersonalMission(self, uniqueQuestID):
        ...
    def questListByOperationIDChainID(self, tileID, chainID):
        ...
    def finalMissionIDByOperationIDChainID(self, tileID, chainID):
        ...
    def initialMissionQuestIDByOperationIDChainID(self, tileID, chainID):
        ...
    def getPersonalMissionIDByUniqueID(self, uniqueQuestID):
        ...
    def branchByMissionID(self, potapovQuestID):
        ...
    def getPersonalMissionNameByID(self, missionID):
        ...
    def getPersonalMissionIDByName(self, missionName):
        ...

class PMStorage(potapov_quests.PQStorage):
    ...

class PMProgressKeys(str, Enum):
    REGULAR = 'potapovQuests'
    PM2_PROGRESS = 'pm2_progress'
    PM3_PROGRESS = 'pm3_progress'
    PM4_PROGRESS = 'pm4_progress'

def isPersonalMissionsEnabled(gameParams, branch):
    ...
def _createPMCache():
    ...
def init():
    ...
