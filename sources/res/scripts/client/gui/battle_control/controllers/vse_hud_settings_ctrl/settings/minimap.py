# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/battle_control/controllers/vse_hud_settings_ctrl/settings/minimap.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_control/controllers/vse_hud_settings_ctrl/settings/minimap.py
from __future__ import absolute_import
from gui.battle_control.controllers.vse_hud_settings_ctrl.settings.base_models import BaseClientModel

class MinimapClientModel(BaseClientModel):
    __slots__ = ('showGrid', 'minimumAnimationDuration', 'maximumAnimationDuration',
                 'animationDurationPerMeter', 'minimumAnimationDistance', 'canToggleFullMap')

    def __init__(self, showGrid, canToggleFullMap, minimumAnimationDuration, maximumAnimationDuration, animationDurationPerMeter, minimumAnimationDistance):
        super(MinimapClientModel, self).__init__()
        self.showGrid = showGrid
        self.canToggleFullMap = canToggleFullMap
        self.minimumAnimationDuration = minimumAnimationDuration
        self.maximumAnimationDuration = maximumAnimationDuration
        self.animationDurationPerMeter = animationDurationPerMeter
        self.minimumAnimationDistance = minimumAnimationDistance

    def __repr__(self):
        return ('<MinimapClientModel>: showGrid=%s, minimumAnimationDuration=%s, maximumAnimationDuration=%s, ' + 'animationDurationPerMeter=%s, minimumAnimationDistance=%s, canToggleFullMap=%s') % (
         self.showGrid,
         self.minimumAnimationDuration,
         self.maximumAnimationDuration,
         self.animationDurationPerMeter,
         self.minimumAnimationDistance,
         self.canToggleFullMap)
