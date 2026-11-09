# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/Scaleform/daapi/view/lobby/rally/action_button_state_vo.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/Scaleform/daapi/view/lobby/rally/action_button_state_vo.py
from __future__ import absolute_import
from gui.impl import backport
from gui.impl.gen import R
from gui.prb_control.settings import UNIT_RESTRICTION
from helpers import dependency
from skeletons.gui.game_control import IComp7Controller

@dependency.replace_none_kwargs(comp7Ctrl=IComp7Controller)
def unitRestrictionsGetter(comp7Ctrl=None):
    return {(UNIT_RESTRICTION.RANK_RESTRICTION): (
                                           backport.text(R.strings.comp7_ext.unit.message.rankRangeRestriction()), {}), 
       (UNIT_RESTRICTION.MODE_OFFLINE): (
                                       backport.text(R.strings.comp7_ext.unit.message.modeOffline()), {})}
