# wot-extractor: codigo DESCOMPILADO de sources/res/open_bundle/scripts/client/open_bundle/gui/impl/gen/view_models/views/lobby/notifications/start_notification_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: open_bundle/scripts/client/open_bundle/gui/impl/gen/view_models/views/lobby/notifications/start_notification_model.py
from gui.impl.gen.view_models.common.notification_base_model import NotificationBaseModel

class StartNotificationModel(NotificationBaseModel):
    __slots__ = ('onOpenBundle', )

    def __init__(self, properties=4, commands=1):
        super(StartNotificationModel, self).__init__(properties=properties, commands=commands)

    def getBundleID(self):
        return self._getNumber(1)

    def setBundleID(self, value):
        self._setNumber(1, value)

    def getBundleType(self):
        return self._getString(2)

    def setBundleType(self, value):
        self._setString(2, value)

    def getIsButtonDisabled(self):
        return self._getBool(3)

    def setIsButtonDisabled(self, value):
        self._setBool(3, value)

    def _initialize(self):
        super(StartNotificationModel, self)._initialize()
        self._addNumberProperty('bundleID', 0)
        self._addStringProperty('bundleType', '')
        self._addBoolProperty('isButtonDisabled', False)
        self.onOpenBundle = self._addCommand('onOpenBundle')
