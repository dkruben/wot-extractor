# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/pet_system/event_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/pet_system/event_view_model.py
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.icon_bonus_model import IconBonusModel

class EventViewModel(ViewModel):
    __slots__ = ('onClose', )

    def __init__(self, properties=3, commands=1):
        super(EventViewModel, self).__init__(properties=properties, commands=commands)

    def getRewards(self):
        return self._getArray(0)

    def setRewards(self, value):
        self._setArray(0, value)

    @staticmethod
    def getRewardsType():
        return IconBonusModel

    def getEventId(self):
        return self._getNumber(1)

    def setEventId(self, value):
        self._setNumber(1, value)

    def getEventType(self):
        return self._getString(2)

    def setEventType(self, value):
        self._setString(2, value)

    def _initialize(self):
        super(EventViewModel, self)._initialize()
        self._addArrayProperty('rewards', Array())
        self._addNumberProperty('eventId', 0)
        self._addStringProperty('eventType', '')
        self.onClose = self._addCommand('onClose')
