# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/battle_control/arena_info/arena_descrs.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/battle_control/arena_info/arena_descrs.py
from __future__ import absolute_import
from gui.battle_control.arena_info.arena_descrs import ArenaDescriptionWithInvitation
from gui.impl import backport
from fun_random.gui.feature.util.fun_mixins import FunAssetPacksMixin, FunSubModesWatcher
from fun_random.gui.feature.util.fun_wrappers import hasBattleSubMode

class FunRandomArenaDescription(ArenaDescriptionWithInvitation, FunAssetPacksMixin, FunSubModesWatcher):

    def getBattleTypeIconPath(self, sizeFolder='c_136x136'):
        iconRes = self.getModeIconsResRoot().battleTypes.dyn(sizeFolder).dyn(self.getFrameLabel())
        if iconRes.exists():
            return backport.image(iconRes())
        return ''

    def getDescriptionString(self, isInBattle=True):
        return self.__getDescriptionString() or self.getModeUserName()

    @hasBattleSubMode(defReturn='')
    def __getDescriptionString(self):
        subModeName = backport.text(self.getBattleSubMode(self._visitor).getLocalsResRoot().userName())
        return self.getModeDetailedUserName(subModeName=subModeName)
