# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/client/story_mode/gui/impl/gen/view_models/views/lobby/icon_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/client/story_mode/gui/impl/gen/view_models/views/lobby/icon_model.py
from frameworks.wulf import ViewModel

class IconModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(IconModel, self).__init__(properties=properties, commands=commands)

    def getSmall(self):
        return self._getString(0)

    def setSmall(self, value):
        self._setString(0, value)

    def getBig(self):
        return self._getString(1)

    def setBig(self, value):
        self._setString(1, value)

    def _initialize(self):
        super(IconModel, self)._initialize()
        self._addStringProperty('small', '')
        self._addStringProperty('big', '')
