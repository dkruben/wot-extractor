# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/markers2d/timer.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import math as math
from gui.Scaleform.daapi.view.battle.shared.timers_common import PythonTimer as PythonTimer

class MarkerTimer(PythonTimer):
    __slots__: tuple
    __animated: Any
    __statusID: Any
    __vehicleID: Any
    __showCountdown: Any
    __isSourceVehicle: Any
    def __init__(self, viewObject, vehicleID, typeID, totalTime, currentInterval=1.0, animated=True, statusID=0, showCountdown=True, isSourceVehicle=False):
        ...
    def getStatusID(self):
        ...
    def remove(self):
        ...
    def _showView(self, isBubble=True):
        ...
    def _hideView(self):
        ...
    def _setViewSnapshot(self, timeLeft):
        ...
