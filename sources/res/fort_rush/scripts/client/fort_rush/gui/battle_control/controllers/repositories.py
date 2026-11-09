# wot-extractor: codigo DESCOMPILADO de sources/res/fort_rush/scripts/client/fort_rush/gui/battle_control/controllers/repositories.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fort_rush/scripts/client/fort_rush/gui/battle_control/controllers/repositories.py
from __future__ import absolute_import
from fort_rush.gui.battle_control.controllers import respawn_ctrl
from fort_rush.gui.battle_control.controllers.spectator_ctrl import FortRushSpectatorViewController
from gui.battle_control.controllers.repositories import SharedControllersRepository, ClassicControllersRepository
from gui.battle_control.controllers.spectator_ctrl import SpectatorViewController

class FortRushControllerRepository(ClassicControllersRepository):
    __slots__ = ()

    @classmethod
    def create(cls, setup):
        repository = super(FortRushControllerRepository, cls).create(setup)
        repository.addViewController(respawn_ctrl.FortRushRespawnViewController(), setup)
        return repository


class FortRushSharedControllersRepository(SharedControllersRepository):
    __slots__ = ()

    def addViewController(self, ctrl, setup):
        if isinstance(ctrl, SpectatorViewController):
            ctrl = FortRushSpectatorViewController()
        super(FortRushSharedControllersRepository, self).addViewController(ctrl, setup)
