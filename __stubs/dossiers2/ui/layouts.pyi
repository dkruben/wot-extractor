# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/dossiers2/ui/layouts.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import defaultdict as defaultdict
from future.utils import viewitems as viewitems, viewvalues as viewvalues
import nations as nations
from constants import DOSSIER_TYPE as DOSSIER_TYPE
from dossiers2.common.DossierBlockBuilders import IBlockBuilderWithRecordsLayout as IBlockBuilderWithRecordsLayout
from dossiers2.custom import layouts as com_layouts, records as records
from dossiers2.custom.vehicle_layout import FALLOUT_ACHIEVEMENTS_BLOCK_LAYOUT as FALLOUT_ACHIEVEMENTS_BLOCK_LAYOUT
from dossiers2.ui import achievements as achievements
_AB = achievements.ACHIEVEMENT_BLOCK
_TANK_EXPERT_PREFIX = 'tankExpert'
_MECH_ENGINEER_PREFIX = 'mechanicEngineer'
_VEHICLE_COLLECTOR_PREFIX = 'collectorVehicle'
_HIST_BATTLEFIELD_POSTFIX = 'battlefield'
TANK_EXPERT_GROUP: list
MECH_ENGINEER_GROUP: list
VEHICLE_COLLECTOR_GROUP: list
HISTORY_BATTLEFIELD_GROUP: list
PERSONAL_MISSIONS_GROUP: list
CHRISTMAS_QUESTS_GROUP: list
HE17_QUESTS_GROUP: list
NY18_QUESTS_GROUP: list
IGNORED_BY_BATTLE_RESULTS: list
_COMMON_DOSSIERS_TYPE = 0
_EXCLUDED_ACHIEVES: Any
_CUSTOM_ACHIEVES: Any
ACCOUNT_ACHIEVEMENT_LAYOUT: list
VEHICLE_ACHIEVEMENT_LAYOUT: list
TANKMAN_ACHIEVEMENT_LAYOUT: list
FORT_ACHIEVEMENT_LAYOUT: list
RATED7x7_ACHIEVEMENT_LAYOUT: list
CLUB_ACHIEVEMENT_LAYOUT: list
_layoutsMap: dict
_MODE_ACHIEVEMENTS: Any
NEAREST_ACHIEVEMENTS: Any

def _7x7(achieveName):
    ...
def _total(achieveName):
    ...
def _single(achieveName):
    ...
def _single7x7(achieveName):
    ...
def _fallout(achieveName):
    ...
def _epicBattle(achieveName):
    ...
def _getComLayoutRecordID(record):
    ...
def _buildComLayoutSet(dossierType, comLayout):
    ...
def getAchievementsLayout(dossierType):
    ...
def isAchievementRegistered(record):
    ...
def getAchievementsByMode(mode):
    ...
def init():
    ...
