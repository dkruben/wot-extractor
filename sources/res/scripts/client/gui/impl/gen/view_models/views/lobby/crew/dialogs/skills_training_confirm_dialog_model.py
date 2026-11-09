# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/crew/dialogs/skills_training_confirm_dialog_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/dialogs/skills_training_confirm_dialog_model.py
from frameworks.wulf import Array
from gui.impl.gen.view_models.views.dialogs.dialog_template_view_model import DialogTemplateViewModel
from gui.impl.gen.view_models.views.lobby.crew.common.skill.skill_model import SkillModel

class SkillsTrainingConfirmDialogModel(DialogTemplateViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=2):
        super(SkillsTrainingConfirmDialogModel, self).__init__(properties=properties, commands=commands)

    def getSkillsList(self):
        return self._getArray(6)

    def setSkillsList(self, value):
        self._setArray(6, value)

    @staticmethod
    def getSkillsListType():
        return SkillModel

    def _initialize(self):
        super(SkillsTrainingConfirmDialogModel, self)._initialize()
        self._addArrayProperty('skillsList', Array())
