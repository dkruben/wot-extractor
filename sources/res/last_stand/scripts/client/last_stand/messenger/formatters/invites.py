# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/last_stand/messenger/formatters/invites.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/last_stand/messenger/formatters/invites.py
from __future__ import absolute_import
from gui.prb_control.formatters.invites import PrbInviteHtmlTextFormatter
from last_stand.skeletons.ls_controller import ILSController
from helpers import dependency

class LSPrbInviteHtmlTextFormatter(PrbInviteHtmlTextFormatter):
    lsCtrl = dependency.descriptor(ILSController)

    def canAcceptInvite(self, invite):
        canAccept = super(LSPrbInviteHtmlTextFormatter, self).canAcceptInvite(invite)
        return canAccept and self.lsCtrl.isAvailable()
