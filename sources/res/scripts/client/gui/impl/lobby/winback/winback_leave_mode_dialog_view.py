# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/winback/winback_leave_mode_dialog_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/winback/winback_leave_mode_dialog_view.py
from functools import partial
from frameworks.wulf import ViewFlags, ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.winback.winback_leave_mode_dialog_view_model import WinbackLeaveModeDialogViewModel
from gui.impl.lobby.dialogs.full_screen_dialog_view import FullScreenDialogBaseView
from gui.impl.pub.dialog_window import DialogButtons

class WinbackLeaveModeDialogView(FullScreenDialogBaseView):
    __slots__ = ()

    def __init__(self):
        settings = ViewSettings(R.views.mono.winback.winback_leave_mode_dialog_view())
        settings.flags = ViewFlags.VIEW
        settings.model = WinbackLeaveModeDialogViewModel()
        super(WinbackLeaveModeDialogView, self).__init__(settings)

    @property
    def viewModel(self):
        return super(WinbackLeaveModeDialogView, self).getViewModel()

    def _getEvents(self):
        return (
         (
          self.viewModel.onLeaveMode, partial(self._setResult, DialogButtons.SUBMIT)),
         (
          self.viewModel.onClose, partial(self._setResult, DialogButtons.CANCEL)))
