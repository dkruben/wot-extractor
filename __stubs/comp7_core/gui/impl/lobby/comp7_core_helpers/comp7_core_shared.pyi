# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_core/scripts/client/comp7_core/gui/impl/lobby/comp7_core_helpers/comp7_core_shared.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.impl.gen.view_models.views.lobby.user_missions.constants.event_banner_state import EventBannerState as EventBannerState
from gui.periodic_battles.models import PeriodType as PeriodType, PrimeTimeStatus as PrimeTimeStatus
from gui.shared.utils.SelectorBattleTypesUtils import isKnownBattleType as isKnownBattleType
from helpers import time_utils as time_utils
_SEASON_START_DURATION_DAYS = 7
_SEASON_END_DURATION_DAYS = 7
INACTIVE_PRIME_TIMES: set

def getCurrentSeasonState(modeController, seasonStateClazz):
    ...
def getModeSeasonState(modeController, seasonStateClazz):
    ...
def getProgressionYearState(modeController, yearStateClazz):
    ...
def getEventBannerState(modeController, seasonStateClazz, selectorBattleType):
    ...
