# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/battle_control/arena_info/vos_collections.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/battle_control/arena_info/vos_collections.py
from __future__ import absolute_import
from past.builtins import cmp
from comp7.gui.battle_control.arena_info.arena_vos import Comp7Keys
from gui.battle_control.arena_info.vos_collections import VehicleInfoSortKey

class Comp7SortKey(VehicleInfoSortKey):
    __slots__ = ()

    def _cmp(self, other):
        xvInfoVO = self.vInfoVO
        yvInfoVO = other.vInfoVO
        result = cmp(yvInfoVO.isAlive(), xvInfoVO.isAlive())
        if result:
            return result
        xvIsQual = xvInfoVO.gameModeSpecific.getValue(Comp7Keys.IS_QUAL_ACTIVE, default=False)
        yvIsQual = yvInfoVO.gameModeSpecific.getValue(Comp7Keys.IS_QUAL_ACTIVE, default=False)
        result = cmp(xvIsQual, yvIsQual)
        if result:
            return result
        xvRank = xvInfoVO.gameModeSpecific.getValue(Comp7Keys.RANK, default=(0, 0))
        yvRank = yvInfoVO.gameModeSpecific.getValue(Comp7Keys.RANK, default=(0, 0))
        result = cmp(xvRank, yvRank)
        if result:
            return result
        return cmp(xvInfoVO.player, yvInfoVO.player)
