# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/crew/dialogs/recruit_window/confirm_irrelevant_dialog_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/dialogs/recruit_window/confirm_irrelevant_dialog_model.py
from gui.impl.gen.view_models.views.lobby.crew.dialogs.recruit_window.recruit_icon_view_model import RecruitIconViewModel
from gui.impl.gen.view_models.views.lobby.crew.dialogs.tankman_skills_change_base_dialog_model import TankmanSkillsChangeBaseDialogModel

class ConfirmIrrelevantDialogModel(TankmanSkillsChangeBaseDialogModel):
    __slots__ = ()

    def __init__(self, properties=10, commands=2):
        super(ConfirmIrrelevantDialogModel, self).__init__(properties=properties, commands=commands)

    @property
    def iconModel(self):
        return self._getViewModel(8)

    @staticmethod
    def getIconModelType():
        return RecruitIconViewModel

    def getName(self):
        return self._getString(9)

    def setName(self, value):
        self._setString(9, value)

    def _initialize(self):
        super(ConfirmIrrelevantDialogModel, self)._initialize()
        self._addViewModelProperty('iconModel', RecruitIconViewModel())
        self._addStringProperty('name', '')
