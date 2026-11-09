# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/lootbox_system/tooltips/entry_point_tooltip_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/lootbox_system/tooltips/entry_point_tooltip_view_model.py
from frameworks.wulf import ViewModel

class EntryPointTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(EntryPointTooltipViewModel, self).__init__(properties=properties, commands=commands)

    def getEventName(self):
        return self._getString(0)

    def setEventName(self, value):
        self._setString(0, value)

    def getIsEnabled(self):
        return self._getBool(1)

    def setIsEnabled(self, value):
        self._setBool(1, value)

    def getEventExpireTime(self):
        return self._getNumber(2)

    def setEventExpireTime(self, value):
        self._setNumber(2, value)

    def _initialize(self):
        super(EntryPointTooltipViewModel, self)._initialize()
        self._addStringProperty('eventName', '')
        self._addBoolProperty('isEnabled', False)
        self._addNumberProperty('eventExpireTime', 0)
