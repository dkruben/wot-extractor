# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_hub/special_shell_param_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_hub/special_shell_param_model.py
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.vehicle_hub.shell_model import ShellModel

class SpecialShellParamModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(SpecialShellParamModel, self).__init__(properties=properties, commands=commands)

    def getShellArray(self):
        return self._getArray(0)

    def setShellArray(self, value):
        self._setArray(0, value)

    @staticmethod
    def getShellArrayType():
        return ShellModel

    def _initialize(self):
        super(SpecialShellParamModel, self)._initialize()
        self._addArrayProperty('shellArray', Array())
