# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/marathon/marathon_constants.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl.gen import R as R
from helpers.time_utils import ONE_DAY as ONE_DAY, ONE_HOUR as ONE_HOUR
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
ZERO_TIME = 0.0
TIME_FORMAT_DAYS = 'days'
TIME_FORMAT_HOURS = 'hours'
TIME_FORMAT_TO_TIME_UNIT: dict
R_BUYING_PANEL = R.strings.marathon.vehiclePreview.buyingPanel
R_TITLE_TOOLTIP = R.strings.marathon.vehiclePreview.title.tooltip
BUYING_BUTTON_ICON_ALIGN = 'right'
TOKEN_COUNT_INDEX = 1
MISSION_TAB_FORMAT = 'MISSIONS_TAB_{}'
AWARD_TOKENS_FORMAT = '{}{}'

class MarathonState(CONST_CONTAINER):
    NOT_STARTED = 0
    IN_PROGRESS = 1
    FINISHED = 3
    SUSPENDED = 4
    DISABLED = 5
    UNKNOWN = 6
    ENABLED_STATE: tuple
    DISABLED_STATE: tuple

class MarathonWarning(CONST_CONTAINER):
    WRONG_VEH_TYPE = 'veh_type'
    WRONG_BATTLE_TYPE = 'battle_type'
    NONE = ''

class MarathonFlagTooltip(CONST_CONTAINER):
    BASE: Any
    COUNTDOWN: Any
    PROGRESS: Any
    TEXT: Any
