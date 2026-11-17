# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/constants.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import enum as enum
ROYALE_POSTBATTLE_REWARDS_COUNT = 8
BR_EQUIPMENTS_WITH_MESSAGES: Any
BR_QUEST_ID_PREFIX = 'token:br:title'
BATTLE_ROYALE_VEHICLES_INVOICE = 'battle_royale_vehicles_invoice'
BR_COIN = 'brcoin'
STP_COIN = 'stpcoin'
SUB_MODE_ID_KEY = 'SubModeId'

class BattleRoyaleEquipments(object):
    LARGE_REPAIRKIT = 'large_repairkit_battle_royale'
    AFTER_BURNING = 'afterburning_battle_royale'
    REGENERATION_KIT = 'regenerationKit'
    SELF_BUFF = 'selfBuff'
    TRAP_POINT = 'trappoint'
    REPAIR_POINT = 'repairpoint'
    HEAL_POINT = 'healPoint'
    SMOKE = 'smoke_battle_royale'
    BOMBER = 'arcade_bomber_with_own_damage_battle_royale'
    KAMIKAZE = 'spawn_kamikaze'
    BERSERKER = 'berserker'
    MINE_FIELD = 'arcade_minefield_battle_royale'
    SMOKE_WITH_DAMAGE = 'arcade_smoke_battle_royale_with_damage'
    ARCADE_SMOKE = 'arcade_smoke_battle_royale'
    FIRE_CIRCLE = 'fireCircle'
    CORRODING_SHOT = 'corrodingShot'
    CLING_BRANDER = 'clingBrander'
    ADAPTATION_HEALTH_RESTORE = 'adaptationHealthRestore'
    THUNDER_STRIKE = 'thunderStrike'
    SHOT_PASSION = 'shotPassion'

class BattleRoyaleComponents(object):
    SHOT_PASSION = 'shotPassionComponent'
    FIRE_CIRCLE = 'vehicleFireCircleEffectComponent'

class AmmoTypes(object):
    BASIC_SHELL = 'bshell'
    PREMIUM_SHELL = 'pshell'
    ITEM = 'item'
    CHARGE1 = 'charge1'
    CHARGE2 = 'charge2'
    CHARGE3 = 'charge3'
    CHARGE4 = 'charge4'
    CHARGES: tuple
    SHELLS: tuple

class BattleRoyalePerfProblems(object):
    HIGH_RISK = 1
    MEDIUM_RISK = 2
    LOW_RISK = 3

class ParamTypes(object):
    DELTA = 'delta'
    CONST = 'const'
    SIMPLE = 'simple'

class BattleRoyaleSubMode(object):
    SOLO_MODE_ID = 1
    SOLO_DYNAMIC_MODE_ID = 2
    SQUAD_MODE_ID = 3
    ALL_RANGE: tuple

class BattleRoyaleModeState(enum.Enum):
    Regular = 0
    CeasefireCurrentServer = 1
    CeasefireAllServers = 2
    Unavailable = 3
    Finished = 4
