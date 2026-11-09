# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/crew/dialogs/recruit_window/recruit_dialog_template_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/dialogs/recruit_window/recruit_dialog_template_view_model.py
from gui.impl.gen.view_models.views.dialogs.dialog_template_view_model import DialogTemplateViewModel
from gui.impl.gen.view_models.views.lobby.crew.dialogs.recruit_window.recruit_content_view_model import RecruitContentViewModel
from gui.impl.gen.view_models.views.lobby.crew.dialogs.recruit_window.recruit_icon_view_model import RecruitIconViewModel

class RecruitDialogTemplateViewModel(DialogTemplateViewModel):
    __slots__ = ()

    def __init__(self, properties=10, commands=2):
        super(RecruitDialogTemplateViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def recruitContent(self):
        return self._getViewModel(6)

    @staticmethod
    def getRecruitContentType():
        return RecruitContentViewModel

    @property
    def iconModel(self):
        return self._getViewModel(7)

    @staticmethod
    def getIconModelType():
        return RecruitIconViewModel

    def getText(self):
        return self._getString(8)

    def setText(self, value):
        self._setString(8, value)

    def getHasVoiceover(self):
        return self._getBool(9)

    def setHasVoiceover(self, value):
        self._setBool(9, value)

    def _initialize(self):
        super(RecruitDialogTemplateViewModel, self)._initialize()
        self._addViewModelProperty('recruitContent', RecruitContentViewModel())
        self._addViewModelProperty('iconModel', RecruitIconViewModel())
        self._addStringProperty('text', '')
        self._addBoolProperty('hasVoiceover', False)
