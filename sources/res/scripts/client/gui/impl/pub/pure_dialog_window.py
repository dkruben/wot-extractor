# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/pub/pure_dialog_window.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/pub/pure_dialog_window.py
from __future__ import absolute_import
import typing
from gui.impl.gen.resources import R
from gui.impl.gen.view_models.constants.dialog_presets import DialogPresets
from gui.impl.pub.dialog_window import DialogWindow, DialogFlags
if typing.TYPE_CHECKING:
    from frameworks.wulf import ViewModel, Array

class PureDialogWindow(DialogWindow):

    def __init__(self, content=None, bottomContent=None, parent=None, balanceContent=None, enableBlur=True, preset=DialogPresets.DEFAULT, flags=DialogFlags.TOP_FULLSCREEN_WINDOW):
        super(PureDialogWindow, self).__init__(bottomContent=bottomContent, parent=parent, balanceContent=balanceContent, enableBlur=enableBlur, content=content, flags=flags)
        self._setPreset(preset)

    def setTitle(self, title=R.invalid(), args=None, fmtArgs=None, namedFmtArgs=True):
        model = self.viewModel
        if title != R.invalid():
            model.setTitle(title)
        if fmtArgs:
            self._addArgsOfModel(model.getTitleFmtArgs(), fmtArgs)
            model.setIsTitleFmtArgsNamed(namedFmtArgs)
        elif args:
            self._addArgsOfString(model.getTitleArgs(), args)

    def setFormattedTitle(self, formattedTitle=''):
        if formattedTitle != '':
            self.viewModel.setFormattedTitle(formattedTitle)

    def setIcon(self, icon):
        self.viewModel.setIcon(icon)

    def addButton(self, name, label, isFocused=False, invalidateAll=False, soundDown=None, rawLabel=''):
        self._addButton(name, label, isFocused, invalidateAll, soundDown=soundDown, rawLabel=rawLabel)

    def setBackground(self, backImg):
        self.viewModel.setBackgroundImage(backImg)

    def _getResultData(self):
        if self.bottomContentViewModel is not None:
            return self.bottomContentViewModel.getIsSelected()
        else:
            return super(PureDialogWindow, self)._getResultData()

    @staticmethod
    def _addArgsOfModel(arrModel, args):
        for arg in args:
            arrModel.addViewModel(arg)

        arrModel.invalidate()

    @staticmethod
    def _addArgsOfString(arrModel, args):
        for arg in args:
            arrModel.addString(arg)

        arrModel.invalidate()
