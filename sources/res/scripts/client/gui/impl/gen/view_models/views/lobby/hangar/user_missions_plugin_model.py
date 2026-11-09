# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/hangar/user_missions_plugin_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/hangar/user_missions_plugin_model.py
from frameworks.wulf import Array, ViewModel

class UserMissionsPluginModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(UserMissionsPluginModel, self).__init__(properties=properties, commands=commands)

    def getUrl(self):
        return self._getString(0)

    def setUrl(self, value):
        self._setString(0, value)

    def getDependencies(self):
        return self._getArray(1)

    def setDependencies(self, value):
        self._setArray(1, value)

    @staticmethod
    def getDependenciesType():
        return unicode

    def _initialize(self):
        super(UserMissionsPluginModel, self)._initialize()
        self._addStringProperty('url', '')
        self._addArrayProperty('dependencies', Array())
