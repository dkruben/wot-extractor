# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/auto_shoot_guns/auto_shoot_guns_common.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import SERVER_TICK_LENGTH as SERVER_TICK_LENGTH
DISCRETE_SHOOTING_THRESHOLD = 0.25
BURST_VERIFYING_DELTA = 0.0
BURST_CONFIRMATION_DELTA = 0.5
BURST_CONFIRMATION_TIMEOUT: Any
PROJECTILE_LOG_FREQUENCY_LIMIT = 10
ASSIST_LOG_FREQUENCY_TIMEOUT = 1.0
COMBAT_ACTIONS_DELAY = 1.0

class PROJECTILE_INTERVAL_SETTINGS:
    PROJECTILE_INTERVAL_LIMITS: list
    DEFAULT_PROJECTILE_INTERVAL = SERVER_TICK_LENGTH

class AutoShootGunState(object):
    NONE = 0
    CONTINUOUS_SHOOTING = 1
    DISCRETE_SHOOTING = 2
    DELAY_SHOOT = 3
    NOT_SHOOT = 4
    SHOOTING_STATES: tuple
    NAMES: dict

class AutoShootPredictionState(object):
    NOT_ACTIVE = 0
    ACTIVATION = 1
    ACTIVE = 2
    DEACTIVATION = 3
    COOLDOWN = 4
    ACTIVATED: tuple
    CONFIRMABLE: tuple
    COOLDOWNABLE: tuple
    DISABLEABLE: tuple
    NAMES: dict

def autoShootDynamicAttrFactors():
    ...
