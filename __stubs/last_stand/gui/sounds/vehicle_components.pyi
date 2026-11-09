# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/sounds/vehicle_components.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import BigWorld as BigWorld
import SoundGroups as SoundGroups
from last_stand.gui.sounds import SoundComponentBase as SoundComponentBase, playSound as playSound
from last_stand.gui.sounds.sound_constants import BOTS_ENGINE as BOTS_ENGINE, BOTS_EXPLOSION as BOTS_EXPLOSION, LootSounds as LootSounds, ObeliskBattleSound as ObeliskBattleSound

class LSCommonEnemySounds(SoundComponentBase):
    def onAvatarReady(self):
        ...
    def onVehicleKilled(self, victimID, *_):
        ...

class LSObeliskSounds(SoundComponentBase):
    def onDamageReceived(self, attackerID, _, damage):
        ...

class LSLootSounds(SoundComponentBase):
    def onLootSucceed(self, lootID, vehicleIDs):
        ...
