# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/server_events/cond_formatters/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
import typing as typing
from gui.Scaleform.locale.QUESTS import QUESTS as QUESTS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.server_events.conditions import GROUP_TYPE as GROUP_TYPE
from gui.server_events.formatters import RELATIONS_SCHEME as RELATIONS_SCHEME, RELATIONS as RELATIONS
from gui.shared.formatters import text_styles as text_styles
from helpers import i18n as i18n
from personal_missions_constants import CONDITION_ICON as CONDITION_ICON
from soft_exception import SoftException as SoftException
from gui.server_events.conditions import BattleResults as BattleResults
MAX_CONDITIONS_IN_OR_SECTION_SUPPORED = 2
TOP_RANGE_HIGHEST = 1
TOP_RANGE_LOWEST = 15
POSSIBLE_BATTLE_RESUTLS_KEYS: dict
BATTLE_RESULTS_KEYS: dict
BATTLE_RESULTS_AGGREGATED_KEYS: dict
VEHICLE_TYPES: dict
FormattableField: Any

class CONDITION_SIZE(object):
    NORMAL = 'normal'
    MINIMIZED = 'minimized'

class FORMATTER_IDS(object):
    DESCRIPTION = 'descriptionFormatter'
    CUMULATIVE = 'cumulativeFormatter'
    COMPLEX = 'complex'
    RELATION = 'relationFormatter'
    COMPLEX_RELATION = 'complexRelationFormatter'
    SIMPLE_TITLE = 'simpleTitleFormatter'

class COMPLEX_CONDITION_BLOCK(object):
    ACHIEVEMENT = 'achievement'
    VEHICLES_LIST = 'vehicles_list'
    VEHICLES_FILTERS = 'vehicles_filters'

def packDescriptionField(description):
    ...
def packSimpleTitle(title):
    ...
def packText(text, styler=None):
    ...
def intersperse(sequence, item):
    ...
def getSeparator(groupType=...):
    ...
def getSeparatorBlock(groupType=...):
    ...
def packTokenProgress(tokenId, questId, title, image, gotCount, needCount, isBigSize=False):
    ...
def getResultsData(condition):
    ...
def _get128CondIcon(iconKey):
    ...
def _get90CondIcon(iconKey):
    ...
def getCondIconBySize(size, iconKey):
    ...
