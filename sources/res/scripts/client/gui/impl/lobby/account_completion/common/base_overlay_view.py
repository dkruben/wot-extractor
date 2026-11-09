# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/account_completion/common/base_overlay_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/account_completion/common/base_overlay_view.py
import typing
from PlayerEvents import g_playerEvents
from gui.impl.lobby.account_completion.curtain.curtain_base_sub_view import CurtainBaseSubView
from gui.impl.lobby.account_completion.curtain.curtain_view import CurtainWindow
from gui.impl.lobby.account_completion.utils.common import openMenu
if typing.TYPE_CHECKING:
    from gui.impl.gen.view_models.views.lobby.account_completion.common.base_overlay_view_model import BaseOverlayViewModel

class BaseOverlayView(CurtainBaseSubView):
    __slots__ = ('_onClose', )
    _IS_CLOSE_BUTTON_VISIBLE = True

    def __init__(self):
        super(BaseOverlayView, self).__init__()
        self._onClose = None
        return

    @property
    def viewModel(self):
        return super(BaseOverlayView, self).getViewModel()

    def activate(self, onClose=None, *args, **kwargs):
        super(BaseOverlayView, self).activate(*args, **kwargs)
        self._onClose = onClose
        self.viewModel.setIsHidden(self.isHidden)
        g_playerEvents.onAccountBecomeNonPlayer += self._onAccountBecomeNonPlayer
        self.viewModel.onEscapePressed += self._escapePressHandler
        self.viewModel.onCloseClicked += self._closeClickedHandler

    def deactivate(self):
        self.viewModel.onCloseClicked -= self._closeClickedHandler
        self.viewModel.onEscapePressed -= self._escapePressHandler
        g_playerEvents.onAccountBecomeNonPlayer -= self._onAccountBecomeNonPlayer
        self._onClose = None
        super(BaseOverlayView, self).deactivate()
        return

    def hide(self):
        super(BaseOverlayView, self).hide()
        self.viewModel.setIsHidden(True)

    def reveal(self):
        super(BaseOverlayView, self).reveal()
        self.viewModel.setIsHidden(False)

    def _onLoading(self, *args, **kwargs):
        self.viewModel.setIsCloseVisible(self._IS_CLOSE_BUTTON_VISIBLE)
        super(BaseOverlayView, self)._onLoading(*args, **kwargs)

    def _onAccountBecomeNonPlayer(self):
        self.destroyWindow()

    def _escapePressHandler(self):
        if not self._IS_CLOSE_BUTTON_VISIBLE:
            openMenu()

    def _closeClickedHandler(self):
        if self._onClose is not None:
            self._onClose()
        CurtainWindow.getInstance().close()
        return
