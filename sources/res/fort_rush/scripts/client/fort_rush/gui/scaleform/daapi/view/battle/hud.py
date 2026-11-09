# wot-extractor: codigo DESCOMPILADO de sources/res/fort_rush/scripts/client/fort_rush/gui/scaleform/daapi/view/battle/hud.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fort_rush/scripts/client/fort_rush/gui/scaleform/daapi/view/battle/hud.py
from __future__ import absolute_import
from gui.impl.gen import R
from helpers import dependency
from skeletons.gui.impl import IGuiLoader
from fort_rush.gui.impl.battle.fort_rush_hud import FortRushHudView

class FortRushHudComponent(object):
    FORT_RUSH_HUD_R = R.views.fort_rush.mono.battle.fort_rush_hud()
    gui = dependency.descriptor(IGuiLoader)

    @property
    def hud(self):
        return self.gui.windowsManager.getViewByLayoutID(self.FORT_RUSH_HUD_R)
