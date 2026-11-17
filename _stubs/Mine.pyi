# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/Mine.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
import BigWorld as BigWorld
import CGF as CGF
from battleground.mines_object import loadMines as loadMines
from entity_world_object import EntityWorldObject as EntityWorldObject
from gui.battle_control import avatar_getter as avatar_getter
from gui.Scaleform.daapi.view.common.battle_royale.br_helpers import getEquipmentById as getEquipmentById
from helpers import dependency as dependency
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from PlayerEvents import g_playerEvents as g_playerEvents
from battle_royale.gui.battle_control.controllers.br_battle_sounds import BREvents as BREvents
from typing import Tuple as Tuple
_logger: Any
DETONATION_TIMER_SPEEDUP_TIME = 30

class Mine(EntityWorldObject):
    battleSession: Any
    __ownerTeam: Any
    __currentObservedVehicleID: Any
    __callbackID: Any
    worldObject: Any
    def __init__(self):
        ...
    def onEnterWorld(self, *args):
        ...
    def onLeaveWorld(self):
        ...
    def set_isDetonated(self, prev=None):
        ...
    def tick(self):
        ...
    @property
    def fieldID(self):
        ...
    def _loadWorldObject(self):
        ...
    def _registerWorldObject(self, worldObject):
        ...
    def __onAvatarReady(self):
        ...
    def __onObservedVehicleChanged(self, observedVehicleID):
        ...

class MineFieldSystem(CGF.System):
    MineActivated: Any
    MineIterate: Any
    Reactions: Any
    __activeMinefields: Any
    def commonUpdate(self):
        ...
    def periodUpdate(self):
        ...
    def __init__(self, *args):
        ...
    def onMineAdded(self, mine):
        ...
    def onMineRemoved(self, mine):
        ...
    def destroy(self):
        ...

class MineField(CallbackDelayer):
    __id: Any
    __detonationTime: Any
    __position: Any
    __minesCount: Any
    __soundObj: Any
    def __init__(self, id_, detonationTime, position):
        ...
    def addMine(self):
        ...
    def removeMine(self):
        ...
    @property
    def hasMines(self):
        ...
    def destroy(self):
        ...
    def __startTimerSound(self):
        ...
    def __setRTPC(self):
        ...
    @property
    def __soundObjectName(self):
        ...
    @property
    def __timeTillDetonation(self):
        ...
