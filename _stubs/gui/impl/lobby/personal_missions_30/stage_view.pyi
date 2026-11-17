# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/personal_missions_30/stage_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from typing import TYPE_CHECKING as TYPE_CHECKING
import SoundGroups as SoundGroups
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings, WindowFlags as WindowFlags, WindowLayer as WindowLayer
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.personal_missions_30.assembling_video_view_model import AssemblingVideoViewModel as AssemblingVideoViewModel
from gui.impl.lobby.personal_missions_30.views_helpers import setVideoOverlayOn as setVideoOverlayOn, setVideoOverlayOff as setVideoOverlayOff
from gui.impl.pub import ViewImpl as ViewImpl, WindowImpl as WindowImpl
from typing import Callable as Callable, Optional as Optional

class AssemblingVideoView(ViewImpl):
    operationID: Any
    stageNumber: Any
    closingCallback: Any
    def __init__(self, layoutID, operationID, stageNumber, closingCallback=None):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    def __startAssembling(self):
        ...

class AssemblingVideoViewWindow(WindowImpl):
    def __init__(self, operationID, stageNumber, closingCallback=None):
        ...
