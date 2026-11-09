# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/dialogs/sub_views/content/text_warning_content.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/dialogs/sub_views/content/text_warning_content.py
from __future__ import absolute_import
from frameworks.wulf import ViewSettings
from gui.impl.dialogs.dialog_template_utils import toString
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.common.dialogs.sub_views.text_with_warning_view_model import TextWithWarningViewModel
from gui.impl.pub import ViewImpl

class TextWithWarning(ViewImpl):
    __slots__ = ()

    def __init__(self, mainText, warningText=None):
        settings = ViewSettings(R.views.dialogs.sub_views.content.TextWithWarning())
        settings.model = TextWithWarningViewModel()
        settings.kwargs = {'mainText': mainText, 
           'warningText': warningText}
        super(TextWithWarning, self).__init__(settings)

    def _onLoading(self, mainText, warningText, *args, **kwargs):
        super(TextWithWarning, self)._onLoading(*args, **kwargs)
        viewModel = self.getViewModel()
        viewModel.setMainText(toString(mainText))
        if warningText:
            viewModel.setWarningText(toString(warningText))

    def updateText(self, text):
        self.getViewModel().setText(toString(text))
