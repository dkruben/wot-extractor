# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/uilogging/clan_supply/constants.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
FEATURE = 'clan_supply'

class ClanSupplyLogAction(Enum):
    CLOSE = 'close'
    OPEN = 'open'

class ClanSupplyLogKeys(Enum):
    QUESTS_SCREEN = 'tour_task_screen_window'
    PROGRESSION_SCREEN = 'map_screen_window'
    CLAN_LANDING = 'clan_landing'
    NOTIFICATION = 'notification'
    HANGAR_HEADER = 'hangar_header'
    BACK_BUTTON = 'back_button'
    SIDEBAR_PROGRESSION = 'sidebar_map'
    SIDEBAR_QUEST = 'sidebar_quest'
