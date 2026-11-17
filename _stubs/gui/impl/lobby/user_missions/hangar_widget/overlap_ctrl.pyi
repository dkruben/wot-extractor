# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/user_missions/hangar_widget/overlap_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from debug_utils import LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION
from frameworks.wulf import WindowStatus as WindowStatus, WindowLayer as WindowLayer
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from gui.impl.lobby.hangar.states import DefaultHangarState as DefaultHangarState
from helpers import dependency as dependency
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
from skeletons.gui.game_control import IOverlayController as IOverlayController

class OverlapCtrlMixin(object):
    __overlayCtrl: Any
    _hangarSpace: Any
    __RESTRICTED_LAYERS: tuple
    _MIN_WINDOW_WIDTH = 1000
    _MIN_WINDOW_HEIGHT = 600
    __ACTIVE_WINDOW_STATUSES: tuple
    _lobbyStateMachine: Any
    _isInHangar: Any
    __isWindowOverlapped: Any
    __isUpdateQueued: Any
    __deferredUpdates: Any
    __lsmViewAliases: Any
    __isFullUpdate: Any
    _isFinalized: Any
    def __init__(self, *args, **kwargs):
        ...
    def deferUpdate(self, updMethod, *args, **kwargs):
        ...
    def initOverlapCtrl(self):
        ...
    @property
    def readyForAnimations(self):
        ...
    @property
    def hasDeferModelUpdate(self):
        ...
    @property
    def isUpdateQueued(self):
        ...
    def queueUpdate(self):
        ...
    def onWidgetUnmounted(self):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    def _onSpaceCreate(self):
        ...
    def _onVisibleRouteChanged(self, routeInfo):
        ...
    def _onWindowStatusChanged(self, _, newStatus):
        ...
    def _updateWindowOverlapped(self):
        ...
    def _onOverlayStateChanged(self):
        ...
    def _rawUpdate(self):
        ...
    def _updateAll(self):
        ...
    def _updateViewModelIfNeeded(self):
        ...
