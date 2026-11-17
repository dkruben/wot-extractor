# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/wotlda/constants.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import enum as enum
from future.utils import listvalues as listvalues
EQUIPMENT_ARCHETYPE_1 = 'equipment_archetype_id_1'
EQUIPMENT_ARCHETYPE_2 = 'equipment_archetype_id_2'
EQUIPMENT_ARCHETYPE_3 = 'equipment_archetype_id_3'
LOADOUT_USAGE_PERCENTAGE = 'usage_percentage'
LAST_UPDATE_TIMESTAMP = 'updated_at'
ExpectedArchetypes: set

class SupportedWotldaLoadoutType(enum.Enum):
    EASY_TANK_EQUIP = 'easy_tank_equip'
    RANDOM = 'random'
    ONSLAUGHT = 'comp7'
    CREW = 'crew'

class SupportedWTRRange(enum.Enum):
    GOLD = 'gold'
    LEGEND = 'legend'
    @staticmethod
    def allRanges():
        ...

class OptDeviceAssistType(enum.Enum):
    NODATA = 0
    NORMAL = 1
    LINKED = 2
    COMBINED = 3
