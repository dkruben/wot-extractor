# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/prb_control/formatters/invites.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/prb_control/formatters/invites.py
from __future__ import absolute_import
from fun_random_common.fun_constants import UNKNOWN_EVENT_ID
from fun_random.gui.feature.util.fun_mixins import FunAssetPacksMixin, FunSubModesWatcher
from fun_random.gui.feature.util.fun_wrappers import hasSpecifiedSubMode
from gui.impl import backport
from gui.impl.gen import R
from gui.prb_control.formatters.invites import PrbInviteHtmlTextFormatter
from gui.shared.utils.functions import makeTooltip
from gui.shared.utils.requesters import REQ_CRITERIA
from helpers import dependency
from shared_utils import first
from skeletons.gui.shared import IItemsCache

class FunPrbInviteHtmlTextFormatter(PrbInviteHtmlTextFormatter, FunAssetPacksMixin, FunSubModesWatcher):
    __itemsCache = dependency.descriptor(IItemsCache)

    def canAcceptInvite(self, invite):
        canAccept = super(FunPrbInviteHtmlTextFormatter, self).canAcceptInvite(invite)
        return canAccept and self.__hasAnyVehicle()

    def getIconPath(self, invite, pathMaker=None):
        return backport.image(self.getModeIconsResRoot().library.invite_notification())

    def updateTooltips(self, invite, canAccept, message):
        if not canAccept and 'buttonsLayout' in message and not self.__hasAnyVehicle():
            tooltip = makeTooltip(body=backport.text(R.strings.fun_random.invite.tooltip.noVehicles()))
            message['buttonsLayout'][0]['tooltip'] = tooltip
        return message

    def _getTitle(self, invite, kwargs=None):
        subModeID = first(invite.getExtraData('unitInviteExtras', []), UNKNOWN_EVENT_ID)
        detailedModeName = self.__getDetailedModeName(subModeID) or self.getModeUserName()
        return backport.text(R.strings.fun_random.invite.text.detailedTitle(), detailedModeName=detailedModeName)

    def __hasAnyVehicle(self):
        return bool(self.__itemsCache.items.getVehicles(REQ_CRITERIA.INVENTORY))

    @hasSpecifiedSubMode(defReturn='')
    def __getDetailedModeName(self, subModeID):
        subModeName = backport.text(self.getSubMode(subModeID).getLocalsResRoot().userName())
        return self.getModeDetailedUserName(subModeName=subModeName)
