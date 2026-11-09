# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/crew/dialogs/fill_all_perks_dialog_row.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/dialogs/fill_all_perks_dialog_row.py
from frameworks.wulf import Array, ViewModel

class FillAllPerksDialogRow(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(FillAllPerksDialogRow, self).__init__(properties=properties, commands=commands)

    def getRole(self):
        return self._getString(0)

    def setRole(self, value):
        self._setString(0, value)

    def getSkills(self):
        return self._getArray(1)

    def setSkills(self, value):
        self._setArray(1, value)

    @staticmethod
    def getSkillsType():
        return unicode

    def _initialize(self):
        super(FillAllPerksDialogRow, self)._initialize()
        self._addStringProperty('role', '')
        self._addArrayProperty('skills', Array())
