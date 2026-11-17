# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/battle_control/controllers/consumables/epic_equipment_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems, viewvalues as viewvalues
import BigWorld as BigWorld
from constants import EQUIPMENT_STAGES as STAGES
from frontline_common.frontline_constants import FLBattleReservesModifier as FLBattleReservesModifier
from gui.battle_control.controllers.consumables import equipment_ctrl as equipment_ctrl
from gui.shared.utils.MethodsRules import MethodsRules as MethodsRules
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider

class EpicEquipmentsController(equipment_ctrl.EquipmentsController):
    sessionProvider: Any
    slotStage: Any
    def __init__(self, setup):
        ...
    def setServerPrevStage(self, **kwargs):
        ...
    def cancel(self):
        ...
    # decorador original: @MethodsRules.delayable(...)
    def setEquipment(self, intCD, quantity, stage, timeRemaining, totalTime, index=0):
        ...
    # decorador original: @MethodsRules.delayable(...)
    def resetEquipment(self, oldIntCD, newIntCD, quantity, stage, timeRemaining, totalTime, index):
        ...

class EpicReplayEquipmentController(EpicEquipmentsController):
    __slots__: tuple
    __callbackID: Any
    __callbackTimeID: Any
    __percentGetters: Any
    __percents: Any
    __timeGetters: Any
    __times: Any
    def __init__(self, setup):
        ...
    def getEquipmentKey(self, intCD, index):
        ...
    def getEquipmentByKey(self, key):
        ...
    def clear(self, leave=True):
        ...
    # decorador original: @MethodsRules.delayable(...)
    def setEquipment(self, intCD, quantity, stage, timeRemaining, totalTime, index=0):
        ...
    # decorador original: @MethodsRules.delayable(...)
    def resetEquipment(self, oldIntCD, newIntCD, quantity, stage, timeRemaining, totalTime, index):
        ...
    @classmethod
    def createItem(cls, descriptor, quantity, stage, timeRemaining, totalTime):
        ...
    def getActivationCode(self, intCD, entityName=None, avatar=None):
        ...
    def canActivate(self, intCD, entityName=None, avatar=None):
        ...
    def changeSetting(self, intCD, entityName=None, avatar=None, idx=None):
        ...
    def changeSettingByTag(self, tag, entityName=None, avatar=None):
        ...
    def __resetTimers(self, intCD, stage, index):
        ...
    def __timeLoop(self):
        ...
    def __timeLoopInSeconds(self):
        ...
    def __tick(self):
        ...
    def __tickInSeconds(self):
        ...
