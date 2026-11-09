# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/battle_control/controllers/hit_direction_ctrl/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_control/controllers/hit_direction_ctrl/__init__.py
from __future__ import absolute_import
from gui.battle_control.controllers.hit_direction_ctrl.base import HitType, IHitIndicator
from gui.battle_control.controllers.hit_direction_ctrl.ctrl import HitDirectionControllerPlayer, HitDirectionController
from gui.shared.system_factory import collectHitDirectionController
__all__ = ('HitType', 'IHitIndicator', 'createHitDirectionController')

def createHitDirectionController(setup):
    hitDirectionControllerType, hitDirectionControllerPlayerType = collectHitDirectionController(setup.arenaVisitor.gui.guiType, HitDirectionController, HitDirectionControllerPlayer)
    if setup.isReplayPlaying:
        return hitDirectionControllerPlayerType(setup)
    return hitDirectionControllerType(setup)
