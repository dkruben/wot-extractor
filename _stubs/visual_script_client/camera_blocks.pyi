# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/visual_script_client/camera_blocks.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from visual_script import ASPECT as ASPECT
from visual_script.block import Block as Block, Meta as Meta
from visual_script.dependency import dependencyImporter as dependencyImporter
from visual_script.slot_types import SLOT_TYPE as SLOT_TYPE
utils: Any
dependency: Any
cameras: Any
hangar_camera_manager: Any
CGF: Any
game_control: Any
lock_overlays: Any
InputHandler: Any
Keys: Any

class CameraMeta(Meta):
    @classmethod
    def blockColor(cls):
        ...
    @classmethod
    def blockCategory(cls):
        ...
    @classmethod
    def blockIcon(cls):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class GetCamera(Block, CameraMeta):
    hangarSpace: Any
    _position: Any
    _direction: Any
    def __init__(self, *args, **kwargs):
        ...
    def _getPosition(self):
        ...
    def _getDirection(self):
        ...

class SwitchCamera(Block, CameraMeta):
    _in: Any
    _cameraName: Any
    _spaceId: Any
    _instantly: Any
    _out: Any
    def __init__(self, *args, **kwargs):
        ...
    def _execute(self):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class ActivateCameraWithOverlay(Block, CameraMeta):
    overlay: Any
    _in: Any
    _cameraName: Any
    _spaceId: Any
    _out: Any
    _onCancel: Any
    def __init__(self, *args, **kwargs):
        ...
    def onStartScript(self):
        ...
    def onFinishScript(self):
        ...
    def _handleKeyEvent(self, event):
        ...
    def _execute(self):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class DeactivateCameraWithOverlay(Block, CameraMeta):
    overlay: Any
    _in: Any
    _spaceId: Any
    _out: Any
    def __init__(self, *args, **kwargs):
        ...
    def _execute(self):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class OnCameraSwitched(Block, CameraMeta):
    _in: Any
    _spaceID: Any
    _out: Any
    _cameraName: Any
    def __init__(self, *args, **kwargs):
        ...
    def _initialize(self):
        ...
    def _onCameraSwitched(self, cameraName):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class GetCameraName(Block, CameraMeta):
    _spaceId: Any
    _cameraName: Any
    def __init__(self, *args, **kwargs):
        ...
    def _execute(self):
        ...
    @classmethod
    def blockAspects(cls):
        ...
