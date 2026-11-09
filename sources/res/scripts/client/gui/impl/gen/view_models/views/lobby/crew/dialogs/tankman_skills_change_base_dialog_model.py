# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/crew/dialogs/tankman_skills_change_base_dialog_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/dialogs/tankman_skills_change_base_dialog_model.py
from gui.impl.gen.view_models.views.dialogs.dialog_template_view_model import DialogTemplateViewModel
from gui.impl.gen.view_models.views.lobby.crew.dialogs.dialog_tankman_with_skills_model import DialogTankmanWithSkillsModel

class TankmanSkillsChangeBaseDialogModel(DialogTemplateViewModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=2):
        super(TankmanSkillsChangeBaseDialogModel, self).__init__(properties=properties, commands=commands)

    @property
    def tankmanBefore(self):
        return self._getViewModel(6)

    @staticmethod
    def getTankmanBeforeType():
        return DialogTankmanWithSkillsModel

    @property
    def tankmanAfter(self):
        return self._getViewModel(7)

    @staticmethod
    def getTankmanAfterType():
        return DialogTankmanWithSkillsModel

    def _initialize(self):
        super(TankmanSkillsChangeBaseDialogModel, self)._initialize()
        self._addViewModelProperty('tankmanBefore', DialogTankmanWithSkillsModel())
        self._addViewModelProperty('tankmanAfter', DialogTankmanWithSkillsModel())
