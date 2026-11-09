# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/matchmaker/active_test_confirm_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/matchmaker/active_test_confirm_view_model.py
from gui.impl.gen.view_models.windows.full_screen_dialog_window_model import FullScreenDialogWindowModel

class ActiveTestConfirmViewModel(FullScreenDialogWindowModel):
    __slots__ = ('onOpenPortalClicked', )

    def __init__(self, properties=14, commands=4):
        super(ActiveTestConfirmViewModel, self).__init__(properties=properties, commands=commands)

    def getClusterName(self):
        return self._getString(11)

    def setClusterName(self, value):
        self._setString(11, value)

    def getTimeRangeStart(self):
        return self._getNumber(12)

    def setTimeRangeStart(self, value):
        self._setNumber(12, value)

    def getTimeRangeEnd(self):
        return self._getNumber(13)

    def setTimeRangeEnd(self, value):
        self._setNumber(13, value)

    def _initialize(self):
        super(ActiveTestConfirmViewModel, self)._initialize()
        self._addStringProperty('clusterName', '')
        self._addNumberProperty('timeRangeStart', 0)
        self._addNumberProperty('timeRangeEnd', 0)
        self.onOpenPortalClicked = self._addCommand('onOpenPortalClicked')
