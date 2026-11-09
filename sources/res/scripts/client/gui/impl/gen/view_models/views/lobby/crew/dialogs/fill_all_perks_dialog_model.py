# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/crew/dialogs/fill_all_perks_dialog_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/dialogs/fill_all_perks_dialog_model.py
from frameworks.wulf import Array
from gui.impl.gen.view_models.views.dialogs.dialog_template_view_model import DialogTemplateViewModel
from gui.impl.gen.view_models.views.lobby.crew.dialogs.fill_all_perks_dialog_row import FillAllPerksDialogRow

class FillAllPerksDialogModel(DialogTemplateViewModel):
    __slots__ = ('onChange', )

    def __init__(self, properties=9, commands=3):
        super(FillAllPerksDialogModel, self).__init__(properties=properties, commands=commands)

    def getRows(self):
        return self._getArray(6)

    def setRows(self, value):
        self._setArray(6, value)

    @staticmethod
    def getRowsType():
        return FillAllPerksDialogRow

    def getAppliedForBarracks(self):
        return self._getBool(7)

    def setAppliedForBarracks(self, value):
        self._setBool(7, value)

    def getAreBarracksEmpty(self):
        return self._getBool(8)

    def setAreBarracksEmpty(self, value):
        self._setBool(8, value)

    def _initialize(self):
        super(FillAllPerksDialogModel, self)._initialize()
        self._addArrayProperty('rows', Array())
        self._addBoolProperty('appliedForBarracks', False)
        self._addBoolProperty('areBarracksEmpty', False)
        self.onChange = self._addCommand('onChange')
