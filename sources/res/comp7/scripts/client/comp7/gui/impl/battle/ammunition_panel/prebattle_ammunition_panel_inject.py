# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/impl/battle/ammunition_panel/prebattle_ammunition_panel_inject.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/impl/battle/ammunition_panel/prebattle_ammunition_panel_inject.py
from __future__ import absolute_import
from comp7.gui.impl.battle.ammunition_panel.prebattle_ammunition_panel_view import Comp7PrebattleAmmunitionPanelView
from comp7_core.gui.impl.battle.ammunition_panel.prebattle_ammunition_panel_inject import Comp7CorePrebattleAmmunitionPanelInject

class Comp7PrebattleAmmunitionPanelInject(Comp7CorePrebattleAmmunitionPanelInject):

    def _makeInjectView(self, vehicle, *args):
        return Comp7PrebattleAmmunitionPanelView(vehicle, *args)
