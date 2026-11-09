# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/post_progression/dialogs/research_steps_dialog.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/post_progression/dialogs/research_steps_dialog.py
from gui.impl.gen.view_models.views.lobby.post_progression.dialogs.research_steps_main_content import ResearchStepsMainContent
from gui.impl.gen.view_models.views.lobby.tank_setup.common.deal_panel_model import DealPanelModel
from gui.impl.gen.view_models.windows.full_screen_dialog_window_model import FullScreenDialogWindowModel

class ResearchStepsDialog(FullScreenDialogWindowModel):
    __slots__ = ()

    def __init__(self, properties=13, commands=3):
        super(ResearchStepsDialog, self).__init__(properties=properties, commands=commands)

    @property
    def dealPanel(self):
        return self._getViewModel(11)

    @staticmethod
    def getDealPanelType():
        return DealPanelModel

    @property
    def mainContent(self):
        return self._getViewModel(12)

    @staticmethod
    def getMainContentType():
        return ResearchStepsMainContent

    def _initialize(self):
        super(ResearchStepsDialog, self)._initialize()
        self._addViewModelProperty('dealPanel', DealPanelModel())
        self._addViewModelProperty('mainContent', ResearchStepsMainContent())
