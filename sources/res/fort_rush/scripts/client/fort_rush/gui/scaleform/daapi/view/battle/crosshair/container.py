# wot-extractor: codigo DESCOMPILADO de sources/res/fort_rush/scripts/client/fort_rush/gui/scaleform/daapi/view/battle/crosshair/container.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fort_rush/scripts/client/fort_rush/gui/scaleform/daapi/view/battle/crosshair/container.py
from __future__ import absolute_import
import typing
from fort_rush.gui.scaleform.daapi.view.battle.crosshair.plugins import createPlugins, SHOT_RESULT_INDICATOR
from gui.Scaleform.daapi.view.battle.shared.crosshair import CrosshairPanelContainer
if typing.TYPE_CHECKING:
    from gui.shared.utils.plugins import IPlugin

class FortRushCrosshairPanelContainer(CrosshairPanelContainer):

    def __init__(self):
        super(FortRushCrosshairPanelContainer, self).__init__()
        self._addPlugins(createPlugins())

    def _getPlugins(self):
        enabledPlugins = super(FortRushCrosshairPanelContainer, self)._getPlugins()
        enabledPlugins.pop(SHOT_RESULT_INDICATOR)
        return enabledPlugins
