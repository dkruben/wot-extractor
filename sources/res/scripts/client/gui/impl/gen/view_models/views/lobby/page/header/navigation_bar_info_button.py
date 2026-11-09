# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/page/header/navigation_bar_info_button.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/page/header/navigation_bar_info_button.py
from enum import Enum
from frameworks.wulf import ViewModel

class ButtonType(Enum):
    INFO = 'Info'
    QUESTION = 'Question'
    VIDEO = 'Video'
    DROP_LIST = 'Drop_List'


class NavigationBarInfoButton(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(NavigationBarInfoButton, self).__init__(properties=properties, commands=commands)

    def getLabel(self):
        return self._getString(0)

    def setLabel(self, value):
        self._setString(0, value)

    def getTooltipHeader(self):
        return self._getString(1)

    def setTooltipHeader(self, value):
        self._setString(1, value)

    def getTooltipBody(self):
        return self._getString(2)

    def setTooltipBody(self, value):
        self._setString(2, value)

    def getType(self):
        return ButtonType(self._getString(3))

    def setType(self, value):
        self._setString(3, value.value)

    def _initialize(self):
        super(NavigationBarInfoButton, self)._initialize()
        self._addStringProperty('label', '')
        self._addStringProperty('tooltipHeader', '')
        self._addStringProperty('tooltipBody', '')
        self._addStringProperty('type', ButtonType.INFO.value)
