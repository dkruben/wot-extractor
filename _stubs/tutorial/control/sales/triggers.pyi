# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/tutorial/control/sales/triggers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from tutorial.control.triggers import Trigger as Trigger, TriggerWithValidateVar as TriggerWithValidateVar
__all__: tuple

class TimerTrigger(TriggerWithValidateVar):
    __timerCallback: Any
    isRunning: Any
    isSubscribed: Any
    def __init__(self, triggerID, validateVarID, setVarID=None, validateUpdateOnly=False):
        ...
    def run(self):
        ...
    def clear(self):
        ...
    def __updateTimer(self, *args):
        ...

class IsCollectibleVehicleTrigger(Trigger):
    def run(self):
        ...
    def isOn(self, *args):
        ...
    def clear(self):
        ...
    def __onCurrentVehicleChanged(self):
        ...
