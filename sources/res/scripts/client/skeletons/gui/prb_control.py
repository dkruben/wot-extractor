# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/skeletons/gui/prb_control.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/skeletons/gui/prb_control.py


class IPrbControlLoader(object):
    __slots__ = ()

    def init(self):
        raise NotImplementedError

    def fini(self):
        raise NotImplementedError

    def getDispatcher(self):
        raise NotImplementedError

    def getInvitesManager(self):
        raise NotImplementedError

    def getAutoInvitesNotifier(self):
        raise NotImplementedError

    def getPeripheriesHandler(self):
        raise NotImplementedError

    def getStorage(self):
        raise NotImplementedError

    def isEnabled(self):
        raise NotImplementedError

    def setEnabled(self, enabled):
        raise NotImplementedError

    def onAccountShowGUI(self, ctx):
        raise NotImplementedError

    def onAvatarBecomePlayer(self):
        raise NotImplementedError

    def onDisconnected(self):
        raise NotImplementedError
