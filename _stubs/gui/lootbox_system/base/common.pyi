# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/lootbox_system/base/common.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from enum import Enum as Enum
from typing import TYPE_CHECKING as TYPE_CHECKING
from gui.impl.gen import R as R
from helpers import dependency as dependency
from skeletons.gui.game_control import ILootBoxSystemController as ILootBoxSystemController
from typing import Callable as Callable, Dict as Dict, Optional as Optional, Tuple as Tuple
_logger: Any
LOOTBOX_RANDOM_NATIONAL_BLUEPRINT = 'randomNationalBlueprint'
LOOTBOX_RANDOM_NATIONAL_BROCHURE = 'randomNationalBrochure'
LOOTBOX_RANDOM_NATIONAL_GUIDE = 'randomNationalGuide'
LOOTBOX_RANDOM_NATIONAL_CREW_BOOK = 'randomNationalCrewBook'
TEXT_RESOURCE_PREFIX = 'lootbox_'
COUNTRY_CODES_FOR_EXTERNAL_LOOT_LIST: tuple
DEFAULT_EVENT_NAME = 'lootbox_system'
LOOTBOX_COMPENSATION_TOKEN_PREFIX = 'lbs_compensation'
LOOTBOX_COMPENSATION_BONUS = 'lootboxCompensation'
REROLLABLE_BOX_OPEN_COUNT = 1
Views: Any

class NotificationPathPart(str, Enum):
    MAIN = 'serviceChannelMessages'
    AUTOOPEN = 'lootBoxesAutoOpen'
    HEADER = 'header'
    TEXT = 'text'
    COUNT = 'count'

class BonusTypeForPreview(str, Enum):
    VEHICLE = 'vehicles'
    CUSTOMIZATION = 'customizations'

class BonusesLayoutAttrs(object):
    PRIORITY = 'priority'
    RARITY = 'rarity'
    VISIBILITY = 'isVisible'
    OVERRIDE = 'override'
    ID = 'id'
    MAIN: tuple

class ViewID(str, Enum):
    INTRO = 'intro'
    MAIN = 'main'
    INFO = 'info'
    AUTOOPEN = 'autoopen'
    SHOP = 'shop'

class _ViewsResolver(object):
    __loaders: Any
    def __init__(self):
        ...
    def load(self, viewID, *args, **kwargs):
        ...
    def getLoader(self, viewID):
        ...
    def setLoader(self, viewID, func):
        ...
    def setLoaders(self, loaders):
        ...
    def clear(self):
        ...

# decorador original: @dependency.replace_none_kwargs(...)
def getTextResource(path, eventName, lootBoxes=None):
    ...
