# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/dialogs/dialog_focus_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/dialogs/dialog_focus_view_model.py
from gui.impl.gen.view_models.views.dialogs.dialog_base_focus_view_model import DialogBaseFocusViewModel

class DialogFocusViewModel(DialogBaseFocusViewModel):
    __slots__ = ('onTabPressed', )
    NOT_FOCUSED_INDEX = -1
    DEFAULT_FOCUSED_INDEX = 0

    def __init__(self, properties=1, commands=1):
        super(DialogFocusViewModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(DialogFocusViewModel, self)._initialize()
        self.onTabPressed = self._addCommand('onTabPressed')
