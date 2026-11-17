# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/debug_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import BattleReplay as BattleReplay
from gui.battle_control.battle_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from gui.battle_control.view_components import IViewComponentsController as IViewComponentsController
from gui.shared.utils.TimeInterval import TimeInterval as TimeInterval
from helpers import dependency as dependency
from skeletons.helpers.statistics import IStatisticsCollector as IStatisticsCollector
_UPDATE_INTERVAL = 0.2

class IDebugPanel(object):
    def updateDebugInfo(self, ping, fps, isLaggingNow, fpsReplay):
        ...

class DebugController(IViewComponentsController):
    statsCollector: Any
    _debugPanelUI: Any
    _timeInterval: Any
    def __init__(self):
        ...
    def getControllerID(self):
        ...
    def startControl(self):
        ...
    def stopControl(self):
        ...
    def setViewComponents(self, debugPanelUI):
        ...
    def clearViewComponents(self):
        ...
    def _update(self):
        ...
