# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/Scaleform/daapi/view/lobby/battle_queue.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/Scaleform/daapi/view/lobby/battle_queue.py
from __future__ import absolute_import
from fun_random.gui.feature.util.fun_mixins import FunAssetPacksMixin, FunSubModesWatcher
from fun_random.gui.feature.util.fun_wrappers import hasDesiredSubMode
from gui.Scaleform.daapi.view.lobby.battle_queue.battle_queue import RandomQueueProvider
from gui.impl import backport

class FunRandomQueueProvider(RandomQueueProvider, FunAssetPacksMixin, FunSubModesWatcher):

    def getIconPath(self, iconlabel):
        return backport.image(self.getModeIconsResRoot().battleTypes.c_136x136.fun_random())

    def getTitle(self, guiType):
        return self.__getTitle() or self.getModeUserName()

    def processQueueInfo(self, qInfo):
        super(FunRandomQueueProvider, self).processQueueInfo(qInfo or {})

    @hasDesiredSubMode(defReturn=False)
    def needAdditionalInfo(self):
        if self._needAdditionalInfo is not None:
            return self._needAdditionalInfo
        else:
            hasBattleQueueWarning = self.getDesiredSubMode().getConfigurationModel().subMode.hasBattleQueueWarning
            if not hasBattleQueueWarning:
                self._needAdditionalInfo = False
            return super(FunRandomQueueProvider, self).needAdditionalInfo()

    @hasDesiredSubMode()
    def _doRequestQueueInfo(self, currPlayer):
        super(FunRandomQueueProvider, self)._doRequestQueueInfo(currPlayer)

    def _getRequestQueueInfoParams(self):
        return (
         self._queueType, self.getDesiredSubMode().getSubModeID())

    @hasDesiredSubMode(defReturn='')
    def __getTitle(self):
        subModeName = backport.text(self.getDesiredSubMode().getLocalsResRoot().userName())
        return self.getModeDetailedUserName(subModeName=subModeName)
