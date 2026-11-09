# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/common/settings_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/common/settings_model.py
from frameworks.wulf import ViewModel

class SettingsModel(ViewModel):
    __slots__ = ('onUpdateSetting', )

    def __init__(self, properties=1, commands=1):
        super(SettingsModel, self).__init__(properties=properties, commands=commands)

    def getReadOnly(self):
        return self._getBool(0)

    def setReadOnly(self, value):
        self._setBool(0, value)

    def _initialize(self):
        super(SettingsModel, self)._initialize()
        self._addBoolProperty('readOnly', False)
        self.onUpdateSetting = self._addCommand('onUpdateSetting')
