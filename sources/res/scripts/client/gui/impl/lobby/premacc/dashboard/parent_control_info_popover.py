# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/premacc/dashboard/parent_control_info_popover.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/premacc/dashboard/parent_control_info_popover.py
from adisp import adisp_process
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.premacc.dashboard.parent_control_info_popover_model import ParentControlInfoPopoverModel
from gui.impl.pub import PopOverViewImpl
from helpers import dependency
from skeletons.gui.game_control import IExternalLinksController
_PARENT_CONTROL_HELP_URL = 'parentControlHelpURL'

class ParentControlInfoPopoverContent(PopOverViewImpl):
    __slots__ = ()
    __links = dependency.descriptor(IExternalLinksController)

    def __init__(self):
        settings = ViewSettings(R.views.lobby.premacc.dashboard.prem_dashboard_parent_control_info.PremDashboardParentControlInfoContent())
        settings.model = ParentControlInfoPopoverModel()
        super(ParentControlInfoPopoverContent, self).__init__(settings)

    @property
    def viewModel(self):
        return super(ParentControlInfoPopoverContent, self).getViewModel()

    def _initialize(self):
        super(ParentControlInfoPopoverContent, self)._initialize()
        self.viewModel.onLinkClicked += self.__onLinkClicked

    def _finalize(self):
        self.viewModel.onLinkClicked -= self.__onLinkClicked

    @adisp_process
    def __onLinkClicked(self):
        parsedUrl = yield self.__links.getURL(_PARENT_CONTROL_HELP_URL)
        self.__links.open(parsedUrl)
