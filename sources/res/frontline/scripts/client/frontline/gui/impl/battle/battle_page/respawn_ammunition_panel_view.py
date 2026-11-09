# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/client/frontline/gui/impl/battle/battle_page/respawn_ammunition_panel_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/client/frontline/gui/impl/battle/battle_page/respawn_ammunition_panel_view.py
from __future__ import absolute_import
import typing
from Event import Event, EventManager
from frameworks.wulf import ViewFlags, ViewSettings
from gui.battle_control.event_dispatcher import showIngameMenu
from gui.impl.common.ammunition_panel.ammunition_groups_controller import GROUPS_MAP
from gui.impl.gen import R
from gui.impl.gen.view_models.views.battle.battle_page.respawn_ammunition_panel_view_model import RespawnAmmunitionPanelViewModel
from frontline.gui.impl.battle.battle_page.ammunition_panel.ammunition_panel import FLRespawnAmmunitionPanel
from gui.impl.pub import ViewImpl

class RespawnAmmunitionPanelView(ViewImpl):
    __slots__ = ('onSwitchLayout', '__ammunitionPanel', '__vehicle', '__eventManager')

    def __init__(self, vehicle):
        settings = ViewSettings(layoutID=R.views.battle.battle_page.EpicRespawnAmmunitionPanelView(), flags=ViewFlags.VIEW, model=RespawnAmmunitionPanelViewModel())
        super(RespawnAmmunitionPanelView, self).__init__(settings)
        self.__ammunitionPanel = None
        self.__vehicle = vehicle
        self.__eventManager = EventManager()
        self.onSwitchLayout = Event(self.__eventManager)
        return

    @property
    def viewModel(self):
        return super(RespawnAmmunitionPanelView, self).getViewModel()

    def createToolTip(self, event):
        pass

    def createContextMenu(self, event):
        pass

    def updateViewVehicle(self, vehicle, fullUpdate=True):
        self.__vehicle = vehicle
        self.__ammunitionPanel.update(self.__vehicle, fullUpdate)
        self.__ammunitionPanel.viewModel.setAmmoNotFull(not self.__vehicle.isAmmoFull)
        self.__setVehicleData()

    def _initialize(self, *args, **kwargs):
        super(RespawnAmmunitionPanelView, self)._initialize()
        self.__addListeners()
        self.__ammunitionPanel.initialize()

    def _finalize(self):
        self.__removeListeners()
        self.__ammunitionPanel.finalize()
        super(RespawnAmmunitionPanelView, self)._finalize()

    def _onLoading(self, *args, **kwargs):
        super(RespawnAmmunitionPanelView, self)._onLoading(*args, **kwargs)
        self.__ammunitionPanel = FLRespawnAmmunitionPanel(self.viewModel.ammunitionPanel, self.__vehicle)
        self.__ammunitionPanel.onLoading()
        self.updateViewVehicle(self.__vehicle, fullUpdate=False)

    def _onLoaded(self, *args, **kwargs):
        super(RespawnAmmunitionPanelView, self)._onLoaded(*args, **kwargs)
        self.viewModel.setIsReady(True)

    def __addListeners(self):
        self.viewModel.ammunitionPanel.onChangeSetupIndex += self.__onChangeSetupByButton
        self.viewModel.onEscKeyDown += self.__onEscKeyDown

    def __removeListeners(self):
        self.viewModel.onEscKeyDown -= self.__onEscKeyDown
        self.viewModel.ammunitionPanel.onChangeSetupIndex -= self.__onChangeSetupByButton
        self.__eventManager.clear()

    def __onChangeSetupByButton(self, args):
        hudGroupID, newLayoutIdx = args.get('groupId', None), args.get('currentIndex', None)
        if self.viewModel.getIsDisabled() or hudGroupID is None or newLayoutIdx is None:
            return
        self.__changeSetup(int(hudGroupID), int(newLayoutIdx))
        return

    def __changeSetup(self, hudGroupID, newLayoutIdx=None):
        groupID = GROUPS_MAP[hudGroupID]
        newLayoutIdx = int(newLayoutIdx) or self.__vehicle.setupLayouts.getNextLayoutIndex(groupID)
        if self.__ammunitionPanel.isNewSetupLayoutIndexValid(hudGroupID, newLayoutIdx):
            self.onSwitchLayout(self.__vehicle.intCD, groupID, newLayoutIdx)

    def __setVehicleData(self):
        with self.viewModel.transaction() as model:
            model.vehicleInfo.setVehicleName(self.__vehicle.shortUserName)
            model.vehicleInfo.setVehicleType(self.__vehicle.type)
            model.vehicleInfo.setVehicleLvl(self.__vehicle.level)
            model.vehicleInfo.setIsElite(False)

    def __onEscKeyDown(self):
        showIngameMenu()
