# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/battle_control/arena_info/arena_descrs.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/battle_control/arena_info/arena_descrs.py
from __future__ import absolute_import
from gui.battle_control.arena_info.arena_descrs import ArenaDescriptionWithInvitation
from gui.impl import backport
from gui.impl.gen import R

class Comp7BattlesDescription(ArenaDescriptionWithInvitation):

    def getBattleTypeIconPath(self, sizeFolder='c_136x136'):
        iconRes = R.images.comp7.gui.maps.icons.battleTypes.dyn(sizeFolder).dyn(self.getFrameLabel())
        if iconRes.exists():
            return backport.image(iconRes())
        return ''
