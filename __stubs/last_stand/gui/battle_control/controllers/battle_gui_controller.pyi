# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/battle_control/controllers/battle_gui_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from math_common import decimal_round as decimal_round
from Event import Event as Event
from last_stand.gui.battle_control.controllers.battle_gui_controller_base import LSBattleGUIControllerBase as LSBattleGUIControllerBase
from LSArenaPhasesComponent import LSArenaPhasesComponent as LSArenaPhasesComponent

class LSBattleGoal(object):
    UNKNOWN = None
    DESTROY_ENEMIES = 'last_stand.destroyEnemies'
    STOP_CONVOY = 'last_stand.stopConvoy'
    CONVOY_DESTROYED_ENEMIES_LEFT = 'last_stand.convoyDestroyedEnemiesLeft'
    WAVE_FINISHED = 'last_stand.waveFinished'
    LAST_WAVE_FINISHED = 'last_stand.lastWaveFinished'

class LSBattleGUIController(LSBattleGUIControllerBase):
    MAX_UI_CONVOY_PROGRESS = 100
    _BATTLE_GOALS_WITHOUT_TIMER: list
    onEnemiesInfoChanged: Any
    onHealthBreakpointsChanged: Any
    onEnemiesStatusChanged: Any
    onConvoyStatusChanged: Any
    onConvoyHealthChanged: Any
    onConvoyDistanceIndicatorChanged: Any
    onClearObeliskVehicleMarker: Any
    _enemiesInfo: Any
    _healthBreakpoints: Any
    _enemiesStatus: Any
    _convoyStatus: Any
    _convoyDestroyed: Any
    def __init__(self):
        ...
    def getEnemiesInfo(self):
        ...
    def updateEnemiesInfo(self, enemiesInfo):
        ...
    def updateConvoyStatus(self, convoyStatus):
        ...
    def updateConvoyDistanceIndicator(self, value):
        ...
    def updateConvoyHealth(self, value):
        ...
    def updateHealthBreakpoints(self, healthBreakpoints):
        ...
    def updateEnemiesStatus(self, enemiesStatus):
        ...
    def _getRelevantGoal(self):
        ...
    def _getHintParams(self):
        ...
    def _removeBattleCommunicationMarkers(self):
        ...
