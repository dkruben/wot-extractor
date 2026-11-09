# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/prb_control/formatters/windows.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/formatters/windows.py
from gui.impl import backport
from gui.impl.gen import R
from helpers import dependency
from skeletons.gui.lobby_context import ILobbyContext

class SwitchPeripheryCtx(object):

    def __init__(self, isForbidden=True):
        super(SwitchPeripheryCtx, self).__init__()
        self.__isForbidden = isForbidden

    def getHeader(self):
        raise NotImplementedError

    def getDescription(self):
        raise NotImplementedError

    def getSelectServerLabel(self):
        raise NotImplementedError

    def getApplySwitchLabel(self):
        raise NotImplementedError

    def getExtraChainSteps(self):
        raise NotImplementedError

    def getUpdateTime(self):
        return 0

    def isPeripheryAvailable(self, peripheryID):
        if self.__isForbidden:
            return peripheryID not in self._getForbiddenPeripherieIDs()
        return peripheryID in self._getAllowedPeripherieIDs()

    def _getForbiddenPeripherieIDs(self):
        raise NotImplementedError

    def _getAllowedPeripherieIDs(self):
        raise NotImplementedError


class SwitchPeripheryFortCtx(SwitchPeripheryCtx):
    lobbyContext = dependency.descriptor(ILobbyContext)

    def getHeader(self):
        return backport.msgid(R.strings.prebattle.switchPeripheryWindow.fort.header())

    def getDescription(self):
        return backport.msgid(R.strings.prebattle.switchPeripheryWindow.fort.description())

    def getSelectServerLabel(self):
        return backport.msgid(R.strings.prebattle.switchPeripheryWindow.fort.selectServerLabel())

    def getApplySwitchLabel(self):
        return backport.msgid(R.strings.prebattle.switchPeripheryWindow.fort.applySwitchLabel())

    def getExtraChainSteps(self):
        return

    def _getForbiddenPeripherieIDs(self):
        return self.lobbyContext.getServerSettings().getForbiddenSortiePeripheryIDs()
