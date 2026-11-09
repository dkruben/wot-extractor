# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/views/presenters/loadout_panel_presenter/commander_presenter.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/impl/lobby/views/presenters/loadout_panel_presenter/commander_presenter.py
from __future__ import absolute_import
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.impl.gen import R
from gui.impl.pub.view_component import ViewComponent
from helpers import dependency
from items.tankmen import ROLES_BY_SKILLS
from shared_utils import first
from skeletons.gui.app_loader import IAppLoader
from skeletons.gui.game_control import IBattleRoyaleController
from battle_royale.gui.impl.lobby.br_helpers.utils import setEventInfo
from battle_royale.gui.impl.gen.view_models.views.lobby.views.commander_view_model import CommanderViewModel, CommanderPerkModel

class CommanderPresenter(ViewComponent[CommanderViewModel]):
    __battleRoyaleController = dependency.descriptor(IBattleRoyaleController)
    __appLoader = dependency.descriptor(IAppLoader)

    def __init__(self):
        self.__toolTipMgr = self.__appLoader.getApp().getToolTipMgr()
        self.__vehicle = None
        super(CommanderPresenter, self).__init__(model=CommanderViewModel)
        return

    @property
    def viewModel(self):
        return super(CommanderPresenter, self).getViewModel()

    def createToolTip(self, event):
        if event.contentID == R.views.common.tooltip_window.backport_tooltip_content.BackportTooltipContent():
            tooltipId = event.getArgument('tooltipId')
            if tooltipId is None:
                return
            commanderID = self.__getCommanderID()
            if commanderID is None:
                return
            role = first(ROLES_BY_SKILLS[tooltipId])
            args = (tooltipId, role, None, None, False)
            self.__toolTipMgr.onCreateWulfTooltip(TOOLTIPS_CONSTANTS.CREW_PERK_GF, args, event.mouse.positionX, event.mouse.positionY, parent=self.getParentWindow())
            return TOOLTIPS_CONSTANTS.CREW_PERK_GF
        else:
            return super(CommanderPresenter, self).createToolTip(event)

    def _onLoading(self, *args, **kwargs):
        super(CommanderPresenter, self)._onLoading(*args, **kwargs)
        self.__updateModel()

    def _finalize(self):
        super(CommanderPresenter, self)._finalize()
        self.__vehicle = None
        return

    def __updateModel(self):
        if not self.__vehicle:
            return
        with self.viewModel.transaction() as model:
            model.setNation(self.__vehicle.nationName)
            perkList = model.getPerkList()
            perkList.clear()
            commanderSkills = self.__battleRoyaleController.getBrCommanderSkills()
            for skill in commanderSkills:
                perkModel = CommanderPerkModel()
                perkModel.setName(skill.name)
                perkModel.setTooltipID(skill.name)
                perkList.addViewModel(perkModel)

            perkList.invalidate()
            setEventInfo(model.eventInfo)

    def __getCommanderID(self):
        if not self.__vehicle:
            return
        else:
            crew = self.__vehicle.crew
            if crew is None:
                return
            return crew[0][1].invID

    def update(self, vehicle):
        self.__vehicle = vehicle
        self.__updateModel()
