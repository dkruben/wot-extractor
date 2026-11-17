# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/AvatarInputHandler/commands/dualgun_control.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import BigWorld as BigWorld
import CommandMapping as CommandMapping
from AvatarInputHandler.commands.input_handler_command import InputHandlerCommand as InputHandlerCommand
from constants import DUAL_GUN as DUAL_GUN, DUALGUN_CHARGER_ACTION_TYPE as DUALGUN_CHARGER_ACTION_TYPE, DUALGUN_CHARGER_STATUS as DUALGUN_CHARGER_STATUS
from gui.battle_control import event_dispatcher as gui_event_dispatcher
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
_logger: Any

class ShotStates(object):
    PREPARING = 0
    DISABLED = 1

class ShotController(CallbackDelayer):
    __SINGLE_SHOT_THRESHOLD_DEFAULT = 0.5
    __PRE_CHARGE_INDICATION_DEFAULT = 0.25
    __CHARGE_CANCEL_TIME_DEFAULT = 0.18
    isLocked: Any
    __state: Any
    __singleShotThreshold: Any
    __preChargeIndicationDelay: Any
    __chargeCancelTime: Any
    __shotUnavailable: Any
    def __init__(self, threshold=..., preChargeIndication=..., chargeCancelTime=...):
        ...
    def updateState(self, state, value):
        ...
    def shootKeyEvent(self, actionType):
        ...
    def __applyShoot(self):
        ...
    def __setShootAvailable(self):
        ...
    def __disable(self, direct=False):
        ...

class DualGunController(InputHandlerCommand):
    isShotLocked: Any
    __activeGun: Any
    __shotControl: Any
    def __init__(self, typeDescr):
        ...
    def updateChargeState(self, state, value):
        ...
    def handleKeyEvent(self, isDown, key, mods, event=None):
        ...
    def cancelShootKeyEvent(self):
        ...
