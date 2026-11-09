# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/ClientSelectableHangarsSwitcher.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import BigWorld as BigWorld
from ClientSelectableObject import ClientSelectableObject as ClientSelectableObject
from helpers import dependency as dependency
from skeletons.gui.game_control import IBattleRoyaleController as IBattleRoyaleController
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
from constants import FESTIVAL_SCENE as FESTIVAL_SCENE, BATTLE_ROYALE_SCENE as BATTLE_ROYALE_SCENE
from gui.shared import g_eventBus as g_eventBus
from gui.hangar_cameras.hangar_camera_common import CameraMovementStates as CameraMovementStates, CameraRelatedEvents as CameraRelatedEvents
_logger: Any

class ClientSelectableHangarsSwitcher(ClientSelectableObject):
    battleRoyale: Any
    hangarSpace: Any
    __postponedMouseClickCallbackID: Any
    __modeSelector: Any
    def __init__(self):
        ...
    def onEnterWorld(self, prereqs):
        ...
    def onLeaveWorld(self):
        ...
    def onMouseClick(self):
        ...
    def __selectRoyaleBattle(self):
        ...
    def __selectRandomBattle(self):
        ...
    def __clear(self):
        ...
    def __onCameraEntityUpdated(self, event):
        ...
    def __isHangarVehicleEntity(self, entityId):
        ...
