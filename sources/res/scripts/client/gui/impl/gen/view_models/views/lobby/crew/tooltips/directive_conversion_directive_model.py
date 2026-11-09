# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/crew/tooltips/directive_conversion_directive_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/tooltips/directive_conversion_directive_model.py
from frameworks.wulf import ViewModel

class DirectiveConversionDirectiveModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(DirectiveConversionDirectiveModel, self).__init__(properties=properties, commands=commands)

    def getIcon(self):
        return self._getString(0)

    def setIcon(self, value):
        self._setString(0, value)

    def getUserName(self):
        return self._getString(1)

    def setUserName(self, value):
        self._setString(1, value)

    def _initialize(self):
        super(DirectiveConversionDirectiveModel, self)._initialize()
        self._addStringProperty('icon', '')
        self._addStringProperty('userName', '')
