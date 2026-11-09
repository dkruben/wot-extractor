# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_pass/rewards_sort.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import re as re
from enum import Enum as Enum, unique as unique
from functools import partial as partial
from gui import GUI_NATIONS as GUI_NATIONS, GUI_NATIONS_ORDER_INDEX as GUI_NATIONS_ORDER_INDEX
from nations import NONE_INDEX as NONE_INDEX
from shared_utils import safeIndexOf as safeIndexOf
_logger: Any
_REWARDS_TYPES_ORDER: tuple
_REWARDS_ORDER: dict
_BASE_PATTERN = '(basic|enhanced|improved|trophy|modernized)*([a-z]+)'
_REWARD_NAME_EXTRACTOR: Any
_REWARD_BATTLE_BOOSTER_EXTRACTOR: Any
_REWARD_NATION_EXTRACTOR: Any
_REWARDS_SORT_KEYS: dict

class _Enum(Enum):
    @classmethod
    def makeValue(cls, value):
        ...

# decorador original: @unique
class _RewardType(_Enum):
    BATTLE_BOOSTER = 'battle_booster'
    BLUEPRINT = 'blueprint'
    BROCHURE = 'brochure'
    DEVICE = 'new_device'
    GUIDE = 'guide'
    MODERNIZED_DEVICE = 'modernized_device'
    TROPHY = 'trophy'
    CREW_BOOK = 'crewbook'

# decorador original: @unique
class _Reward(_Enum):
    ADDIT_INVISIBILITY_DEVICE = 'AdditInvisibilityDevice'
    ADDITIONAL_INVISIBILITY_DEVICE = 'AdditionalInvisibilityDevice'
    AIM_DRIVES = 'AimDrives'
    AIM_STABILIZER = 'AimingStabilizer'
    AIM_DRIVES_AIM_STABILIZER = 'AimDrivesAimingStabilizer'
    ANTI_FRAGMENTATION = 'AntifragmentationLining'
    BLUEPRINT = 'Blueprint'
    BROCHURE = 'Brochure'
    CAMOUFLAGE = 'CamouflageNet'
    COMM_VIEW = 'CommandersView'
    CONFIGURATION = 'Configuration'
    GROUSERS = 'Grousers'
    GUIDE = 'Guide'
    HEALTH_RESERVE = 'ExtraHealthReserve'
    HEALTH_RESERVE_ANTI_FRAGMENTATION = 'ExtraHealthReserveAntifragmentationLining'
    OPTICS = 'CoatedOptics'
    RADIO = 'RadioCommunication'
    ROT_MECHANISM = 'RotationMechanism'
    SIGHTS = 'Sights'
    SIGHTS_ENHANCED_AIM_DRIVES = 'SightsEnhancedAimDrives'
    STEREOSCOPE = 'Stereoscope'
    TANK_RAMMER = 'TankRammer'
    TURBOCHARGER = 'Turbocharger'
    TURBOCHARGER_ROT_MECHANISM = 'TurbochargerRotationMechanism'
    RAMMER = 'Rammer'
    VENTILATION = 'Ventilation'

def _extractRewardName(rewardRawName, extractor):
    ...
def _extractRewardNation(rewardRawName):
    ...
def _rewardTypeSortKey(item):
    ...
def _rewardSortByNation(item):
    ...
def _rewardSortByType(rewardType, item):
    ...
def _defaultItemSort(item):
    ...
def getTypesSortKey():
    ...
def getItemsSortKey(rewardTypeName):
    ...
