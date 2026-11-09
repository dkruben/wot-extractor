# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/client/frontline/gui/impl/gen/view_models/views/lobby/components/alert_message_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/client/frontline/gui/impl/gen/view_models/views/lobby/components/alert_message_model.py
from frameworks.wulf import ViewModel

class AlertMessageModel(ViewModel):
    __slots__ = ('onClick', )

    def __init__(self, properties=2, commands=1):
        super(AlertMessageModel, self).__init__(properties=properties, commands=commands)

    def getMessage(self):
        return self._getString(0)

    def setMessage(self, value):
        self._setString(0, value)

    def getButtonLabel(self):
        return self._getString(1)

    def setButtonLabel(self, value):
        self._setString(1, value)

    def _initialize(self):
        super(AlertMessageModel, self)._initialize()
        self._addStringProperty('message', '')
        self._addStringProperty('buttonLabel', '')
        self.onClick = self._addCommand('onClick')
