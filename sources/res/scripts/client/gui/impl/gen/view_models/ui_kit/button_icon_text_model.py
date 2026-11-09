# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/ui_kit/button_icon_text_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/ui_kit/button_icon_text_model.py
from gui.impl.gen import R
from gui.impl.gen.view_models.ui_kit.button_common_model import ButtonCommonModel

class ButtonIconTextModel(ButtonCommonModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=2):
        super(ButtonIconTextModel, self).__init__(properties=properties, commands=commands)

    def getIcon(self):
        return self._getResource(6)

    def setIcon(self, value):
        self._setResource(6, value)

    def _initialize(self):
        super(ButtonIconTextModel, self)._initialize()
        self._addResourceProperty('icon', R.invalid())
