# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/seniority_awards/notifications/available_tokens_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/seniority_awards/notifications/available_tokens_model.py
from gui.impl.gen.view_models.common.notification_base_model import NotificationBaseModel

class AvailableTokensModel(NotificationBaseModel):
    __slots__ = ('onClick', 'onClose')

    def __init__(self, properties=3, commands=2):
        super(AvailableTokensModel, self).__init__(properties=properties, commands=commands)

    def getTimeLeft(self):
        return self._getNumber(1)

    def setTimeLeft(self, value):
        self._setNumber(1, value)

    def getCount(self):
        return self._getNumber(2)

    def setCount(self, value):
        self._setNumber(2, value)

    def _initialize(self):
        super(AvailableTokensModel, self)._initialize()
        self._addNumberProperty('timeLeft', 0)
        self._addNumberProperty('count', 0)
        self.onClick = self._addCommand('onClick')
        self.onClose = self._addCommand('onClose')
