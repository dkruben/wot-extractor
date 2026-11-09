# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/crew/dialogs/mentor_assignment_dialog_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/dialogs/mentor_assignment_dialog_model.py
from gui.impl.gen.view_models.views.dialogs.dialog_template_view_model import DialogTemplateViewModel
from gui.impl.gen.view_models.views.lobby.crew.dialogs.mentor_assignment_tankman_model import MentorAssignmentTankmanModel

class MentorAssignmentDialogModel(DialogTemplateViewModel):
    __slots__ = ('onInputChange', )

    def __init__(self, properties=14, commands=3):
        super(MentorAssignmentDialogModel, self).__init__(properties=properties, commands=commands)

    @property
    def sourceTankman(self):
        return self._getViewModel(6)

    @staticmethod
    def getSourceTankmanType():
        return MentorAssignmentTankmanModel

    @property
    def targetTankman(self):
        return self._getViewModel(7)

    @staticmethod
    def getTargetTankmanType():
        return MentorAssignmentTankmanModel

    def getNation(self):
        return self._getString(8)

    def setNation(self, value):
        self._setString(8, value)

    def getXpTransfer(self):
        return self._getReal(9)

    def setXpTransfer(self, value):
        self._setReal(9, value)

    def getXpLose(self):
        return self._getReal(10)

    def setXpLose(self, value):
        self._setReal(10, value)

    def getIsConfirmRequire(self):
        return self._getBool(11)

    def setIsConfirmRequire(self, value):
        self._setBool(11, value)

    def getIsSourceMaxXp(self):
        return self._getBool(12)

    def setIsSourceMaxXp(self, value):
        self._setBool(12, value)

    def getIsTargetMaxXp(self):
        return self._getBool(13)

    def setIsTargetMaxXp(self, value):
        self._setBool(13, value)

    def _initialize(self):
        super(MentorAssignmentDialogModel, self)._initialize()
        self._addViewModelProperty('sourceTankman', MentorAssignmentTankmanModel())
        self._addViewModelProperty('targetTankman', MentorAssignmentTankmanModel())
        self._addStringProperty('nation', '')
        self._addRealProperty('xpTransfer', 0.0)
        self._addRealProperty('xpLose', 0.0)
        self._addBoolProperty('isConfirmRequire', False)
        self._addBoolProperty('isSourceMaxXp', False)
        self._addBoolProperty('isTargetMaxXp', False)
        self.onInputChange = self._addCommand('onInputChange')
