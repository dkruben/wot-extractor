# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/impl/battle/vehicle_ban/ban_progression.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/impl/battle/vehicle_ban/ban_progression.py
from __future__ import absolute_import
from comp7.gui.impl.battle.vehicle_ban.ban_helpers import fillBanProgressionModel
from comp7_core.gui.battle_control.controllers.sound_ctrls.comp7_battle_sounds import BAN_PROGRESSION_SOUND_SPACE
from comp7_core.gui.comp7_core_constants import BATTLE_CTRL_ID
from comp7.gui.impl.gen.view_models.views.battle.ban_progression_model import BanProgressionModel
from frameworks.wulf import ViewSettings, WindowFlags
from gui.impl.gen import R
from gui.impl.pub import ViewImpl
from gui.impl.pub.window_impl import WindowImpl
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
from skeletons.gui.game_control import IComp7Controller

class BanProgressionView(ViewImpl):
    __slots__ = ()
    _COMMON_SOUND_SPACE = BAN_PROGRESSION_SOUND_SPACE
    __comp7Controller = dependency.descriptor(IComp7Controller)
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self):
        settings = ViewSettings(R.views.comp7.mono.battle.ban_progression())
        settings.model = BanProgressionModel()
        super(BanProgressionView, self).__init__(settings)

    @property
    def viewModel(self):
        return super(BanProgressionView, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(BanProgressionView, self)._onLoading(*args, **kwargs)
        self.__addListeners()
        self.__updateData()

    def _finalize(self):
        self.__removeListeners()
        super(BanProgressionView, self)._finalize()

    def __addListeners(self):
        self.viewModel.pollServerTime += self.__onPollServerTime
        vehicleBanCtrl = self.__getVehicleBanCtrl()
        if vehicleBanCtrl is not None:
            vehicleBanCtrl.onBanPhaseUpdated += self.__updateData
        return

    def __removeListeners(self):
        self.viewModel.pollServerTime -= self.__onPollServerTime
        vehicleBanCtrl = self.__getVehicleBanCtrl()
        if vehicleBanCtrl is not None:
            vehicleBanCtrl.onBanPhaseUpdated -= self.__updateData
        return

    @replaceNoneKwargsModel
    def __updateData(self, model=None):
        vehicleBanCtrl = self.__getVehicleBanCtrl()
        fillBanProgressionModel(self.viewModel, vehicleBanCtrl)

    def __onPollServerTime(self):
        self.__updateData()

    def __getVehicleBanCtrl(self):
        return self.__sessionProvider.dynamic.getControllerByID(BATTLE_CTRL_ID.COMP7_VEHICLE_BAN_CTRL)


class BanProgressionWindow(WindowImpl):
    __slots__ = ()

    def __init__(self, parent=None):
        super(BanProgressionWindow, self).__init__(wndFlags=WindowFlags.WINDOW | WindowFlags.WINDOW_FULLSCREEN, content=BanProgressionView(), parent=parent)
