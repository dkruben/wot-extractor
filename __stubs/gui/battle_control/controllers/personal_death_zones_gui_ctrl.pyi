# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/personal_death_zones_gui_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
from typing import TYPE_CHECKING as TYPE_CHECKING
import BigWorld as BigWorld
from Event import EventManager as EventManager, Event as Event
from gui.battle_control.battle_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from gui.battle_control.controllers.interfaces import IBattleController as IBattleController
import PersonalDeathZone as PersonalDeathZone

class PersonalDeathZonesGUIController(IBattleController):
    __eManager: Any
    onPlayerEnteredDeathZone: Any
    onPlayerLeftDeathZone: Any
    _deathZones: Any
    def __init__(self):
        ...
    def startControl(self, *args):
        ...
    def stopControl(self):
        ...
    def getControllerID(self):
        ...
    @property
    def enteredDeathZones(self):
        ...
    def onPlayerEntered(self, deathZone):
        ...
    def onPlayerLeft(self, deathZone):
        ...
    def _updateWarningNotification(self, zone, visible):
        ...
