# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/tooltips/clans.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/tooltips/clans.py
from frameworks.wulf import View, ViewFlags, ViewSettings
from gui.impl.gen.view_models.views.lobby.tooltips.clan_short_info_content_model import ClanShortInfoContentModel
from gui.shared.view_helpers.emblems import ClanEmblemsHelper
from gui.impl.gen import R
from helpers import dependency
from skeletons.gui.web import IWebController

class ClanShortInfoTooltipContent(View, ClanEmblemsHelper):
    __webCtrl = dependency.descriptor(IWebController)

    def __init__(self):
        settings = ViewSettings(R.views.lobby.tooltips.clans.ClanShortInfoTooltipContent(), ViewFlags.VIEW, ClanShortInfoContentModel())
        super(ClanShortInfoTooltipContent, self).__init__(settings)
        clanProfile = self.__webCtrl.getAccountProfile()
        self.requestClanEmblem32x32(clanProfile.getClanDbID())
        self.viewModel.setFullName(clanProfile.getClanFullName())

    @property
    def viewModel(self):
        return super(ClanShortInfoTooltipContent, self).getViewModel()

    def onClanEmblem32x32Received(self, clanDbID, emblem):
        if emblem and self.viewModel:
            self.viewModel.setEmblem(self.getMemoryTexturePath(emblem))
