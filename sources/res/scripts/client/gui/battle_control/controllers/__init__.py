# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/battle_control/controllers/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_control/controllers/__init__.py
from __future__ import absolute_import
from gui.shared.system_factory import collectBattleControllerRepo, collectSharedControllerRepo, collectDynamicBattleControllerRepo
from gui.battle_control.controllers.repositories import BattleSessionSetup
from gui.battle_control.controllers.repositories import SharedControllersLocator
from gui.battle_control.controllers.repositories import DynamicControllersLocator
from gui.battle_control.controllers.repositories import ClassicControllersRepository
from gui.battle_control.controllers.repositories import SharedControllersRepository
from gui.battle_control.controllers.repositories import _ControllersRepository
__all__ = ('createShared', 'createDynamic', 'BattleSessionSetup', 'SharedControllersLocator',
           'DynamicControllersLocator', '_ControllersRepository', 'ClassicControllersRepository')

def createShared(setup):
    repository, inited = collectSharedControllerRepo(setup.arenaVisitor.gui.guiType, setup)
    if not inited:
        repository = SharedControllersRepository.create(setup)
    return SharedControllersLocator(repository=repository)


def createDynamic(setup):
    repository, inited = collectBattleControllerRepo(setup.arenaVisitor.gui.guiType, setup)
    if not inited:
        repository, isDynamicInited = collectDynamicBattleControllerRepo(setup)
        if not isDynamicInited:
            repository = ClassicControllersRepository.create(setup)
    return DynamicControllersLocator(repository=repository)
