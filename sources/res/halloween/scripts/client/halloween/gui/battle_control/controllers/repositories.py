# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/halloween/gui/battle_control/controllers/repositories.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/halloween/gui/battle_control/controllers/repositories.py
from __future__ import absolute_import
from gui.battle_control.controllers import battle_field_ctrl, debug_ctrl, team_bases_ctrl, default_maps_ctrl, perk_ctrl
from gui.battle_control.controllers.battle_hints import controller as battle_hints_ctrl
from gui.battle_control.controllers.repositories import ControllersRepositoryByBonuses, SharedControllersRepository
from gui.battle_control.controllers.sound_ctrls.common import ShotsResultSoundController
from halloween.gui.battle_control.controllers import appearance_cache_ctrl
from halloween.gui.battle_control.controllers import battle_gui_controller
from halloween.gui.battle_control.controllers import personal_death_zones_gui_ctrl
from halloween.gui.battle_control.controllers import arena_border_ctrl

class HalloweenControllerRepository(ControllersRepositoryByBonuses):
    __slots__ = ()

    @classmethod
    def create(cls, setup):
        repository = super(HalloweenControllerRepository, cls).create(setup)
        repository.addArenaViewController(team_bases_ctrl.createTeamsBasesCtrl(setup), setup)
        repository.addViewController(debug_ctrl.DebugController(), setup)
        repository.addViewController(default_maps_ctrl.DefaultMapsController(setup), setup)
        repository.addArenaViewController(battle_field_ctrl.BattleFieldCtrl(), setup)
        repository.addViewController(perk_ctrl.PerksController(), setup)
        repository.addViewController(battle_hints_ctrl.BattleHintsController(), setup)
        repository.addArenaController(appearance_cache_ctrl.HalloweenAppearanceCacheController(setup), setup)
        repository.addArenaController(battle_gui_controller.HWBattleGUIController(), setup)
        repository.addController(personal_death_zones_gui_ctrl.HWPersonalDeathZonesGUIController())
        repository.addController(ShotsResultSoundController())
        return repository


class HalloweenSharedControllersRepository(SharedControllersRepository):

    @classmethod
    def getArenaBorderController(cls):
        return arena_border_ctrl.HWArenaBorderController()
