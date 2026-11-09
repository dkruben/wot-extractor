# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/death_cam_hud.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/shared/death_cam_hud.py
from __future__ import absolute_import
from gui.Scaleform.daapi.view.meta.DeathCamHudMeta import DeathCamHudMeta
from gui.shared import EVENT_BUS_SCOPE
from gui.shared.events import GameEvent, DeathCamEvent

class DeathCamHud(DeathCamHudMeta):

    def onAnimationFinished(self):
        self.fireEvent(GameEvent(DeathCamEvent.DEATH_CAM_HIDDEN), scope=EVENT_BUS_SCOPE.BATTLE)
