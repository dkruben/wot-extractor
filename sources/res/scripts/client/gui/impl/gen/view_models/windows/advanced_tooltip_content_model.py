# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/windows/advanced_tooltip_content_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/windows/advanced_tooltip_content_model.py
from frameworks.wulf import ViewModel

class AdvancedTooltipContentModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(AdvancedTooltipContentModel, self).__init__(properties=properties, commands=commands)

    def getShowAnim(self):
        return self._getBool(0)

    def setShowAnim(self, value):
        self._setBool(0, value)

    def _initialize(self):
        super(AdvancedTooltipContentModel, self)._initialize()
        self._addBoolProperty('showAnim', False)
