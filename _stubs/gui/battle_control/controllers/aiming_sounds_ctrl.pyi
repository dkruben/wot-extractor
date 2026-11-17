# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/aiming_sounds_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from helpers import dependency as dependency
from gui.battle_control import avatar_getter as avatar_getter
from gui.battle_control.arena_info.interfaces import IAimingSoundsCtrl as IAimingSoundsCtrl
from gui.battle_control.battle_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
_AIMING_SOUND = 'sight_convergence'
_DUAL_ACC_SOUND = 'dual_aiming'
_EMPTY_SOUND = ''

class AimingSoundsCtrl(IAimingSoundsCtrl):
    __sessionProvider: Any
    __isAimingEnded: Any
    __isDualAimingEnded: Any
    def __init__(self):
        ...
    def getControllerID(self):
        ...
    def updateDispersion(self, shotFactor, multFactor, aimingFactor, idealFactor, dualAccMultFactor, dualAccFactor, idealDualAccFactor, hasDualAcc):
        ...
    def __setAimingEnded(self, value):
        ...
    def __setDualAimingEnded(self, value):
        ...
    def __playSoundNotification(self, notification):
        ...
    def __updateDispersion(self, multFactor, aimingFactor, idealFactor, aimingSetter, notification, skipNotification):
        ...
