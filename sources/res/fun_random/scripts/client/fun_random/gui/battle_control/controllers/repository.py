# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/battle_control/controllers/repository.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/battle_control/controllers/repository.py
from __future__ import absolute_import
from fun_random.gui.battle_control.controllers.sound_ctrls.fun_random_battle_sounds import createFunRandomBattleSoundsController
from gui.battle_control.controllers.repositories import ClassicControllersRepository

class FunRandomControllerRepository(ClassicControllersRepository):
    __slots__ = ()

    @classmethod
    def create(cls, setup):
        repository = super(FunRandomControllerRepository, cls).create(setup)
        repository.addController(createFunRandomBattleSoundsController(setup))
        return repository
