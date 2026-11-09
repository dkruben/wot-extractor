# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/mode_selector/items/items_constants.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from enum import Enum as Enum
from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_columns import ModeSelectorColumns as ModeSelectorColumns
from gui.prb_control.settings import PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME
DEFAULT_COLUMN = ModeSelectorColumns.COLUMN_2
DEFAULT_PRIORITY = -1
DEFAULT_MODE_SETTING = 'default'
COLUMN_SETTINGS: dict

class ModeSelectorRewardID(Enum):
    BONES = 'bones'
    BOUNTY_EQUIPMENT = 'bountyEquipment'
    CREDITS = 'credits'
    CREW = 'crew'
    EXPERIENCE = 'experience'
    IMPROVED_EQUIPMENT = 'improvedEquipment'
    OTHER = 'other'
    RANDOM = 'random'
    STYLE = 'style'
    PROGRESSION_STYLE = 'progressionStyle'
    VEHICLE = 'vehicle'
    LOOT_BOXES = 'lootBoxes'
    ATTACHMENT = 'attachment'
    EXPERIMENTAL_EQUIPMENT = 'experimentalEquipment'
