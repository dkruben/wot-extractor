# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/prestige_system/prestige_milestones_common.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
from typing import Optional as Optional, Dict as Dict, Set as Set, Any as Any, Union as Union
from copy import copy as copy
from constants import IS_CLIENT as IS_CLIENT
from debug_utils import LOG_DEBUG_DEV as LOG_DEBUG_DEV, LOG_DEBUG as LOG_DEBUG
from dossiers2.custom.cache import getCache as getDossiers2Cache, buildCache as buildDossiers2Cache
VehCDType: _Any
PrestigeLevelType: _Any
InvoiceStatusType: _Any
ErrorStrType: _Any
MilestoneData: _Any
MilestonesType: _Any
MilestonesCacheType: _Any
OverrideItem: _Any
_g_cache: dict

class PrestigeMilestonesConfig(object):
    _config: _Any
    __cache: _Any
    def __init__(self, config):
        ...
    @property
    def milestones(self):
        ...

def getCache():
    ...
def computePrestigeMilestonesCache(config, cache=None, dossiers2Cache=None):
    ...
def computeMilestonesCache(defaultMilestones, overrideItems, enabledVehicleLevels, vehiclesByLevel):
    ...
def applyOverrideMilestones(vehicleMilestones, override):
    ...
