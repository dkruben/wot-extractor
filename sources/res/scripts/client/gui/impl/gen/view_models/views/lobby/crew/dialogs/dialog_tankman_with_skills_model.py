# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/crew/dialogs/dialog_tankman_with_skills_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/dialogs/dialog_tankman_with_skills_model.py
from gui.impl.gen.view_models.views.lobby.crew.common.crew_skill_list_model import CrewSkillListModel
from gui.impl.gen.view_models.views.lobby.crew.dialogs.dialog_tankman_base_model import DialogTankmanBaseModel

class DialogTankmanWithSkillsModel(DialogTankmanBaseModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(DialogTankmanWithSkillsModel, self).__init__(properties=properties, commands=commands)

    @property
    def skillList(self):
        return self._getViewModel(6)

    @staticmethod
    def getSkillListType():
        return CrewSkillListModel

    def _initialize(self):
        super(DialogTankmanWithSkillsModel, self)._initialize()
        self._addViewModelProperty('skillList', CrewSkillListModel())
