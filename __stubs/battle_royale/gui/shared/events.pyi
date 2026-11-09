# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/shared/events.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.shared.events import HasCtxEvent as HasCtxEvent

class DeathZoneEvent(HasCtxEvent):
    UPDATE_DEATH_ZONE = 'deathZone/update'

class AirDropEvent(HasCtxEvent):
    AIR_DROP_SPAWNED = 'onAirDropSpawned'
    AIR_DROP_LANDED = 'onAirDropLanded'
    AIR_DROP_ENTERED = 'onAirDropEntered'
    AIR_DROP_LEFT = 'onAirDropLeft'
    AIR_DROP_NXT_SPAWNED = 'onAirDropNxtSpawned'

class LootEvent(HasCtxEvent):
    LOOT_PICKED_UP = 'onLootPickedUp'
