# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/avatar_components/avatar_recovery_mechanic.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from functools import partial as partial
import BigWorld as BigWorld
import CommandMapping as CommandMapping
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as BONUS_CAPS
from constants import RM_STATE as RM_STATE
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE as VEHICLE_VIEW_STATE

class AvatarRecoveryMechanic(object):
    __enabled: Any
    __lastRecoveryArgs: Any
    __keyCheckCallback: Any
    __recoveryRequested: Any
    def __init__(self):
        ...
    def onBecomePlayer(self):
        ...
    def handleKey(self, isDown, key, mods):
        ...
    def onBecomeNonPlayer(self):
        ...
    def notifyCannotStartRecovering(self):
        ...
    def notifyCancelled(self):
        ...
    def updateState(self, activated, state, timerDuration, endOfTimer):
        ...
    def getLastRecoveryArgs(self):
        ...
    def __currentRevcoveryState(self):
        ...
    def __checkKey(self, key, isFirstCheck=False):
        ...
