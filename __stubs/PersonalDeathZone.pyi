# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/PersonalDeathZone.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import Math as Math
import BigWorld as BigWorld
from AreaOfEffect import AreaOfEffect as AreaOfEffect
import TriggersManager as TriggersManager
from gui.battle_control.battle_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from helpers import dependency as dependency
from math_common import round_py2_style as round_py2_style
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
TRIGGER_NAME_PREFIX = 'personal_deathzone'

class PersonalDeathZone(AreaOfEffect, TriggersManager.ITriggerListener):
    _TRIGGER_NAME_TEMPLATE: Any
    _TRIGGER_TYPE = TriggersManager.TRIGGER_TYPE.CURRENT_VEHICLE_AREA
    _TRIGGER_EXIT_INTERVAL = 1.0
    _TRIGGER_SCALE: tuple
    _TRIGGER_DIRECTION_AXIS = 1
    _guiSessionProvider: Any
    _triggerName: Any
    _triggerId: Any
    _markerItem: Any
    def __init__(self):
        ...
    def onEnterWorld(self, prereqs):
        ...
    def onLeaveWorld(self):
        ...
    def onTriggerActivated(self, args):
        ...
    def onTriggerDeactivated(self, args):
        ...
    @property
    def adjustedDelay(self):
        ...
    @property
    def delay(self):
        ...
    @property
    def _guiController(self):
        ...
    def _showMarker(self):
        ...
    def _hideMarker(self):
        ...
    def _onVehicleKilled(self, victimID, *_):
        ...
    def _isOwnTrigger(self, args):
        ...
