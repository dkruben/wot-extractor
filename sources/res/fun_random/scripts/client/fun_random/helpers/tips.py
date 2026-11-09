# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/helpers/tips.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/helpers/tips.py
from __future__ import absolute_import
import random
from cgf_components.marker_component import IBattleSessionProvider
from fun_random.gui.feature.util.fun_mixins import FunSubModesWatcher
from fun_random.gui.feature.util.fun_wrappers import hasBattleSubMode
from gui.impl.gen import R
from helpers import dependency
from helpers.tips import TipsCriteria, TipData

class FunRandomTipsCriteria(TipsCriteria, FunSubModesWatcher):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    @hasBattleSubMode(defReturn=TipData(R.invalid(), R.invalid(), R.invalid()))
    def find(self):
        battleSubMode = self.getBattleSubMode(self.__sessionProvider.arenaVisitor)
        iconsRoot = battleSubMode.getIconsResRoot()
        tips = [TipData(tipRes.title(), tipRes.description(), iconsRoot.tips.dyn(tipID)()) for tipID, tipRes in battleSubMode.getLocalsResRoot().dyn('tips').items()]
        if tips:
            return random.choice(tips)
        return TipData(R.invalid(), R.invalid(), R.invalid())

    def _getTipsValidator(self):
        return
