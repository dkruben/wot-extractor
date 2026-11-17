# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/LSVehicleSoundComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import SoundGroups as SoundGroups
from last_stand.gui.ls_gui_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from helpers import dependency as dependency
from script_component.DynamicScriptComponent import DynamicScriptComponent as DynamicScriptComponent
from last_stand_common.last_stand_constants import PLAYERS_TEAM as PLAYERS_TEAM, ATTACK_REASON as ATTACK_REASON, OBELISK_ROLE_TAG as OBELISK_ROLE_TAG
from last_stand.gui.sounds import ComponentsHolder as ComponentsHolder
from last_stand.gui.sounds.vehicle_components import LSCommonEnemySounds as LSCommonEnemySounds, LSLootSounds as LSLootSounds, LSObeliskSounds as LSObeliskSounds
from last_stand.gui.sounds.sound_constants import VEHICLE_OBJ_NAME_PATTERN as VEHICLE_OBJ_NAME_PATTERN
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
_VEHICLE_SOUND_COMPONENTS: list

class LSVehicleSoundComponent(DynamicScriptComponent):
    sessionProvider: Any
    _components: Any
    _soundObject: Any
    def __init__(self):
        ...
    def onDestroy(self):
        ...
    @property
    def soundObject(self):
        ...
    @property
    def isEnemy(self):
        ...
    @property
    def soulsContainer(self):
        ...
    @property
    def lsBattleGuiCtrl(self):
        ...
    def onLootFailed(self, lootID, vehicleIDs):
        ...
    def onLootSucceed(self, lootID, vehicleIDs):
        ...
    def _onAvatarReady(self):
        ...
    def onDamageReceived(self, attackerID, attackReasonID, damage):
        ...
    def _onVehicleKilled(self, victimID, *args):
        ...
