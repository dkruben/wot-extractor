# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/AvatarInputHandler/remote_camera_sender.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
import BigWorld as BigWorld
from BigWorld import ArcadeAimingSystem as ArcadeAimingSystem, SniperAimingSystem as SniperAimingSystem, DualGunAimingSystem as DualGunAimingSystem, StrategicAimingSystem as StrategicAimingSystem, ArtyAimingSystem as ArtyAimingSystem, TwinGunAimingSystem as TwinGunAimingSystem
from aih_constants import CTRL_MODES as CTRL_MODES
from AvatarInputHandler.commands.input_handler_command import InputHandlerCommand as InputHandlerCommand
from AvatarInputHandler.control_modes import ArcadeControlMode as ArcadeControlMode, SniperControlMode as SniperControlMode, DualGunControlMode as DualGunControlMode, TwinGunControlMode as TwinGunControlMode, StrategicControlMode as StrategicControlMode, ArtyControlMode as ArtyControlMode
from AvatarInputHandler.MapCaseMode import MapCaseControlModeBase as MapCaseControlModeBase
from system_events import g_systemEvents as g_systemEvents

class RemoteCameraSender(InputHandlerCommand):
    __aih: Any
    def __init__(self, avatarInputHandler):
        ...
    def destroy(self):
        ...
    def __sendCameraData(self):
        ...
