# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/account_completion/curtain/curtain_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from frameworks.wulf import ViewSettings as ViewSettings, WindowLayer as WindowLayer
from gui.hangar_cameras.hangar_camera_common import CameraRelatedEvents as CameraRelatedEvents
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.account_completion.curtain.curtain_view_model import CurtainViewModel as CurtainViewModel, CurtainStateEnum as CurtainStateEnum
from gui.impl.lobby.account_completion.curtain.curtain_base_sub_view import CurtainBaseSubView as CurtainBaseSubView
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.dialog_window import DialogFlags as DialogFlags
from gui.impl.pub.lobby_window import LobbyWindow as LobbyWindow
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, events as events
from helpers import dependency as dependency
from skeletons.gui.game_control import IOverlayController as IOverlayController
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from typing import Optional as Optional, Type as Type, Dict as Dict
_DYN_ACCESSOR = R.views.lobby.account_completion.CurtainView

class CurtainView(ViewImpl, IGlobalListener):
    __slots__: tuple
    _overlay: Any
    _subViews: Any
    _activeSubView: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    @property
    def activeSubView(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _onLoaded(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def setActiveSubView(self, subViewClass, *args, **kwargs):
        ...
    def onUnitFlagsChanged(self, flags, timeLeft):
        ...
    def close(self):
        ...
    def hide(self):
        ...
    def reveal(self):
        ...
    def _activateSubView(self, subView, *args, **kwargs):
        ...
    def _deactivateSubView(self, subView):
        ...
    def _stateTransitionCompleteHandler(self):
        ...
    def _waitingChangedHandler(self, isVisible, msgResID=...):
        ...
    @staticmethod
    def _moveSpaceHandler(args=None):
        ...

class CurtainWindow(LobbyWindow):
    __slots__: tuple
    guiLoader: Any
    def __init__(self):
        ...
    @property
    def content(self):
        ...
    def setSubView(self, subViewClass, *args, **kwargs):
        ...
    def close(self):
        ...
    def hide(self, destroy=False):
        ...
    def reveal(self):
        ...
    @staticmethod
    def getOpenedCurtainView():
        ...
    @staticmethod
    def getInstance():
        ...
    @staticmethod
    def isOpened():
        ...
    @staticmethod
    def getActiveSubView():
        ...
