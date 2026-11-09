# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/pub/window_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/pub/window_view.py
from __future__ import absolute_import
from frameworks.wulf import View, ViewFlags, ViewSettings
from gui.impl.gen.view_models.windows.window_model import WindowModel
from gui.impl.gen import R

class WindowView(View):
    __slots__ = ()

    def __init__(self, layoutID=R.views.common.standard_window.standard_window.StandardWindow(), flags=ViewFlags.WINDOW_DECORATOR, viewModelClazz=WindowModel):
        super(WindowView, self).__init__(ViewSettings(layoutID, flags, viewModelClazz()))

    @property
    def viewModel(self):
        return super(WindowView, self).getViewModel()
