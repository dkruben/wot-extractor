# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/user_missions/tooltips/daily_reroll_tooltip_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/user_missions/tooltips/daily_reroll_tooltip_model.py
from frameworks.wulf import ViewModel

class DailyRerollTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(DailyRerollTooltipModel, self).__init__(properties=properties, commands=commands)

    def getTimeLeft(self):
        return self._getNumber(0)

    def setTimeLeft(self, value):
        self._setNumber(0, value)

    def getRerollInterval(self):
        return self._getNumber(1)

    def setRerollInterval(self, value):
        self._setNumber(1, value)

    def _initialize(self):
        super(DailyRerollTooltipModel, self)._initialize()
        self._addNumberProperty('timeLeft', 0)
        self._addNumberProperty('rerollInterval', 0)
