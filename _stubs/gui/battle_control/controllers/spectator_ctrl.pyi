# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/spectator_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import Event as Event
import BattleReplay as BattleReplay
from gui.battle_control.battle_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from gui.battle_control.view_components import ViewComponentsController as ViewComponentsController
from gui.Scaleform.genConsts.EPIC_CONSTS import EPIC_CONSTS as EPIC_CONSTS
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import GameEvent as GameEvent, DeathCamEvent as DeathCamEvent
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider

class SPECTATOR_MODE(object):
    NONE = EPIC_CONSTS.TARGET_NONE
    FREECAM = EPIC_CONSTS.SPECTATOR_MODE_FREECAM
    FOLLOW = EPIC_CONSTS.SPECTATOR_MODE_FOLLOW

class ISpectatorViewListener(object):
    def updateSpeedLevel(self, newSpeedLevel):
        ...

class SpectatorViewController(ViewComponentsController):
    _sessionProvider: Any
    spectatorViewMode: Any
    __plugins: Any
    __eManager: Any
    __mode: Any
    __vehicleID: Any
    __currentSpeedGear: Any
    onSpectatorViewModeChanged: Any
    onFreeCameraMoved: Any
    onFreeCameraVerticalMoved: Any
    def __init__(self):
        ...
    def markerWasHovered(self, isHovered, targetID):
        ...
    def toggleFollowHint(self, toggle):
        ...
    def getCurrentSpeedGear(self):
        ...
    def spectatorViewModeChanged(self, mode):
        ...
    def freeCamSpeedLevelChanged(self, newSpeedLevel):
        ...
    def freeCamMoved(self):
        ...
    def freeCamVerticalMoved(self):
        ...
    def getControllerID(self):
        ...
    def startControl(self):
        ...
    def stopControl(self):
        ...
    def __getViewMode(self):
        ...
