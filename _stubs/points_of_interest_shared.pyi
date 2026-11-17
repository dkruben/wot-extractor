# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/points_of_interest_shared.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import enum as enum
ENEMY_VEHICLE_ID = -1
INVALID_TIMESTAMP = -1
POI_EQUIPMENT_TAG = 'poiEquipment'
INT_2_POI_STATUS: dict
PoiEquipmentNamesByPoiType: dict
PoiTypesByPoiEquipmentName: dict

# decorador original: @enum.unique
class PoiType(enum.IntEnum):
    ARTILLERY = 1
    RECON = 2
    ILLUMINATION_FLARE = 3

# decorador original: @enum.unique
class PoiStatus(enum.IntEnum):
    ACTIVE = 1
    CAPTURING = 2
    COOLDOWN = 3

# decorador original: @enum.unique
class PoiBlockReasons(enum.IntEnum):
    DAMAGE = 1
    EQUIPMENT = 2
    OVERTURNED = 3
