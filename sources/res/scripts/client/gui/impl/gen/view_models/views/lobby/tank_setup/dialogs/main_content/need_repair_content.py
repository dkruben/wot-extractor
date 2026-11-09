# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/dialogs/main_content/need_repair_content.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/dialogs/main_content/need_repair_content.py
from frameworks.wulf import ViewModel

class NeedRepairContent(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(NeedRepairContent, self).__init__(properties=properties, commands=commands)

    def getRepairPercentage(self):
        return self._getNumber(0)

    def setRepairPercentage(self, value):
        self._setNumber(0, value)

    def getFreeAutoRepair(self):
        return self._getBool(1)

    def setFreeAutoRepair(self, value):
        self._setBool(1, value)

    def _initialize(self):
        super(NeedRepairContent, self)._initialize()
        self._addNumberProperty('repairPercentage', 0)
        self._addBoolProperty('freeAutoRepair', False)
