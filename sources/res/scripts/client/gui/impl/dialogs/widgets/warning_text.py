# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/dialogs/widgets/warning_text.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/dialogs/widgets/warning_text.py
from __future__ import absolute_import
from frameworks.wulf import ViewSettings
from gui.impl.dialogs.dialog_template_utils import toString
from gui.impl.gen import R
from gui.impl.gen.view_models.views.dialogs.sub_views.simple_text_view_model import SimpleTextViewModel
from gui.impl.pub import ViewImpl

class WarningText(ViewImpl):
    __slots__ = ('__text', )
    LAYOUT_DYN_ACCESSOR = R.views.dialogs.widgets.WarningText

    def __init__(self, text, layoutID=None):
        settings = ViewSettings(layoutID or self.LAYOUT_DYN_ACCESSOR())
        settings.model = SimpleTextViewModel()
        super(WarningText, self).__init__(settings)
        self.__text = text

    @property
    def viewModel(self):
        return self.getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(WarningText, self)._onLoading(*args, **kwargs)
        self.__updateViewModel()

    def __updateViewModel(self):
        with self.viewModel.transaction() as vm:
            vm.setText(toString(self.__text))
