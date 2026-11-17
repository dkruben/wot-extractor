# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/Scaleform/daapi/view/battle/minimap/settings.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from constants import LOOT_TYPE as LOOT_TYPE

class BattleRoyaleEntries(object):
    BATTLE_ROYALE_DEATH_ZONE = 'DeathZoneEntry'
    VIEW_RANGE_SECTOR = 'ViewRangeSectorEntry'
    BATTLE_ROYALE_MARKER = 'BRMarkerUI'

class ViewRangeSectorAs3Descr(object):
    AS_ADD_SECTOR = 'as_addSector'
    AS_UPDATE_SECTOR_RADIUS = 'as_updateSectorRadius'
    AS_INIT_ARENA_SIZE = 'as_initArenaSize'

class DeathZonesAs3Descr(object):
    AS_UPDATE_DEATH_ZONES = 'as_updateDeathZones'
    AS_INIT_DEATH_ZONE_SIZE = 'as_initDeathZoneSize'

class MarkersAs3Descr(object):
    AS_UPDATE_RADAR_RADIUS = 'updateRadarRadius'
    AS_PLAY_RADAR_ANIMATION = 'play'
    AS_UPDATE_MARKER = 'updateIcon'
    AS_ADD_MARKER = 'show'
    AS_REMOVE_MARKER = 'hide'
    AS_ADD_MARKER_LOOT_BY_TYPE_ID: dict
    AS_ADD_MARKER_LOOT_BIG_BY_TYPE_ID: dict
    AS_ADD_MARKER_ENEMY_VEHICLE = 'enemyVehicle'
    AS_ADD_MARKER_ENEMY_VEHICLE_BIG = 'enemyVehicle_big'
    AS_ADD_MARKER_SQUAD_VEHICLE = 'squadVehicle'
    AS_ADD_MARKER_BOT_VEHICLE = 'ally_bot_vehicle'
    AS_ADD_MARKER_ENEMY_BOT_VEHICLE = 'botVehicle'
    AS_ADD_MARKER_ENEMY_BOT_VEHICLE_BIG = 'botVehicle_big'
