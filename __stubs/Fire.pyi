# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/Fire.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import random as random
import weakref as weakref
import BigWorld as BigWorld
import CGF as CGF
from constants import FIRE_NOTIFICATION_CODES as FIRE_NOTIFICATION_CODES
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
import Statuses as Statuses
import TriggersManager as TriggersManager
from TriggersManager import TRIGGER_TYPE as TRIGGER_TYPE
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE as VEHICLE_VIEW_STATE

class Fire(BigWorld.DynamicScriptComponent):
    __guiSessionProvider: Any
    __FIRE_SOUNDS: dict
    __EXTENDED_NOTIFICATION_WINDOW = 1
    __effectListPlayerRef: Any
    def __init__(self):
        ...
    def __tryShowFlameEffect(self):
        ...
    def set_fireInfo(self, _=None):
        ...
    def onLeaveWorld(self):
        ...
    def onDestroy(self):
        ...
    def _cleanup(self):
        ...
    def __getEffectsListPlayer(self):
        ...
    def __playEffect(self):
        ...
    def __stopEffects(self):
        ...
    def __fadeEffects(self):
        ...
    def onUnderWaterSwitch(self, isVehicleUnderwater):
        ...
