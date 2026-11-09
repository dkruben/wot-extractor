# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/crew/crew_banner_widget_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/crew_banner_widget_model.py
from frameworks.wulf import ViewModel

class CrewBannerWidgetModel(ViewModel):
    __slots__ = ('onReset', 'onFill')

    def __init__(self, properties=3, commands=2):
        super(CrewBannerWidgetModel, self).__init__(properties=properties, commands=commands)

    def getSecondsLeft(self):
        return self._getNumber(0)

    def setSecondsLeft(self, value):
        self._setNumber(0, value)

    def getIsFillDisabled(self):
        return self._getBool(1)

    def setIsFillDisabled(self, value):
        self._setBool(1, value)

    def getIsResetDisabled(self):
        return self._getBool(2)

    def setIsResetDisabled(self, value):
        self._setBool(2, value)

    def _initialize(self):
        super(CrewBannerWidgetModel, self)._initialize()
        self._addNumberProperty('secondsLeft', 0)
        self._addBoolProperty('isFillDisabled', False)
        self._addBoolProperty('isResetDisabled', False)
        self.onReset = self._addCommand('onReset')
        self.onFill = self._addCommand('onFill')
