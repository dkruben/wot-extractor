# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/profile/ProfileAchievementSection.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/profile/ProfileAchievementSection.py
from __future__ import absolute_import
from gui.Scaleform.daapi.view.meta.ProfileAchievementSectionMeta import ProfileAchievementSectionMeta
from helpers import dependency
from skeletons.gui.shared.utils import IRaresCache

class ProfileAchievementSection(ProfileAchievementSectionMeta):
    rareAchievesCache = dependency.descriptor(IRaresCache)

    def __init__(self, *args):
        super(ProfileAchievementSection, self).__init__(*args)
        self.rareAchievesCache.onImageReceived += self._onRareImageReceived

    def _onRareImageReceived(self, imgType, rareID, imageData):
        pass

    def _disposeRequester(self):
        self.rareAchievesCache.onImageReceived -= self._onRareImageReceived
