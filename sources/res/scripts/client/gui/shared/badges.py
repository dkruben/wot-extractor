# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/shared/badges.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/badges.py
from __future__ import absolute_import
from gui.doc_loaders.badges_loader import getAvailableBadges
from helpers import dependency
from skeletons.gui.shared.gui_items import IGuiItemsFactory

def buildBadge(badgeID, extraData=None):
    if badgeID != 0:
        allBadges = getAvailableBadges()
        badgeDescriptor = allBadges[badgeID].copy()
        if badgeDescriptor is not None:
            return dependency.instance(IGuiItemsFactory).createBadge(badgeDescriptor, extraData=extraData)
    return
