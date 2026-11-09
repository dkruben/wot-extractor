# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/pub/simple_dialog_window.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/pub/simple_dialog_window.py
from __future__ import absolute_import
import typing
from frameworks.wulf import ViewSettings
from gui.impl.gen.resources import R
from gui.impl.gen.view_models.constants.dialog_presets import DialogPresets
from gui.impl.gen.view_models.windows.simple_dialog_window_model import SimpleDialogWindowModel
from gui.impl.pub.dialog_window import DialogContent, DialogFlags
from gui.impl.pub.pure_dialog_window import PureDialogWindow
if typing.TYPE_CHECKING:
    from frameworks.wulf import ViewModel

class SimpleDialogWindow(PureDialogWindow):

    def __init__(self, bottomContent=None, parent=None, balanceContent=None, enableBlur=True, preset=DialogPresets.DEFAULT, flags=DialogFlags.TOP_WINDOW):
        contentSettings = ViewSettings(R.views.common.dialog_view.simple_dialog_content.SimpleDialogContent())
        contentSettings.model = SimpleDialogWindowModel()
        super(SimpleDialogWindow, self).__init__(bottomContent=bottomContent, parent=parent, balanceContent=balanceContent, enableBlur=enableBlur, content=DialogContent(contentSettings), flags=flags)
        self._setPreset(preset)

    @property
    def contentViewModel(self):
        content = self.content
        if content is not None:
            return content.getViewModel()
        else:
            return

    def setFormattedMessage(self, formattedMessage=''):
        if formattedMessage != '':
            self.contentViewModel.setFormattedMessage(formattedMessage)

    def setMessage(self, message, args=None, fmtArgs=None, namedFmtArgs=True):
        model = self.contentViewModel
        model.setMessage(message)
        if fmtArgs:
            self._addArgsOfModel(model.getMessageFmtArgs(), fmtArgs)
            model.setIsMessageFmtArgsNamed(namedFmtArgs)
        elif args:
            self._addArgsOfString(model.getMessageArgs(), args)
