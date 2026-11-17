# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/hangar/easy_tank_equip_state.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.lobby.hangar.random.sound_manager import EASY_TANK_EQUIP_SOUND_SPACE as EASY_TANK_EQUIP_SOUND_SPACE
from gui.lobby_state_machine.states import LobbyState as LobbyState, LobbyStateDescription as LobbyStateDescription
from helpers.events_handler import EventsHandler as EventsHandler
from sound_gui_manager import ViewSoundExtension as ViewSoundExtension
_logger: Any

class EasyTankEquipStatePrototype(LobbyState, EventsHandler):
    __soundExtension: Any
    def getNavigationDescription(self):
        ...
    def registerTransitions(self):
        ...
    def _getEvents(self):
        ...
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...
    def __onVehicleChanged(self):
        ...

def generateEasyTankEquipStates(hangarStateCls, easyTankEquipStateProtoCls=...):
    ...
