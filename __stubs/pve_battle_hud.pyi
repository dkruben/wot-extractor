# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/pve_battle_hud.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import logging as logging
from logging import Logger as Logger
import enum as enum
PVE_HUD_LOGGER_NAME = 'PVEBattleHUD'

# decorador original: @enum.unique
class WidgetType(enum.IntEnum):
    ENEMY_LIST = 1
    ALLY_LIST = 2
    MINIMAP = 3
    PROGRESS_COUNTER = 4
    PRIMARY_OBJECTIVE = 5
    SECONDARY_OBJECTIVE = 6
    COUNTDOWN = 7
    CHAT = 8
    BATTLE_COMMUNICATION = 9
    RESPAWN_HUD = 10

# decorador original: @enum.unique
class ProgressCounterState(enum.IntEnum):
    INITIAL = 1
    APPEARANCE = 2
    REGULAR = 3
    HIDDEN = 4

# decorador original: @enum.unique
class PrimaryObjectiveState(enum.IntEnum):
    INITIAL = 1
    APPEARANCE = 2
    REGULAR = 3
    HIDDEN = 4
    REMIND = 5
    LAST_REMIND = 6
    LARGE_TIMER = 7
    COUNTDOWN = 8
    SUCCESS = 9
    FAILURE = 10
    def isCompleted(self):
        ...

# decorador original: @enum.unique
class SecondaryObjectiveState(enum.IntEnum):
    INITIAL = 1
    APPEARANCE = 2
    RESTORED = 3
    REGULAR = 4
    COUNTDOWN = 5
    SUCCESS = 6
    FAILURE = 7
    DISAPPEARANCE = 8
    HIDDEN = 9

def getPveHudLogger():
    ...
