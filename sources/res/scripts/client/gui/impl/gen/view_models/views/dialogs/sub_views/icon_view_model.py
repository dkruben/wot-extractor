# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/dialogs/sub_views/icon_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/dialogs/sub_views/icon_view_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen import R
from gui.impl.gen.view_models.views.dialogs.sub_views.simple_text_view_model import SimpleTextViewModel

class IconViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(IconViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def iconLabel(self):
        return self._getViewModel(0)

    @staticmethod
    def getIconLabelType():
        return SimpleTextViewModel

    def getPath(self):
        return self._getResource(1)

    def setPath(self, value):
        self._setResource(1, value)

    def _initialize(self):
        super(IconViewModel, self)._initialize()
        self._addViewModelProperty('iconLabel', SimpleTextViewModel())
        self._addResourceProperty('path', R.invalid())
