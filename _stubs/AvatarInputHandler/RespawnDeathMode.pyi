# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/AvatarInputHandler/RespawnDeathMode.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
import BigWorld as BigWorld
import GUI as GUI
import SoundGroups as SoundGroups
import BattleReplay as BattleReplay
from AvatarInputHandler import aih_global_binding as aih_global_binding
from AvatarInputHandler.DynamicCameras.ArcadeCamera import ArcadeCamera as ArcadeCamera
from AvatarInputHandler.control_modes import IControlMode as IControlMode
from math_utils import clamp as clamp
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider

class RespawnDeathMode(IControlMode):
    camera: Any
    isEnabled: Any
    curVehicleID: Any
    aimingMode: Any
    guiSessionProvider: Any
    __aimOffset: Any
    __aih: Any
    __cam: Any
    __isEnabled: Any
    __curVehicleID: Any
    _aimingMode: Any
    def __init__(self, dataSection, avatarInputHandler):
        ...
    def create(self):
        ...
    def destroy(self):
        ...
    def enable(self, **args):
        ...
    def disable(self):
        ...
    def handleMouseEvent(self, dx, dy, dz):
        ...
