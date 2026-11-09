# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/halloween/messenger/formatters/invites.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/halloween/messenger/formatters/invites.py
from __future__ import absolute_import
from gui.prb_control.formatters.invites import PrbInviteHtmlTextFormatter
from halloween.skeletons.halloween_controller import IHalloweenController
from helpers import dependency

class HalloweenPrbInviteHtmlTextFormatter(PrbInviteHtmlTextFormatter):
    __halloweenCtrl = dependency.descriptor(IHalloweenController)

    def canAcceptInvite(self, invite):
        canAccept = super(HalloweenPrbInviteHtmlTextFormatter, self).canAcceptInvite(invite)
        return canAccept and self.__halloweenCtrl.isAvailable()
