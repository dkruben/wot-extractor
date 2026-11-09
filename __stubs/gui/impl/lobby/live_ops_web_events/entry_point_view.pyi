# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/live_ops_web_events/entry_point_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import Event as Event
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings
from gui.Scaleform.daapi.view.meta.LiveOpsWebEventsEntryPointInjectMeta import LiveOpsWebEventsEntryPointInjectMeta as LiveOpsWebEventsEntryPointInjectMeta
from gui.game_control.live_ops_web_events_controller import EventState as EventState
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.live_ops_web_events.entry_point_base import State as State
from gui.impl.gen.view_models.views.lobby.live_ops_web_events.entry_point_view_model import EntryPointViewModel as EntryPointViewModel
from gui.impl.lobby.live_ops_web_events.entry_point_tooltip_view import EntryPointTooltipView as EntryPointTooltipView
from gui.impl.pub import ViewImpl as ViewImpl
from helpers import dependency as dependency
from shared_utils import nextTick as nextTick
from skeletons.gui.game_control import ILiveOpsWebEventsController as ILiveOpsWebEventsController
EVENT_STATE_TO_UI_STATE_MAPPING: dict

class LiveOpsWebEventsEntryPointComponent(LiveOpsWebEventsEntryPointInjectMeta):
    def _onPopulate(self):
        ...
    def _addInjectContentListeners(self):
        ...
    def _removeInjectContentListeners(self):
        ...
    def _makeInjectView(self, *args):
        ...
    # decorador original: @nextTick
    def __createInject(self):
        ...
    def __onViewSizeChanged(self, isSmall):
        ...

class LiveOpsWebEventsEntryPointView(ViewImpl):
    __liveOpsWebEventsController: Any
    onEntryPointSizeChanged: Any
    __isSmall: Any
    def __init__(self, flags=...):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def __updateViewModel(self, setIsSmall=False):
        ...
    def __onSettingsChanged(self):
        ...
    @staticmethod
    def __onClick():
        ...
