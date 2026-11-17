# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/maps_training/maps_training_base_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl.pub import ViewImpl as ViewImpl
from gui.hangar_cameras.hangar_camera_common import CameraRelatedEvents as CameraRelatedEvents
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, events as events
from frameworks.wulf import ViewSettings as ViewSettings, ViewFlags as ViewFlags
from helpers import dependency as dependency
from skeletons.gui.app_loader import IAppLoader as IAppLoader

class MapsTrainingBaseView(ViewImpl):
    appLoader: Any
    _BACKGROUND_ALPHA = 0
    def __init__(self, viewResource, viewModel, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _addListeners(self):
        ...
    def _removeListeners(self):
        ...
    def _onMoveSpace(self, args=None):
        ...
    def _onMouseOver3dScene(self, args):
        ...
