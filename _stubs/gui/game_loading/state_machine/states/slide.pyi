# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_loading/state_machine/states/slide.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import ResMgr as ResMgr
import typing as typing
import game_loading_bindings as game_loading_bindings
from frameworks_common.state_machine import StateFlags as StateFlags
from gui.game_loading import loggers as loggers
from gui.game_loading.resources.consts import InfoStyles as InfoStyles
from gui.game_loading.state_machine.const import TickingMode as TickingMode
from gui.game_loading.state_machine.models import ImageViewSettingsModel as ImageViewSettingsModel
from gui.game_loading.state_machine.states.base import BaseViewResourcesTickingState as BaseViewResourcesTickingState, BaseState as BaseState
from gui.impl.utils.path import normalizeGfImagePath as normalizeGfImagePath
from frameworks_common.state_machine import StateEvent as StateEvent
from gui.game_loading.resources.models import LocalImageModel as LocalImageModel
from gui.game_loading.resources.base import BaseResources as BaseResources
_logger: Any

class StaticSlideState(BaseState):
    __slots__: tuple
    _images: Any
    _image: Any
    _imageViewSettings: Any
    def __init__(self, stateID, images, imageViewSettings, flags=...):
        ...
    @property
    def lastShownImage(self):
        ...
    @property
    def timeLeft(self):
        ...
    def setImage(self, image=None):
        ...
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...

class SlideState(BaseViewResourcesTickingState):
    __slots__: tuple
    _startFromFirstShownImage: Any
    _lastShownImage: Any
    _firstShownImage: Any
    _firstImageToShow: Any
    _imageViewSettings: Any
    def __init__(self, stateID, images, imageViewSettings, flags=..., tickingMode=..., onCompleteEvent=None, startFromFirstShownImage=False):
        ...
    @property
    def lastShownImage(self):
        ...
    def setImage(self, image):
        ...
    def _stop(self):
        ...
    def _selectResource(self):
        ...
    def _beforeView(self):
        ...
    def _view(self, image):
        ...
    def _onMinDurationTimeReached(self):
        ...

def _showImage(image, settings):
    ...
def _isImageFileExists(image):
    ...
