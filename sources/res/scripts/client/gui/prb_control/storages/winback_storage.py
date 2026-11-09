# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/prb_control/storages/winback_storage.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/storages/winback_storage.py
from gui.prb_control.storages.local_storage import SessionStorage
from helpers import dependency
from skeletons.gui.game_control import IWinbackController

class WinbackStorage(SessionStorage):
    __winbackController = dependency.descriptor(IWinbackController)

    def isModeSelected(self):
        return super(WinbackStorage, self).isModeSelected() and self.isModeAvailable()

    def isModeAvailable(self):
        return self.__winbackController.isModeAvailable()

    def _determineSelection(self, arenaVisitor):
        return arenaVisitor.gui.isWinback()
