# wot-extractor: codigo DESCOMPILADO de sources/res/comp7_light/scripts/client/comp7_light/gui/battle_control/controllers/repositories.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7_light/scripts/client/comp7_light/gui/battle_control/controllers/repositories.py
from __future__ import absolute_import
from comp7_core.gui.battle_control.controllers.appearance_cache_ctrls.comp7_appearance_cache_ctrl import Comp7AppearanceCacheController
from comp7_core.gui.battle_control.controllers.comp7_vehicle_ban_ctrl import Comp7VehicleBanController
from comp7_core.gui.battle_control.controllers.comp7_voip_ctrl import Comp7VOIPController
from comp7_core.gui.battle_control.controllers.sound_ctrls.comp7_battle_sounds import Comp7BattleSoundController
from gui.battle_control.controllers.prebattle_setup_ctrl import PrebattleSetupController
from gui.battle_control.controllers.repositories import ClassicControllersRepository
from helpers import dependency
from skeletons.gui.game_control import IComp7LightController

class Comp7LightControllerRepository(ClassicControllersRepository):
    __slots__ = ()
    __comp7LightController = dependency.descriptor(IComp7LightController)

    @classmethod
    def create(cls, setup):
        repository = super(Comp7LightControllerRepository, cls).create(setup)
        settings = cls.__comp7LightController.getModeSettings()
        isTeamChannelAvailable = settings.createVivoxTeamChannels if settings is not None else False
        repository.addArenaController(Comp7VOIPController(isTeamChannelAvailable), setup)
        repository.addController(Comp7BattleSoundController())
        repository.addController(Comp7VehicleBanController())
        repository.addArenaViewController(PrebattleSetupController(setup), setup)
        return repository

    @staticmethod
    def _getAppearanceCacheController(setup):
        return Comp7AppearanceCacheController(setup)
